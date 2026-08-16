# Privacy Policy for Telescan

**Public page:** [tgtelescan.ru/privacy](https://tgtelescan.ru/privacy)

**Effective date:** August 16, 2026

Telescan is an iOS app for discovering nearby users and opening the public
Telegram profiles they choose to share. This policy describes data processed by
the Telescan app, Telegram bot, API, MongoDB database, web proxy, and
S3-compatible profile-photo storage and encrypted database-backup storage. Use
of the service is also governed by the [Terms of
Service](./TERMS_OF_SERVICE.md).

## Data we process

### Telegram profile and account data

When you request a link code through the Telescan Telegram bot, Telegram
provides the bot with your numeric Telegram ID, first name, username, and first
available public profile photo. The bot forwards those fields to the Telescan
API so it can create or update your Telescan account.

The active server account contains:

- a random public `telescan_id` UUID;
- Telegram ID, first name, and username;
- a profile-photo URL and timestamps;
- an internal database identifier.

The Telegram ID is used for account linking and retained server-side Telegram
confirmation support. It is not broadcast over BLE and is not returned by the
current public profile API.

### Authentication and session data

The API generates a short-lived, one-time link code. The clear code is returned
to the bot, shown to you, and later sent by the iOS app to the API over HTTPS.
The bot and iOS app do not persist it. The server stores an HMAC-SHA-256 digest,
status, timestamps, expiry, a consumption-attempt counter, and the installation
ID that consumed the code.

For each linked installation, the server stores a random device UUID, a
SHA-256 digest of the rotating refresh token, creation and activity timestamps,
expiry, and optional revocation time. Access JWTs are validated against these
active sessions. The clear access token, refresh token, and installation UUID
are stored locally in the iOS Keychain.

If the retained server-side logout-all contract is invoked, it temporarily
stores a random confirmation ID, action, status, expiry, and the Telegram
chat/message IDs required to remove inline buttons and process the decision.
The current iOS MVP does not expose this request flow.

### Profile photos

The bot may copy your current Telegram profile photo when it updates the server
profile. In the app, you can replace that photo using the camera or system photo
picker. Telescan accesses only the image you choose, processes it on the device,
and uploads a copy to Telescan-managed S3-compatible storage under the account's
random `telescan_id` prefix.

### Nearby discovery

While discoverability is enabled, the app broadcasts your random public
`telescan_id` over BLE. Nearby Telescan devices use that UUID with their own
authenticated API session to request your shared name, username, and photo URL.
The Telegram ID and authentication tokens are not broadcast.

BLE signal strength, the approximate distance estimate, and the nearby-device
list are processed locally and are not sent to the Telescan server. A BLE UUID
is nevertheless observable and replayable by devices in radio range.

### Local app data

The iOS app may store:

- access and refresh tokens plus installation ID in Keychain;
- `telescan_id`, name, username, photo URL, registration state, BLE identity,
  and discovery preferences in `UserDefaults`;
- selected or cached profile images, HTTP responses, and image-library cache
  entries in app storage.

Nearby profiles are retained in memory while devices are visible and may also
be present in normal image or URL caches.

### Reports and blocks

When you report a profile, the API stores a random report ID, your and the
reported account's Telescan IDs, the selected reason, an optional comment, the
reported name, username, and photo URL as they appeared at that time, report
status, timestamps, and any later moderator actor and note. Capturing the
snapshot prevents a profile edit from removing the context a moderator needs.
The reported user is not shown the reporter's identity.

When you block a profile, the API stores the two internal account IDs, the
blocked Telescan ID, a profile snapshot, and creation time. The iOS app also
caches blocked Telescan IDs in `UserDefaults` so blocked profiles and nearby
notifications remain suppressed during a network outage. A block makes profile
lookups unavailable in both directions and can be removed from the app.

### Operational request data

Web infrastructure may process IP address, timestamp, requested path, response
status, user agent, and forwarding metadata for delivery, troubleshooting,
reliability, abuse prevention, and security. Telescan does not use this data for
advertising or behavioral analytics.

## Data we do not collect

Telescan does not request or store GPS location, contacts, Telegram messages,
advertising identifiers, movement history, or server-side encounter history. It
does not include advertising or third-party analytics SDKs.

## How data is used and shared

Data is used to link accounts, maintain authenticated device sessions, display
shared profiles, manage photos, operate nearby discovery, process reports and
blocks, support retained server-side confirmation actions, prevent abuse, and
maintain the service.
Telescan does not sell personal data.

Data may be disclosed:

- to authenticated Telescan users who receive or otherwise know your advertised
  `telescan_id`;
- to Telegram when the bot sends codes or confirmation messages;
- to infrastructure providers needed to operate HTTPS, MongoDB, photo storage,
  and encrypted backup storage;
- to authorized moderators who need report records and captured profile
  context to review possible abuse;
- when required by applicable law or a valid legal request.

Telegram and Apple process data under their own terms and privacy policies.
Telescan does not access Telegram messages or contacts.

## Security and retention

API traffic uses HTTPS with TLS 1.2 or TLS 1.3. Telescan uses one-time link-code
digests, rotating refresh tokens, active per-device session checks, Keychain
storage, and a private service credential between the API and bot. No system
can guarantee absolute security; current boundaries are documented in the
[Security Policy](./SECURITY.md).

The account record and current profile photo remain while the Telescan account
is active. Link codes, sessions, and confirmation requests have expirations and
MongoDB TTL indexes; cleanup is asynchronous and may occur after application
logic has already stopped accepting the expired record. Revoked sessions may
remain until deletion or expiry. Operational logs follow the retention and
rotation settings of deployed infrastructure.

Production database backups are stored in a client-side encrypted off-host
Restic repository. Automation retains up to 7 daily, 5 weekly, and 12 monthly
snapshots. Backup data is not used for normal profile access or product
analytics; it is accessed for recovery and restore verification. Data deleted
from the live service may remain inside an encrypted snapshot until that
snapshot expires under this rotation.

Blocks remain until you unblock the profile or either Telescan account is
deleted. Pending and reviewing reports remain until a moderation decision.
Resolved and dismissed reports are scheduled for automatic deletion 180 days
after that decision. Account deletion removes the live database relation to the
deleted reporter or reported account; a report snapshot and Telescan ID may be
retained for the remaining moderation and abuse-prevention period.

Local session and profile data remain until logout, account deletion, or normal
cache eviction, depending on the item. The installation UUID is retained across
logout and account deletion so a later link can identify the same installation;
it remains locally unlinked after the server session and account records are
deleted. It is removed only when the corresponding Keychain item is erased.

## Account and data deletion

Open your profile in the app, select **Delete account**, and confirm. After the
server accepts the authenticated request, Telescan revokes all sessions and
removes profile photos, link codes, confirmation requests, block relationships,
device sessions, and the account record. Existing abuse reports follow the
limited retention and relationship-removal rules above. The app then clears
local tokens, profile data, blocked-ID cache, BLE state, stored images, and
caches. Live-service deletion cannot be undone. Encrypted backup copies age out
under the backup-retention schedule described above and are not restored for
ordinary account recovery.

Deleting a Telescan account does not delete or modify your Telegram account.
Information that must be retained by law may be kept only for the legally
required period.

## Your choices

You can disable discoverability, replace or remove your profile photo, report
or block a profile, manage blocked profiles, sign out the current device, or
permanently delete the account and all its sessions.
Depending on applicable law, you may also have rights to access, correct,
restrict, delete, or object to processing of personal data.

Telescan is not intended for children under 13. A higher minimum age may apply
under local law or Telegram and Apple platform rules.

## Changes and contact

We may update this policy when the service or legal requirements change. The
effective date above identifies the current version.

For privacy questions, contact
[admin@tgtelescan.ru](mailto:admin@tgtelescan.ru).
