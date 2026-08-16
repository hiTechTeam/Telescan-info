# Telescan Roadmap

**Last reviewed:** August 16, 2026

Telescan currently provides iOS-to-iOS BLE discovery, Telegram account linking,
random public BLE identities, authenticated per-device sessions, rotating
refresh tokens, fresh Telegram profile synchronization, current-device logout,
and in-app account deletion. The current iOS MVP does not expose logout-all.
Authenticated reports, two-way profile blocking, a local blocked-profile cache,
and in-app unblock management are implemented.

## Completed foundations

- API ownership of all MongoDB collections and S3-compatible photo operations.
- One-time expiring link codes stored as HMAC-SHA-256 digests.
- Short-lived access JWTs backed by active `DeviceSession` records.
- Atomic refresh-token rotation and reuse-triggered session revocation.
- Random `telescan_id` BLE identity instead of Telegram ID.
- Size-safe 16-byte BLE identity characteristic with staged text compatibility.
- Resolved-only nearby profile UI with presence expiry and retry cancellation.
- Offline-safe iOS profile cache and transient refresh-error handling.
- Authenticated own-profile, nearby-profile, photo, logout, and deletion routes.
- Service-authenticated bot/API integration and restart-safe confirmations.
- Retained server-side Telegram-confirmed logout-all contract for future clients.
- Public nginx denial of `/internal/`, Swagger, ReDoc, and OpenAPI routes.
- Secret-safe API and bot Docker build contexts plus restart and health policies.
- App-owned iOS privacy manifest for the required `UserDefaults` API reason.
- API, bot, and iOS automated tests plus Python lint, format, and type checks.
- Idempotent profile reports with target snapshots and moderation state.
- Two-way server-enforced blocking, offline-safe iOS suppression, and unblock UI.
- Service-authenticated internal moderation endpoints and a deployed,
  allow-listed Telegram admin bot with moderator audit fields.
- Unprivileged, read-only API, user-bot, and admin-bot containers with dropped
  capabilities.
- Automated TLS renewal with post-renewal nginx reload.
- Daily encrypted MongoDB backups with restore-to-volume validation and
  7-daily, 5-weekly, and 12-monthly retention.
- Protected `main` branches, secret scanning with push protection, vulnerability
  alerts, and Dependabot security updates across all repositories.
- Pull-request iOS CI on Xcode 26.3 with tests, Release build, and bundle checks.

## Current priorities

| Area | Direction | Status |
| --- | --- | --- |
| Migration | Disable the legacy API after supported iOS adoption, then remove legacy code hashes with the guarded migration command | Rollout required |
| Rate limiting | Replace the process-local limiter with a shared Redis-compatible implementation before horizontal scaling | Planned |
| Operations | Health-gated deployment, restart policies, certificate renewal, and encrypted backup/restore validation are implemented; centralized monitoring, alerting, log retention, recurring recovery drills, and documented secret rotation remain | In progress |
| Security | Review service-secret rotation, storage permissions, token incident response, and authenticated-profile enumeration risk | In progress |
| BLE | Test background behavior, restoration, power use, and identity replay on multiple physical iPhone models | In progress |
| Quality | Expand real MongoDB/S3 integration, API contract, bot failure, iOS UI, accessibility, and physical BLE tests | In progress |
| Protocol | Version and stabilize the BLE contract for additional clients | Planned |
| Android | Build an interoperable Android client after the BLE protocol is versioned | Planned |
| Product | Publish focused onboarding, support, and operational status documentation | Planned |
| Sessions | Revisit multi-device logout after APNs and an Apple Developer account are available; avoid foreground polling as the final design | Deferred for MVP |
| Moderation | Operate the allow-listed admin bot, define the moderator response SLA, document escalation, and add a richer admin console only when volume requires it | In progress |

## Design constraints

Features involving encounter history, compatibility scoring, advertising,
analytics, persistent chat, or AI recommendations are outside the current
privacy model. They require a separate threat model, explicit consent,
retention controls, deletion behavior, and updated legal documentation before
development.

## Contributing

Useful contributions include security review, physical-device BLE testing,
deployment automation, accessibility, translations, Android protocol work, and
failure-mode tests. Open an issue in the relevant repository before starting a
large change.
