# Telescan Public Roadmap

**Last reviewed: August 19, 2026.**

This roadmap describes product direction, not a release commitment. Priorities
may change after testing, user feedback, platform changes, or security review.

## Available in the current MVP

- Telegram account linking with a temporary one-time code.
- Per-device authenticated iOS sessions.
- Nearby iPhone discovery through Bluetooth Low Energy.
- Complete-profile validation before a nearby user is displayed.
- Approximate distance and a visible countdown before a lost profile disappears.
- Current-device logout and account deletion.
- Profile-photo refresh and local offline account cache.
- Reports, blocks, and in-app block management.
- Restricted moderation workflow for reviewing user reports.
- Aggregated nearby notifications that avoid exposing profile names.
- Production metrics, centralized logs, dashboards, and operational alerts.
- Encrypted off-host MongoDB backups with a completed restore drill.
- English and Russian product and legal information.

## Before a broad public launch

- Complete production signing, TestFlight validation, and App Store review
  materials.
- Finish accessibility and supported-iOS regression testing.
- Calibrate alert thresholds and formalize moderation response ownership.
- Schedule recurring recovery drills.

## Later directions

- Improve accessibility and localization.
- Refine nearby-notification controls and aggregation.
- Explore a more privacy-preserving versioned Bluetooth identity protocol.
- Expand moderation tools as the community grows.
- Consider Android interoperability after the Bluetooth contract is stable.

The core implementation repositories are private. Public release timing and
feature scope will be announced separately when confirmed.
