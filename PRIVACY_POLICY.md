# Telescan Privacy Policy

**Public page:** [tgtelescan.ru/privacy](https://tgtelescan.ru/privacy)

**Effective date:** September 1, 2026

Telescan is an iOS app for discovering nearby users and opening the public
Telegram profiles they choose to share. This policy explains the information
processed by the Telescan app, Telegram bots, API, and supporting service
providers. Use of Telescan is also governed by the [Terms of
Service](./TERMS_OF_SERVICE.md).

## Data we process

### Apple account information

When you use Sign in with Apple, Telescan receives a stable Apple account
identifier. If you choose to share them, Telescan may also receive your name
and email address or Apple private-relay email. Apple authenticates the primary
Telescan account.

### Telegram profile information

When you request a linking code through the Telescan Telegram bot, Telescan may
receive your Telegram numeric ID, first name, username, and current public
profile photo. This information is used to create or refresh the Telescan
profile you choose to share.

Telescan does not receive your Telegram password and does not read Telegram
messages or contacts.

### Telescan account and session information

Telescan creates a random public Telescan ID and device-session records needed
to keep each signed-in installation authenticated. Linking codes are temporary,
single-use values. The iOS app stores session credentials in the system
Keychain.

### Profile photos

You may use the current public Telegram photo or select another image through
the iOS camera or system photo picker. Telescan accesses only the selected image,
prepares it on the device, and uploads a copy for profile display. Replacing or
removing the photo removes the obsolete live profile copy according to the
service workflow.

### Nearby discovery

While discoverability is enabled, the app broadcasts your random Telescan ID
over Bluetooth Low Energy. Nearby Telescan devices may use that identifier to
request the profile you share.

Bluetooth signal strength, approximate distance, and the nearby-device list are
processed on the device. Telescan does not send those measurements to the
server. Radio identifiers may still be observed or replayed by devices within
range, and Bluetooth must not be treated as precise proof of identity or
location.

After a complete profile leaves the nearby list, the app may keep its public
profile snapshot and last-seen time in a **Met** history on the current device.
This history contains no GPS location or distance measurements, is not uploaded
to Telescan servers, and is automatically removed after 24 hours. You can clear
it earlier; it is also cleared on sign-out or account deletion. Blocking a
profile removes it from this local history.

When you save another profile, the app keeps that public profile snapshot in a
**Saved** list only on the current device. Saved profiles are not uploaded or
synchronized between devices. They remain until you remove them, sign out, or
delete the account from the device.

### Reports, blocks, and moderation

When you report a profile, Telescan processes identifiers for the reporting and
reported accounts, an optional comment, relevant profile context, timestamps,
review status, and moderation audit information. The current product submits
one universal report rather than asking you to select a category. The reported
user is not shown the reporter's identity through the product.

When you block a profile, Telescan stores the relationship and enough profile
context to display and manage the block. Blocking hides profile access in both
directions until it is removed. Block identifiers may be cached on the device
so blocked profiles remain hidden during a network outage.

### Operational request information

Service providers may process IP address, time, requested host and path,
response status, user agent, and performance or forwarding metadata needed to
deliver, protect, troubleshoot, and maintain Telescan. This information is not
used for advertising or behavioral profiling.

## Data we do not collect

Telescan does not request or intentionally store:

- GPS location or server-side movement history;
- Telegram messages, contacts, or password;
- advertising identifiers;
- precise Bluetooth-distance history on the server;
- third-party advertising or behavioral analytics data.

## How data is used

Data is processed to:

- create, authenticate, and maintain your Telescan account;
- show the profile you choose to share to nearby authenticated users;
- operate Bluetooth discovery and load complete profiles;
- maintain the device-local Met and Saved lists you choose to use;
- manage profile photos, device sessions, reports, and blocks;
- review possible abuse and protect users and the service;
- provide support, diagnose failures, and maintain availability;
- comply with applicable legal obligations.

Telescan does not sell personal data.

## Sharing and service providers

Information may be disclosed:

- to authenticated Telescan users who receive or already know your public
  Telescan ID;
- to Telegram and Apple as required by the features and platforms you use;
- to hosting, network, storage, backup, and other infrastructure providers
  necessary to operate the service;
- to authorized moderators who need report information to review possible abuse;
- when required by applicable law or a valid legal request.

Service providers may process information in Russia, the European Economic Area,
and other jurisdictions in which Telegram, Apple, or Telescan providers operate.
Data-protection rules may differ between jurisdictions.

## Security and retention

Telescan uses encrypted network transport, temporary linking codes, per-device
sessions, system Keychain storage, restricted service access, and operational
security measures. No system can guarantee absolute security.

The live account record and current profile photo remain while your Telescan
account is active. Linking codes and sessions have limited lifetimes. Blocks
remain until removed or account deletion. Pending reports remain while they are
reviewed; resolved or dismissed reports are scheduled for deletion after 180
days. Operational records are retained only for periods reasonably required for
security, reliability, abuse prevention, and legal obligations.

Device-local Met entries are removed after 24 hours. Device-local Saved entries
remain until you remove them, sign out, or delete the account on that device.

## Account and data deletion

Open your profile in the app, choose **Delete account**, and confirm. Telescan
revokes active sessions and removes the live account, linking codes, stored
profile photos, blocks, and local account data and caches. Direct report
relations are removed; limited report snapshots may remain for the moderation
retention period.

Deletion cannot be undone and does not delete or modify your Telegram account.

## Your choices and rights

You can:

- disable discoverability;
- clear the device-local 24-hour encounter history;
- save or remove public profile snapshots on the current device;
- replace or remove your shared photo;
- report, block, or unblock profiles;
- sign out the current device;
- delete your Telescan account and its sessions.

Depending on applicable law, you may also have rights to request access,
correction, deletion, restriction, or objection regarding personal data.

## Children

Telescan is not intended for children under 13. A higher minimum age may apply
where required by local law or platform rules.

## Changes and contact

This policy may be updated when the service or legal requirements change. The
effective date identifies the current version.

Privacy questions and requests: [admin@tgtelescan.ru](mailto:admin@tgtelescan.ru).
