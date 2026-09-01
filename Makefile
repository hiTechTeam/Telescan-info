.PHONY: check legal

legal:
	python3 scripts/generate_legal.py

check:
	python3 -m json.tool legal/legal_documents.json >/dev/null
	python3 scripts/generate_legal.py --check
