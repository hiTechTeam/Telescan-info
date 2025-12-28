## Known issues and device compatibility

### Bluetooth Low Energy (BLE) detection issues on iPhone 17 series (iOS 26.x)

**Device Affected**: iPhone 17, iPhone 17 Pro, iPhone 17 Pro Max, iPhone 17 Air.  
**iOS Versions**: iOS 26.0 - 26.2 (as of December 2025).

**Symptoms**:

- Nearby Telescan users are not detected during scanning.
- The device itself is not visible to other Telescan users (advertising is buggy or unstable).
- Works great on older models (iPhone 11, 14, iPad, etc.) with the same iOS version.

**Reason**:
This is a **known system level Bluetooth issue** in the iPhone 17 series due to the new **N1 Bluetooth/Wi-Fi chip** and bugs in iOS 26.x.  
Apple acknowledged similar Bluetooth connectivity issues (disconnects, audio stuttering, CarPlay issues) in the release notes for iOS 26.0.1 and later updates. Many users and developers are reporting issues specific to BLE (CoreBluetooth detection/advertising instability), especially in early builds of iOS 26.

This issue **doesn't** occur on older iPhone models running the same version of iOS.

**Current Status** (December 28, 2025):

- Partial fixes in iOS 26.0.1 and 26.1 resolve some outages, but **BLE detection remains unreliable** for many iOS 26.2 users.
- Developer reports highlight improvements in iOS 26.2 beta and the upcoming 26.3 (expected January-February 2026).

**Workarounds** (limited effectiveness):

- Reset network settings: “Settings” → “General” → “Transfer or reset iPhone” → “Reset” → “Reset network settings”.
- Reboot your device.
- Temporarily turn off nearby Apple Watches (they actively use BLE channels).
- Test older iPhone models for development.

**Recommendation**:
For reliable testing and use, use iPhone 14 or earlier models until Apple releases a full fix (likely iOS 26.3).

We monitor Apple updates and developer forums. This section will be updated when the issue is resolved.

If you encounter this issue, please report it through Apple Feedback Assistant to speed up the resolution.
