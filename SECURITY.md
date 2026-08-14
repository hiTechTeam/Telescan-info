# Security Policy

## Reporting a vulnerability

Do not disclose a security vulnerability in a public GitHub issue or
discussion. Send a private report to
[r66cha@gmail.com](mailto:r66cha@gmail.com) with:

- the affected component and a clear description;
- reproducible steps or a proof of concept;
- expected impact;
- a suggested mitigation, if available.

We aim to acknowledge reports within 48 hours, investigate confirmed issues,
provide progress updates, and coordinate disclosure after a fix is available.
Timelines depend on severity and complexity.

While testing, do not access data without permission, disrupt the service,
degrade availability, or violate user privacy. Researchers may be credited with
their permission.

## Implemented security model

- The API is the sole owner of MongoDB and S3-compatible profile-photo access.
- Link codes are random, short-lived, one-time values. The API stores only an
  HMAC-SHA-256 digest and atomically records consumption.
- iOS stores access tokens, rotating refresh tokens, and its random installation
  ID in Keychain; it does not persist the clear link code.
- Access JWTs are accepted only while their referenced device session is active.
- Refresh-token reuse revokes the affected session.
- Own-profile reads, photo mutations, logout, nearby-profile reads, and account
  deletion require an active access token and session.
- Logout-all requires a second-channel decision from the linked Telegram user.
- Internal bot/API calls use a shared Bearer service secret and constant-time
  comparisons.
- Production API startup rejects built-in development secrets and wildcard or
  empty CORS configuration.
- nginx permits TLS 1.2/1.3 and returns `404` for `/internal/`, Swagger, ReDoc,
  and OpenAPI paths on every public domain.
- The app has no advertising or third-party analytics SDKs.

## BLE design

Telescan advertises a random public `telescan_id` UUID through a custom BLE
service. The UUID may appear in the advertisement local name; otherwise it can
be read from a GATT characteristic. Telegram IDs, access tokens, and refresh
tokens are not broadcast.

BLE traffic remains public to devices in radio range. A nearby observer can
capture, correlate, replay, or replace the advertised UUID and manipulate RSSI.
The protocol discovers a claimed Telescan identity; it does not prove physical
proximity, ownership, or authenticity.

## Current limitations

- A valid authenticated account can request any shared profile when it knows
  that profile's `telescan_id`; proximity is not verified server-side.
- API rate limiting is held in one process, is not shared between replicas, and
  resets on restart.
- `BOT_SERVICE_SECRET` is a long-lived shared credential and requires external
  rotation and secret-management procedures.
- Logout-all depends on Telegram and bot availability. Current-device logout
  and account deletion remain separate API operations.
- CoreBluetooth background scanning and advertising are scheduled by iOS and
  cannot be guaranteed continuously.
- A feature-flagged legacy API exists for a short migration window. Enabling it
  restores weaker compatibility behavior and must be treated as temporary.
- The repository tests do not replace physical-device BLE testing, production
  backup/restore drills, storage permission review, or deployment monitoring.

Telescan is intended for public-profile discovery and must not be used to share
sensitive information or as a safety, ranging, access-control, or identity
verification system.

## User guidance

- Enable discoverability only when you want the random Telescan identity to be
  visible nearby.
- Keep one-time codes private and enter them only in the official iOS app.
- If a device or token may be compromised, sign out that device or request
  logout-all and confirm it in the bot.
- Keep iOS, Telescan, and Telegram updated.
- Avoid using the app on a jailbroken device.

Security work is tracked in the [Roadmap](./ROADMAP.md). General questions can
be sent to [r66cha@gmail.com](mailto:r66cha@gmail.com).
