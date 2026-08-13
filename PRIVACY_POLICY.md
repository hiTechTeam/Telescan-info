# Privacy Policy for Telescan

**Public page:** [tgtelescan.ru/privacy](https://tgtelescan.ru/privacy)

**Effective date:** August 12, 2026

Telescan is an iOS app for discovering nearby users and opening the public Telegram profiles they choose to share. This policy describes the data used by the Telescan app, bot, API, database, and profile-photo storage. Use of the service is also governed by the [Terms of Service](./TERMS_OF_SERVICE.md).

## Data we process

When you register through the Telescan Telegram bot, the service receives your Telegram ID, first name, username, and current public profile photo from Telegram. The bot generates an eight-character authentication code and stores only its SHA-256 hash on the server. The original code is shown to you and may be stored locally by the iOS app so it can identify your account.

You may replace the profile photo by taking a new photo with the camera or selecting an image through the system photo picker. Telescan accesses only the image you choose, resizes and compresses it on the device, then uploads a copy to Telescan cloud storage. Camera and photo-library access occur only when you use these controls.

The service stores the following account data while your Telescan account is active:

- Telegram ID, first name, and username;
- hashed authentication code;
- a copy of your Telegram or user-selected profile photo in Telescan cloud storage.

During discovery, the app broadcasts your Telegram ID over Bluetooth Low Energy (BLE). Nearby Telescan devices use that ID to request your shared profile from the API. BLE signal strength and approximate distance are processed locally and are not sent to the Telescan server.

The app stores your own profile, authentication code, settings, and profile photo locally between launches. Nearby profiles are held temporarily while devices remain visible. Images and network responses may also be cached by iOS and the image-loading library.

Our web infrastructure may process standard request metadata, including IP address, time, path, and response status, for delivery, reliability, and security. Telescan does not use this information for advertising or behavioral analytics.

## Data we do not collect

Telescan does not request or store GPS location, contacts, Telegram messages, advertising identifiers, or movement history. It does not include advertising or third-party analytics SDKs.

## How data is used and shared

Account data is used only to register users, show shared profiles, support profile-photo changes, operate nearby discovery, and maintain the service. Telescan does not sell personal data.

Data is disclosed only:

- to nearby Telescan users when you enable discoverability;
- to infrastructure providers needed to operate the API, database, and photo storage;
- when required by applicable law or a valid legal request.

Telescan uses Telegram for registration and for opening public profiles, but does not access Telegram messages or contacts. Telegram processes data under its own terms and privacy policy.

## Security and retention

API traffic uses HTTPS with TLS 1.2 or TLS 1.3. Authentication codes are hashed before transmission to the API and stored on the server only as hashes. No system can guarantee absolute security; current design limitations are documented in the [Security Policy](./SECURITY.md).

The live account record and stored profile photos remain until you delete the Telescan account. Local account data remains until account deletion or removal of the app. Temporary nearby-device data is cleared when devices leave range or discovery is reset. Operational request metadata follows the retention and rotation settings of the deployed infrastructure.

## Account and data deletion

Open your profile in the app, select **Delete account**, and confirm the request. Telescan then removes the live account record, hashed authentication code, current and earlier stored profile photos, and locally stored account data and caches. The operation cannot be undone.

Deleting Telescan does not delete or modify your Telegram account. Information that must be retained by law may be kept only for the legally required period.

## Your choices

You can disable discoverability at any time, replace or remove your profile photo, update the authentication code through the bot, and delete the account in the app. Depending on applicable law, you may also have rights to access, correct, restrict, or object to processing of personal data.

Telescan is not intended for children under 13. Age requirements may be higher where local law requires it.

## Changes and contact

We may update this policy when the service or legal requirements change. The effective date above identifies the current version.

For privacy questions, contact [admin@tgtelescan.ru](mailto:admin@tgtelescan.ru).
