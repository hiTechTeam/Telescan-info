# Security Policy

## Reporting a vulnerability

Please do not disclose security vulnerabilities in a public GitHub issue or discussion. Send a private report to [r66cha@gmail.com](mailto:r66cha@gmail.com) with:

- a clear description and affected component;
- reproducible steps or proof of concept;
- expected impact;
- suggested mitigation, if available.

We aim to acknowledge reports within 48 hours, investigate confirmed issues, provide progress updates, and coordinate disclosure after a fix is available. Timelines depend on severity and complexity.

Please avoid accessing data without permission, disrupting the service, degrading availability, or violating user privacy while testing. Researchers may be credited with their permission.

## Current security model

- API traffic is served over HTTPS and permits TLS 1.2 and TLS 1.3.
- The bot stores authentication codes as SHA-256 hashes; the iOS app hashes a code before sending it to the API.
- Account deletion verifies both the Telegram ID and authentication-code hash.
- Profile photos and account records are removed by the in-app deletion flow.
- BLE access requires iOS permission, and users explicitly control discoverability.
- The app contains no advertising or third-party analytics SDKs.

## BLE design

Telescan advertises a custom 128-bit BLE service UUID. The Telegram ID may be present in the advertisement local name; if it is unavailable there, another device can connect to the service and read the identity characteristic. Devices that have not been seen for 20 seconds are removed from the nearby list.

BLE advertisements are public to devices in radio range. A nearby observer can capture, replay, or manipulate identifiers and signal strength. RSSI is only an approximate distance signal and is not proof of physical proximity or identity.

## Known limitations

Telescan currently uses an eight-character code rather than an expiring session or access token. The original code is stored locally in iOS `UserDefaults`, and possession of it may allow account access until the code is updated.

Hashing protects the original code in server storage but does not by itself prevent replay. Public profile lookup uses a Telegram ID and does not require authentication. Some profile-photo operations also rely on Telegram ID without a separate authorization token. API-level rate limiting is not currently implemented.

These limitations mean Telescan should not be used to share sensitive or private information. Planned authentication hardening belongs in the [Roadmap](./ROADMAP.md).

## User guidance

- Enable discoverability only when you want to be visible nearby.
- Keep your authentication code private and update it through [@tgtelescan_bot](https://t.me/tgtelescan_bot) if it may be compromised.
- Keep iOS, Telescan, and Telegram updated.
- Avoid using the app on a jailbroken device.

Supported releases and fixes are tracked in the relevant component repositories. General security questions can be sent to [r66cha@gmail.com](mailto:r66cha@gmail.com).
