# Telescan Public Roadmap

**Last reviewed: September 1, 2026.**

This roadmap describes product direction, not a release commitment. Priorities
may change after testing, user feedback, platform changes, or security review.

## Available in the current MVP

- Telegram account linking with a temporary one-time code.
- Primary account authentication with Sign in with Apple.
- Per-device authenticated iOS sessions.
- Nearby iPhone discovery through Bluetooth Low Energy.
- Complete-profile validation before a nearby user is displayed.
- Approximate distance and a visible countdown before a lost profile disappears.
- Stable discovery-order rows with distance labels refreshed every 10 seconds.
- Device-local 24-hour history of profiles that have left the nearby list.
- Device-local Saved profiles and configurable quick chat, clear, and block
  actions.
- New-Met highlights plus application and profile badge aggregation.
- Current-device logout and account deletion.
- Optional 36-character BIO, profile-photo refresh, and local offline cache.
- Universal reports, blocks, and in-app block management.
- Restricted moderation workflow for reviewing user reports.
- Aggregated nearby notifications that avoid exposing profile names.
- Production metrics, centralized logs, dashboards, and operational alerts.
- Encrypted off-host MongoDB backups with a completed restore drill.
- English and Russian product and legal information.

## Before a broad public launch

- Complete Apple Developer enrollment, production signing, TestFlight
  validation, and App Store submission.
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
