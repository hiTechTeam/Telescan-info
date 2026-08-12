# Known Issues

**Last reviewed:** August 12, 2026

## BLE reliability on newer iPhone models

Some tests have shown intermittent discovery or advertising on iPhone 17, iPhone Air, and iPhone 17 Pro devices. Symptoms include nearby users appearing late, disappearing unexpectedly, or not being discovered.

Apple documented an iOS 26.0.1 issue in which Wi-Fi and Bluetooth could occasionally disconnect on these models. This supports a possible system-level factor, but it does not establish the cause of every CoreBluetooth or Telescan failure. See [About iOS 26 Updates](https://support.apple.com/123075).

Before reporting a problem:

1. Install the latest available iOS and Telescan versions.
2. Confirm Bluetooth permission and restart Bluetooth or the device.
3. Test with two physical devices at close range; the iOS Simulator cannot test BLE discovery.
4. Record both device models, iOS versions, app version, and whether scanning or advertising failed.

Report reproducible Telescan problems in the relevant repository. For suspected iOS defects, also use Apple Feedback Assistant.
