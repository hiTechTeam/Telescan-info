# Telescan Whitepaper

## Purpose and scope

Telescan connects nearby people through the public Telegram profiles they
choose to share. Bluetooth Low Energy (BLE) performs local discovery, while a
small authenticated backend manages accounts, sessions, profiles, and photos.

The current product scope is intentionally narrow: link an account through a
Telegram bot, enable discovery in the iOS app, see nearby Telescan identities,
load their shared profiles, and open a selected Telegram username. Telescan has
native reporting and profile blocking, but no chat, GPS tracking, encounter
history, analytics, or advertising system.

## System architecture

Telescan is split across independent repositories with explicit ownership
boundaries:

- **iOS app:** registration, Keychain-backed device sessions, BLE scanning and
  advertising, approximate distance, profile display, photo management, logout,
  reports, blocking, and account deletion.
- **Telegram bot:** Telegram commands, current profile-data forwarding, display
  of one-time codes, and server-side confirmation messages.
- **Admin bot:** allow-listed Telegram moderation for report review, decisions,
  notes, notifications, and moderator attribution.
- **API:** the only application service that reads or writes MongoDB and
  S3-compatible photo storage.
- **Database repository:** MongoDB 8 runtime plus encrypted off-host backup and
  restore-validation automation.
- **nginx:** TLS termination, automatic certificate renewal, and public routing
  policy.

```mermaid
flowchart LR
    U["User"] --> BOT["Telegram bot"]
    M["Allow-listed moderator"] --> ADMIN["Admin bot"]
    U --> IOS["iOS app"]
    IOS <-->|"BLE: telescan_id"| PEER["Nearby iOS app"]
    IOS -->|"HTTPS + device session"| API["Telescan API"]
    PEER -->|"HTTPS + device session"| API
    BOT -->|"Internal API + service secret"| API
    ADMIN -->|"Moderation API + separate secret"| API
    API -->|"Confirmation notification"| BOT
    API --> DB[("MongoDB")]
    API --> S3[("Photo storage")]
    DB -->|"Encrypted daily snapshot"| BACKUP[("Off-host Restic repository")]
    IOS --> TG["Telegram profile"]
```

The iOS app, user bot, and admin bot never receive MongoDB or S3 credentials.

## Registration, identity, and sessions

The bot reads the user's current Telegram ID, first name, username, and first
available profile photo for every new code. It forwards those fields and an
explicit photo state to the authenticated `/internal/v1` contract. The API
upserts the account, removes an obsolete photo when Telegram reports none, and
assigns a random, stable UUID called `telescan_id`. Failed photo downloads
preserve the existing photo; successful replacements use unique object URLs.

The API generates an eight-character code from uppercase letters and digits.
It stores an HMAC-SHA-256 digest, revokes any earlier unused code for that user,
and returns the clear code to the bot. The default validity period is ten
minutes. Code consumption is atomic, records the installation `device_id`, and
can succeed only once.

The iOS app sends the clear code and a random installation UUID directly to the
API. On success, the API creates or replaces that device's session and returns:

- an HS256 access JWT, normally valid for 15 minutes;
- a random refresh token, normally valid for 30 days;
- the account's public profile and `telescan_id`.

Only a SHA-256 digest of the refresh token is stored. Refresh rotates the token
atomically; reuse of a previous refresh token revokes the affected session.
Every protected endpoint validates the JWT and confirms that its session is
still active, making revocation immediate.

The iOS Keychain stores access and refresh tokens plus the installation
`device_id`. The clear link code is cleared after the linking attempt and is not
persisted. Public profile metadata and discovery preferences may be stored in
`UserDefaults`.

## Session validation, logout, and account deletion

The current iOS MVP presents one account-actions alert with current-device
logout, account deletion, and cancellation. Each destructive choice opens its
own system confirmation. Current-device logout revokes one `DeviceSession` and
clears local account data and caches.

At launch and foreground activation, iOS requests `/api/v1/users/me`. A valid
response refreshes cached Telegram profile fields. A definitively invalid
session or missing current account clears local data; transport failures, rate
limits, malformed gateway responses, and `5xx` errors during validation or
token refresh preserve tokens, cached profile fields, and the cached photo. A
newly linked session clears local photo and HTTP caches before storing the fresh
profile.

The API and bot retain the two-channel logout-all confirmation contract for
compatibility, but the current iOS app does not expose or poll that flow. A
future multi-device logout UI should use reliable push delivery rather than
continuous client polling.

