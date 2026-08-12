# Telescan Roadmap

Telescan currently provides iOS-to-iOS BLE discovery, Telegram-based registration, shared profiles, approximate distance, profile-photo management, and in-app account deletion.

## Priorities

| Area | Direction | Status |
| --- | --- | --- |
| Security | Expiring credentials, authenticated profile changes, and API rate limiting | Planned |
| BLE | Improve background reliability and energy use within iOS constraints | Research |
| Protocol | Document and stabilize a cross-platform BLE protocol | Planned |
| Android | Build an interoperable Android client | Planned |
| Quality | Expand automated API, bot, BLE, and UI tests | In progress |
| Product | Publish a focused landing page and user documentation | Planned |

## Ideas under evaluation

Event-oriented discovery and temporary local interactions may be explored after the core protocol, privacy model, and authentication are stable.

Features that require encounter history, compatibility scoring, analytics, persistent chats, or AI recommendations are not part of the current privacy model. They would require a separate design review, explicit consent, retention controls, and updated documentation before development.

## Contributing

The most useful contributions are security review, testing on physical devices, BLE reliability research, Android protocol work, accessibility, design, and translation. Open an issue in the relevant repository before starting a large change.
