# Privacy Policy for Telescan

**Public page:** [tgtelescan.ru/privacy](https://tgtelescan.ru/privacy)

**Effective date:** August 14, 2026

Telescan is an iOS app for discovering nearby users and opening the public
Telegram profiles they choose to share. This policy describes data processed by
the Telescan app, Telegram bot, API, MongoDB database, web proxy, and
S3-compatible profile-photo storage. Use of the service is also governed by the
[Terms of Service](./TERMS_OF_SERVICE.md).

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

The Telegram ID is used for account linking and Telegram confirmation messages.
It is not broadcast over BLE and is not returned by the current public profile
API.

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

Logout-all requests temporarily store a random confirmation ID, action, status,
expiry, and the Telegram chat/message IDs required to remove inline buttons and
process the decision.

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
shared profiles, manage photos, operate nearby discovery, confirm sensitive
session actions, prevent abuse, and maintain the service. Telescan does not sell
personal data.

Data may be disclosed:

- to authenticated Telescan users who receive or otherwise know your advertised
  `telescan_id`;
- to Telegram when the bot sends codes or confirmation messages;
- to infrastructure providers needed to operate HTTPS, MongoDB, and photo
  storage;
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

Local session and profile data remain until logout, account deletion, or normal
cache eviction, depending on the item. The installation UUID is retained across
logout and account deletion so a later link can identify the same installation;
it remains locally unlinked after the server session and account records are
deleted. It is removed only when the corresponding Keychain item is erased.

## Account and data deletion

Open your profile in the app, select **Delete account**, and confirm. After the
server accepts the authenticated request, Telescan revokes all sessions and
removes profile photos, link codes, confirmation requests, device sessions, and
the account record. The app then clears local tokens, profile data, BLE state,
stored images, and caches. This operation cannot be undone.

Deleting a Telescan account does not delete or modify your Telegram account.
Information that must be retained by law may be kept only for the legally
required period.

## Your choices

You can disable discoverability, replace or remove your profile photo, sign out
one device, request confirmed logout on all devices, or permanently delete the
account. Depending on applicable law, you may also have rights to access,
correct, restrict, delete, or object to processing of personal data.

Telescan is not intended for children under 13. A higher minimum age may apply
under local law or Telegram and Apple platform rules.

## Changes and contact

We may update this policy when the service or legal requirements change. The
effective date above identifies the current version.

For privacy questions, contact
[admin@tgtelescan.ru](mailto:admin@tgtelescan.ru).
