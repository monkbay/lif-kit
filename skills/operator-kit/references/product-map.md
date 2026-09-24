# The products, screens and words
**Seed file — verify a line before relying on it, and correct it here when you learn something new.** Last touched 2026-09-24.

## Bellhop — hotel PMS + channel manager
First real hotels going live. Two halves that staff treat as separate products:
- **PMS** — what front desk uses. Known screen: room map, `/pms/room-map`, staff call it **Sơ đồ phòng**. Cash fund ("Quỹ tiền mặt"). Per-hotel permissions.
- **CMS / Extranet** — what a hotel's own manager uses, also sold whitelabel.
- **Channel manager** — Channex, Hotel Link and OTA connections. Anything touching these is an integration, and it depends on someone else's API and credentials.

## Lifrooms — revenue management, live
Reporting and pricing for hotel groups. Numbers are the product here, so every figure needs its definition and its source. RevPAR has been reported wrong more than once; never print a metric without saying how it was calculated and which hotels are included.

## Hotels seen in the boards
Smoke Test (the safe one to demonstrate on), Hidden Green, Daiga Home. A feature is often on for some and off for others — always say which.

## Words staff use
| They say | It means |
|---|---|
| Sơ đồ phòng | the room map grid |
| Lễ tân | front desk |
| Quỹ tiền mặt | cash fund |
| Khách sạn (KS) | hotel |
| Đã lên / lên production | it reached real hotels |
| Duyệt | approve |
| Kẹt | stuck |
| Chưa thấy UI | I cannot see it on the screen |

## Never put in output
Hotel guest names, credentials, keys, or anything from a private message. If a request contains one, work without it and say what you left out.
