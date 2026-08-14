# Known Issues

**Last reviewed:** August 14, 2026

## BLE discovery is not continuous in the background

iOS controls background scanning, advertising, restoration, and radio
scheduling. A nearby user may appear late, disappear, or require the app to be
foregrounded even when Telescan has configured CoreBluetooth restoration.

Test BLE only on physical devices. Confirm Bluetooth permission, keep both
devices close for the first discovery, and record device model, iOS version,
app version, and whether scanning or advertising failed when reporting an issue.

## Distance is an estimate

The displayed distance is derived from recent RSSI samples. Device orientation,
the human body, walls, interference, radio hardware, and iOS scheduling can
change RSSI substantially. Do not use the value for navigation, safety,
identity, or access-control decisions.

## BLE identity can be observed or replayed

The app broadcasts a random `telescan_id` instead of a Telegram ID, but that
UUID is stable for the lifetime of the Telescan account. Nearby hardware can
capture, correlate, or replay it. The current BLE protocol does not provide
cryptographic proof of identity or proximity.

## Profile lookup does not prove proximity

The profile endpoint requires an active Telescan session, but any authenticated
account that knows a valid `telescan_id` can request that shared profile. The
server does not receive BLE sightings and cannot verify that the requester is
actually nearby.

## Rate limiting is process-local

Current API throttling is stored in memory. It resets on restart and is not
shared between multiple API replicas. Do not horizontally scale the API without
a shared rate-limit adapter and an updated abuse model.

## Logout-all depends on Telegram

Signing out every device requires the API, bot, and Telegram delivery to be
available before the confirmation expires. If that path is unavailable, sign
out the current device separately and retry logout-all later. Account deletion
is a distinct authenticated API operation.

## A fresh iOS checkout needs local build settings

`Debug.xcconfig` and `Release.xcconfig` are intentionally ignored and excluded
from the app bundle. Set `API_ORIGIN`, `TELESCAN_BOT`, and optional `LOCALHOST`
values before building. Never add secrets or local `.xcconfig` files to Git.

## Legacy API is transitional

The old `/v1` contract is registered only when `ENABLE_LEGACY_API=true`. It is
less secure than the session-based API and must remain disabled except during a
controlled old-client migration. Removing legacy user hashes requires the
explicit guarded migration command documented in `Telescan-api`.
