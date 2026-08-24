# Telescan Security Policy

**Last reviewed: August 24, 2026.**

## Reporting a vulnerability

Please do not disclose a suspected vulnerability in a public GitHub issue,
Telegram discussion, review, or social-media post.

Send a private report to [admin@tgtelescan.ru](mailto:admin@tgtelescan.ru) with:

- the affected Telescan feature or public endpoint;
- a clear description of the problem and possible impact;
- reproducible steps or a minimal proof of concept;
- the device and iOS version when the issue affects the app;
- any suggested mitigation, if available.

Do not include real user data, credentials, private keys, or destructive test
results. Do not access another person's account, perform denial-of-service tests,
or retain data beyond what is necessary to demonstrate the issue.

Receipt will be acknowledged when practical. Telescan does not currently offer
a bug bounty or guarantee a response or remediation deadline.

## Supported version

Security fixes target the current production version of the iOS app and active
Telescan services. Older, modified, unofficial, or unsupported builds may not
receive fixes.

## Product security notes

- Telescan does not request GPS location, Telegram messages, or contacts.
- Nearby discovery uses Bluetooth radio data, which can be observed or replayed
  and is not proof of identity or precise physical proximity.
- Users should keep iOS updated, protect access to the linked Telegram account,
  and report unexpected account or profile behavior privately.
- The implementation and detailed infrastructure documentation are maintained
  in private repositories and are not part of this public repository.

General support and privacy questions may also be sent to
[admin@tgtelescan.ru](mailto:admin@tgtelescan.ru).