Account deletion is separate from logout. The API revokes sessions first, then
removes owned photos, link codes, confirmation requests, block relationships,
device sessions, and the user record. Existing reports lose their direct
database relation to the deleted account and follow their moderation-retention
window. Local tokens, profile metadata, blocked-ID cache, BLE state, stored
images, and caches are cleared only after the server confirms deletion.

## Reports, blocking, and moderation

The iOS profile sheet offers native report and block actions. Reports use a
client request UUID for idempotency and capture the target's current shared
profile, reason, optional context, status, timestamps, and moderator audit
fields. Repeated pending reports from the same reporter, target, and reason
collapse to one record.

Blocking is enforced by the API in both lookup directions. The app removes a
blocked profile from its list and open sheet, suppresses aggregate background
notifications for that identity, and caches the last successful blocked-ID set
for offline suppression. Users can list and remove their blocks in the app.

The deployed admin bot is restricted to configured Telegram IDs and accesses
reports only through the private moderation API with a credential separate from
the user-bot secret. It can move reports through pending, reviewing, resolved,
and dismissed states, attach moderator notes, and records the acting moderator.
It has no MongoDB credentials and exposes no public port.

## BLE discovery protocol

Each discoverable iPhone publishes a custom primary GATT service:

| Item | Value |
| --- | --- |
| Service UUID | `A6B50001-8A5D-4F7A-9E4C-123456789001` |
| Compact identity characteristic | `A6B50003-8A5D-4F7A-9E4C-123456789003` |
| Compact identity value | Full `telescan_id` UUID encoded as 16 lossless bytes |
| Compatibility characteristic | `A6B50002-8A5D-4F7A-9E4C-123456789002` |
| Compatibility value | Lowercase `telescan_id` UUID encoded as UTF-8 |
| Characteristic access | Readable |

Only the fixed service UUID is advertised. The `telescan_id` is never placed in
the size-constrained advertisement local name. A scanner connects, reads the
compact characteristic, and caches the peripheral-to-identity mapping. The
text characteristic allows staged interoperability with the preceding iOS
release. Cached mappings are periodically revalidated and discarded after
repeated GATT failures.

```mermaid
sequenceDiagram
    participant A as Discoverable iPhone
    participant B as Scanning iPhone
    participant API as Telescan API

    A->>B: Advertise fixed service UUID
    B->>A: Connect and read compact identity characteristic
    A-->>B: Full 16-byte telescan_id
    B->>API: GET /api/v1/profiles/{telescan_id} with access token
    API-->>B: Shared name, username, and photo URL
    B->>B: Validate matching ID and required username
    B->>B: Publish complete profile in nearby UI
```

Duplicate advertisements update RSSI and presence without reconnecting on each
packet. A device expires after 10 seconds without a foreground sighting, with a
45-second background grace period for iOS scheduling. A raw BLE candidate is
never rendered: the app first obtains a matching API profile with a non-empty
Telegram username, retries transient failures with bounded exponential backoff,
and cancels resolution when presence is lost. CoreBluetooth state-restoration
identifiers are configured, but iOS still controls background scheduling, so
continuous discovery is not guaranteed.

Background nearby notifications contain only aggregate counts. A BLE identity
is counted only after the authenticated API returns a complete, accessible
profile. The last successful blocked-ID set is cached locally, so offline BLE
events do not reintroduce profiles blocked by the current account.

The random BLE identifier reduces direct exposure of the Telegram numeric ID,
but it is still a stable public pseudonym that nearby observers can capture,
replay, or correlate until the Telescan account is deleted.

## API surface and authorization

| Area | Paths | Credential |
| --- | --- | --- |
| Link and refresh | `/api/v1/auth/link`, `/api/v1/auth/refresh` | One-time code or refresh token |
| Session management | `/api/v1/auth/session`; retained `/api/v1/auth/logout-all/request` compatibility flow | Active access JWT and session |
| Own account | `/api/v1/users/me`, `/api/v1/users/me/photo` | Active access JWT and session |
| Nearby profiles | `/api/v1/profiles/{telescan_id}` | Active access JWT and session |
| Reports | `/api/v1/reports` | Active access JWT and session |
| Blocks | `/api/v1/users/me/blocks...` | Active access JWT and session |
| Bot operations | `/internal/v1/...` | Shared bot service Bearer secret |
| Moderation operations | `/internal/v1/moderation/reports...` | Separate moderation service Bearer secret |
| Legal pages | `/privacy`, `/terms` | Public |

Legacy `/v1` endpoints exist only behind the `ENABLE_LEGACY_API` migration
flag and are hidden from OpenAPI. Public nginx blocks `/internal/`, `/docs`,
`/docs/`, `/redoc`, and `/openapi.json` with `404`. Swagger remains available
only through the API's `127.0.0.1:8000` binding and an SSH tunnel.

