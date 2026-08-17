# Telescan

**Last reviewed: August 17, 2026.**

[![Swift](https://img.shields.io/badge/Swift-5.0-orange.svg)](https://swift.org)
[![iOS](https://img.shields.io/badge/iOS-17.6+-blue.svg)](https://developer.apple.com/ios/)
[![License](https://img.shields.io/badge/license-proprietary-lightgrey.svg)](./LICENSE)

Telescan is an iOS extension for Telegram that helps people nearby exchange the
public Telegram usernames they choose to share. Nearby discovery uses Bluetooth
Low Energy; profiles are loaded only for authenticated Telescan users.

![Telescan overview](./docs/images/slide1.png)

## How it works

1. Request a one-time linking code from the Telescan Telegram bot.
2. Enter the code in the iOS app to connect the current device.
3. Enable scanning when you want to be discoverable.
4. Open a nearby profile and copy its public Telegram username.
5. Disable scanning at any time to stop advertising your Telescan profile.

![Nearby exchange](./docs/images/slide2.png)

## Privacy at a glance

- Nearby devices exchange a random Telescan profile identifier, not your
  Telegram password, messages, contacts, or phone number.
- Bluetooth signal strength and approximate distance are processed on the
  device and are not sent to Telescan servers.
- Telescan does not request GPS location or maintain movement history.
- Your Telescan ID is advertised nearby only while discoverability is enabled;
  an authenticated user who already knows that ID may still request the shared
  profile.
- You can report or block a profile, remove your photo, sign out the current
  device, or delete the Telescan account from the app.
- Telescan contains no advertising or third-party behavioral analytics SDK.

Bluetooth visibility and distance are approximate and may be delayed by iOS.
Telescan must not be used for navigation, safety decisions, emergency response,
or precise proof that a person is physically present.

## Availability

The current client supports iOS 17.6 or newer and requires a Telegram account.
An internet connection is required for account linking, profile loading,
reports, blocks, photo updates, logout, and account deletion. Nearby Bluetooth
detection alone does not guarantee that a complete profile can be displayed.

The core application and infrastructure are developed in private repositories.
This public repository contains only product, policy, support, and
security-contact information.

## Policies and project information

- [Privacy Policy](./PRIVACY_POLICY.md)
- [Terms of Service](./TERMS_OF_SERVICE.md)
- [Security Policy](./SECURITY.md)
- [Public Roadmap](./ROADMAP.md)

The current public legal pages are also available at
[tgtelescan.ru/privacy](https://tgtelescan.ru/privacy) and
[tgtelescan.ru/terms](https://tgtelescan.ru/terms).

## Contact

- Developer: [Ruslan Chukavin](https://github.com/r66cha)
- Telegram: [@r_chukavin](https://t.me/r_chukavin)
- Email: [admin@tgtelescan.ru](mailto:admin@tgtelescan.ru)

## License

Copyright © 2025–2026 Ruslan Chukavin. All rights reserved. The documentation,
branding, and other materials in this repository are not open source. See
[LICENSE](./LICENSE).
