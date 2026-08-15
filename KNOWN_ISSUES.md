# Known Issues

**Last reviewed:** August 15, 2026

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

## Remote multi-device logout is not exposed in the iOS MVP

The current app can sign out its own device or delete the Telescan account.
Deleting the account revokes every session and removes owned server data without
changing the Telegram account. The API and bot retain the confirmed logout-all
contract, but iOS no longer polls it; a future UI depends on a reliable push
delivery design.

## A fresh iOS checkout needs local build settings

`Debug.xcconfig` and `Release.xcconfig` are intentionally ignored and excluded
from the app bundle. Set `API_ORIGIN`, `TELESCAN_BOT`, and optional `LOCALHOST`
values before building. Never add secrets or local `.xcconfig` files to Git.

## Legacy API is transitional

The old `/v1` contract is registered only when `ENABLE_LEGACY_API=true`. It is
less secure than the session-based API and must remain disabled except during a
controlled old-client migration. Removing legacy user hashes requires the
explicit guarded migration command documented in `Telescan-api`.