## Server-side data model

MongoDB currently contains:

- `users`: random `telescan_id`, Telegram ID, name, username, photo URL, and
  timestamps;
- `link_codes`: HMAC digest, owner, status, expiry, consumption metadata, and
  an attempt counter updated on successful atomic consumption;
- `device_sessions`: installation ID, refresh-token digest, expiry, activity,
  and revocation metadata;
- `confirmation_requests`: public request ID, action, status, expiry, and
  temporary Telegram chat/message IDs;
- `reports`: reporter and target Telescan IDs, reason, optional context, target
  profile snapshot, review state, moderator audit fields, and retention time;
- `blocks`: unique blocker/target relation, target profile snapshot, and time.

Link codes, sessions, confirmations, and resolved or dismissed reports have TTL
indexes. Report creation is idempotent and duplicate pending reports from the
same reporter, target, and reason collapse to one record. Profile access is
hidden with `404` when either user has blocked the other. MongoDB TTL cleanup is
asynchronous, so an expired document may remain stored briefly after it is no
longer accepted by application logic. Profile objects use the
`users/{telescan_id}/...` prefix in S3-compatible storage.

## Distance estimation

RSSI is converted into a coarse distance estimate using the log-distance model:

`distance = 10 ^ ((TX - RSSI) / (10 × n))`

The current defaults are `TX = -59 dBm` at one metre and path-loss exponent
`n = 2`. The app keeps up to 30 samples for each visible identity, uses the
median, and updates displayed distance every three seconds. The result is a
relative proximity hint, not a physical measurement or safety boundary.

## Privacy and security boundaries

Implemented protections include one-time HMAC-protected link codes,
Keychain-backed client tokens, rotating refresh tokens, per-request session
validation, authenticated own-account mutations, a service credential for bot
traffic, a separate moderation credential, explicit production secrets,
unprivileged read-only application containers, encrypted verified database
backups, TLS renewal automation, protected repository branches, and public proxy
denial of internal and documentation routes.

Current limitations remain:

- any authenticated Telescan account that knows a valid `telescan_id` can query
  that shared profile; the API does not prove physical proximity;
- BLE identifiers and RSSI can be observed, replayed, or manipulated;
- the rate limiter is process-local and resets on restart;
- the bot service credential is a shared long-lived secret;
- moderation currently uses a small allow-listed Telegram bot rather than a
  full case-management console or multi-role permission model;
- remote multi-device logout is not exposed by the current iOS MVP;
- background BLE behavior is controlled by iOS;
- the legacy API must remain disabled except during the controlled migration
  window.

Telescan should be understood as public-profile discovery, not anonymity,
mutual identity proof, precise ranging, or end-to-end encryption.

## Operations and repository controls

The API, user bot, and admin bot run under unprivileged container users. Compose
uses read-only root filesystems, bounded tmpfs mounts, dropped Linux
capabilities, and `no-new-privileges`; the admin bot has one writable SQLite
volume for notification deduplication. API and user-bot deployments wait for
their health checks, and MongoDB is published only on server loopback.

A systemd timer creates a compressed MongoDB archive daily, validates it before
upload, stores it in a client-side encrypted Restic repository, restores the
latest snapshot into a verification volume, validates it again with
`mongorestore --dryRun`, and retains 7 daily, 5 weekly, and 12 monthly snapshots.
The first production restore validation completed successfully on August 16,
2026. A separate timer runs Certbot twice per day and reloads nginx after a
successful renewal command.

All seven repositories protect `main` with pull requests, prevent force-pushes
and deletion, and enable secret scanning with push protection, vulnerability
alerts, and Dependabot security updates. The iOS repository additionally
requires its Xcode 26.3 `Build and test` check before merge.

## Verification status

The current repositories include automated API authentication/deletion and
readiness tests, bot service/confirmation/liveness tests, iOS token-refresh
concurrency tests, BLE manager tests, Compose validation, Python
linting/formatting/type checks, Debug/Release iOS builds, secret-safe Docker build
contexts, health-gated deployments, hardened application containers, automated
certificate renewal, a verified encrypted production backup, repository security
controls, and an app-owned iOS privacy manifest. Physical-device BLE, production
MongoDB/S3 migration, recurring disaster-recovery drills, centralized monitoring,
alerting, and documented log retention remain operational checks.

This document describes the implementation on August 16, 2026. Source code is
licensed under the [MIT License](./LICENSE).
