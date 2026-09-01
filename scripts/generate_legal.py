#!/usr/bin/env python3
"""Generate public Markdown and an integrity manifest from the legal source."""

from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "legal" / "legal_documents.json"
MANIFEST_PATH = ROOT / "legal" / "LEGAL_MANIFEST.json"
OUTPUTS = {
    ("privacy", "en"): ROOT / "PRIVACY_POLICY.md",
    ("privacy", "ru"): ROOT / "PRIVACY_POLICY.ru.md",
    ("terms", "en"): ROOT / "TERMS_OF_SERVICE.md",
    ("terms", "ru"): ROOT / "TERMS_OF_SERVICE.ru.md",
}
KINDS = {"privacy", "terms"}
LANGUAGES = {"en", "ru"}
BLOCK_TYPES = {"paragraph", "list"}


def source_bytes() -> bytes:
    return SOURCE_PATH.read_bytes()


def load_source() -> dict[str, Any]:
    data = json.loads(source_bytes())
    validate_source(data)
    return data


def require_non_empty(value: Any, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{location} must be a non-empty string")
    return value


def require_iso_date(value: Any, location: str) -> str:
    value = require_non_empty(value, location)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value) is None:
        raise ValueError(f"{location} must be an ISO date")
    try:
        date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"{location} must be a valid calendar date") from error
    return value


def require_https_url(value: Any, location: str) -> str:
    value = require_non_empty(value, location)
    parsed = urlparse(value)
    if (
        parsed.scheme != "https"
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.fragment
    ):
        raise ValueError(f"{location} must be a credential-free HTTPS URL")
    return value


def validate_source(data: dict[str, Any]) -> None:
    if data.get("schema_version") != 1:
        raise ValueError("schema_version must be 1")
    require_iso_date(data.get("legal_version"), "legal_version")
    documents = data.get("documents")
    if not isinstance(documents, dict) or set(documents) != KINDS:
        raise ValueError("documents must contain exactly privacy and terms")

    section_ids: dict[tuple[str, str], set[str]] = {}
    for kind in sorted(KINDS):
        localized = documents[kind]
        if not isinstance(localized, dict) or set(localized) != LANGUAGES:
            raise ValueError(f"documents.{kind} must contain exactly en and ru")
        for language in sorted(LANGUAGES):
            document = localized[language]
            prefix = f"documents.{kind}.{language}"
            for field in ("title", "summary", "effective_label"):
                require_non_empty(document.get(field), f"{prefix}.{field}")
            require_iso_date(document.get("effective_date"), f"{prefix}.effective_date")
            require_https_url(document.get("canonical_url"), f"{prefix}.canonical_url")
            sections = document.get("sections")
            if not isinstance(sections, list) or not sections:
                raise ValueError(f"{prefix}.sections must be a non-empty list")
            ids: set[str] = set()
            for index, section in enumerate(sections):
                section_prefix = f"{prefix}.sections[{index}]"
                section_id = require_non_empty(
                    section.get("id"), f"{section_prefix}.id"
                )
                if section_id in ids:
                    raise ValueError(f"duplicate section id: {prefix}.{section_id}")
                ids.add(section_id)
                require_non_empty(section.get("title"), f"{section_prefix}.title")
                blocks = section.get("blocks")
                if not isinstance(blocks, list) or not blocks:
                    raise ValueError(f"{section_prefix}.blocks must be non-empty")
                for block_index, block in enumerate(blocks):
                    block_prefix = f"{section_prefix}.blocks[{block_index}]"
                    block_type = block.get("type")
                    if block_type not in BLOCK_TYPES:
                        raise ValueError(f"unsupported block type at {block_prefix}")
                    if block_type == "paragraph":
                        require_non_empty(block.get("text"), f"{block_prefix}.text")
                    else:
                        items = block.get("items")
                        if not isinstance(items, list) or not items:
                            raise ValueError(f"{block_prefix}.items must be non-empty")
                        for item_index, item in enumerate(items):
                            require_non_empty(
                                item, f"{block_prefix}.items[{item_index}]"
                            )
            section_ids[(kind, language)] = ids

    for kind in KINDS:
        if section_ids[(kind, "en")] != section_ids[(kind, "ru")]:
            raise ValueError(f"{kind} section ids differ between en and ru")


def render_markdown(document: dict[str, Any], language: str) -> str:
    if language == "ru":
        heading = document["title"]
        date_label = "Дата вступления в силу"
        effective = document["effective_label"].removeprefix("Действует с ")
    else:
        heading = f"Telescan {document['title']}"
        date_label = "Effective date"
        effective = document["effective_label"].removeprefix("Effective ")
    lines = [
        "<!-- Generated by scripts/generate_legal.py; edit legal/legal_documents.json. -->",
        "",
        f"# {heading}",
        "",
        f"**Public page:** [{document['canonical_url']}]({document['canonical_url']})",
        "",
        f"**{date_label}:** {effective}",
        "",
        document["summary"],
        "",
    ]
    for section in document["sections"]:
        lines.extend((f"## {section['title']}", ""))
        for block in section["blocks"]:
            if block["type"] == "paragraph":
                lines.extend((block["text"], ""))
            else:
                lines.extend(f"- {item}" for item in block["items"])
                lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_manifest(data: dict[str, Any]) -> str:
    digest = hashlib.sha256(source_bytes()).hexdigest()
    documents: dict[str, Any] = {}
    for kind in sorted(KINDS):
        documents[kind] = {}
        for language in sorted(LANGUAGES):
            document = data["documents"][kind][language]
            documents[kind][language] = {
                "canonical_url": document["canonical_url"],
                "effective_date": document["effective_date"],
            }
    manifest = {
        "schema_version": 1,
        "legal_version": data["legal_version"],
        "source": "legal/legal_documents.json",
        "source_sha256": digest,
        "documents": documents,
    }
    return json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def generated_files(data: dict[str, Any]) -> dict[Path, str]:
    files = {
        output: render_markdown(data["documents"][kind][language], language)
        for (kind, language), output in OUTPUTS.items()
    }
    files[MANIFEST_PATH] = render_manifest(data)
    return files


def check(files: dict[Path, str]) -> int:
    stale: list[str] = []
    for path, expected in files.items():
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            stale.append(str(path.relative_to(ROOT)))
    if stale:
        print("Generated legal files are stale:", file=sys.stderr)
        for path in stale:
            print(f"  - {path}", file=sys.stderr)
        print("Run: python3 scripts/generate_legal.py", file=sys.stderr)
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check", action="store_true", help="fail if generated files differ"
    )
    args = parser.parse_args()
    data = load_source()
    files = generated_files(data)
    if args.check:
        return check(files)
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
