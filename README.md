# Telescan

[![Swift](https://img.shields.io/badge/Swift-5.0-orange.svg)](https://swift.org)
[![iOS](https://img.shields.io/badge/iOS-17.6+-blue.svg)](https://developer.apple.com/ios/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

![About Telescan](./docs/images/slide1.png)

Telescan is a social radar for discovering people nearby. It uses Bluetooth Low Energy (BLE) to detect other Telescan users without collecting GPS coordinates or sending proximity measurements to the server.

Telescan works as an extension of Telegram. A user links a Telegram profile through the Telescan bot, chooses when to become discoverable, and can open a nearby person's public profile directly in Telegram. BLE discovery works locally; profile loading, photo management, and account deletion require an internet connection.

## How it works

1. Get an authentication code from [@tgtelescan_bot](https://t.me/tgtelescan_bot) and enter it in the iOS app.
2. Enable discovery to advertise your Telegram ID and detect nearby Telescan users over BLE.
3. Select a person to view their shared profile and open it in Telegram.

![Data transmitted between nearby devices](./docs/images/slide2.png)

## Ecosystem

| Project                                                            | Purpose                           |
| ------------------------------------------------------------------ | --------------------------------- |
| [Telescan-iOS](https://github.com/hiTechTeam/Telescan-iOS)         | iOS application and BLE discovery |
| [Telescan-bot-app](https://github.com/hiTechTeam/Telescan-bot-app) | Telegram registration bot         |
| [Telescan-api](https://github.com/hiTechTeam/Telescan-api)         | Profile and account API           |
| [Telescan-nginx](https://github.com/hiTechTeam/Telescan-nginx)     | Reverse proxy                     |
| [Telescan-db](https://github.com/hiTechTeam/Telescan-db)           | Database configuration            |

Android support is planned. Platform-specific setup and development instructions live in the corresponding repository.

## Privacy

Telescan does not collect location, contacts, analytics, or advertising identifiers. BLE signal strength and approximate distance are processed locally on the device. The service stores the Telegram ID, display name, username, profile photo, and hashed authentication code required to provide the shared profile.

Users control when they are discoverable and can permanently delete their Telescan account and associated data from the profile screen in the app. Deleting a Telescan account does not delete or modify the connected Telegram account.

## Documentation

- [Whitepaper](./WHITEPAPER.md) — product and technical design
- [Privacy Policy](https://tgtelescan.ru/privacy) — collected data, retention, and deletion
- [Terms of Service](https://tgtelescan.ru/terms) — rules for using Telescan
- [Security Policy](./SECURITY.md) — security practices and vulnerability reporting
- [Roadmap](./ROADMAP.md) — planned development
- [Known Issues](./KNOWN_ISSUES.md) — current limitations and troubleshooting

![Telescan logos](./docs/images/logos.png)

## License and contact

Telescan is available under the [MIT License](./LICENSE).
Contact [r66cha](https://github.com/r66cha) via [Telegram](https://t.me/ruslanrocketman1) or [email](mailto:r66cha@gmail.com).
