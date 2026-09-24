---
name: proof
description: Bằng chứng — ảnh thật của màn hình đang chạy so với ảnh đã duyệt, và xem ở đâu. Use when someone asks whether something is done, deployed, live, or says they cannot see it on the screen.
argument-hint: mã ticket, tên tính năng, hoặc mô tả
---

Prove the state of: $ARGUMENTS

**First, load the `lif-kit:operator-kit` skill with the Skill tool**, and follow the Proof shape in its `references/templates.md`.

## Steps

1. **Preflight**, then **find the thing** — by ticket id, feature name, or description. Several matches: list them and ask which. Never guess between two.
2. **Look at it for real.** Open the screen in the browser, sign in, walk the path a user would take, screenshot each step, and read the console and network panels. An error on load is part of the current state.
3. **Compare** live against the approved picture, point by point, using the numbered changes. State matches and differences separately — a difference is not a failure until a person says so.
4. **Re-check every acceptance line yourself.** One fails: fix it if it is yours to fix and say you did, or send it back with exactly what you saw. Never hand a failing check to the operator as a question.
5. **No evidence means blocked, not done.** Could not open it, could not sign in, flag off → the verdict is `chưa chứng minh được`, with the one thing needed to prove it. Never write `đã xong` or `deployed` on an unevidenced check. This is the most important rule in the kit.
6. **Always end with where it lives**: the screen in staff words · the link · hotels it is on and hotels it is not · a check anyone can do in 30 seconds.
7. **If the verdict is live, write the release note too** (shape 6 in the operator-kit templates): what staff now see, where, which hotels are on and off, the 30-second check. This is the answer to "will it tell us when it's live" — it comes out of `/proof`, not out of nowhere.
8. **Say who should be told, and draft it.** Name the person who raised it, write the message they could paste, and stop there. You never send it — they do.
9. **Surface**: the comparison on a page, three lines and the link in chat.

## If something is missing
- **No browser tool available** → do not guess. Verdict `chưa chứng minh được`, plus the 30-second check written so a person can do it in a minute, and say plainly that you could not open the screen yourself.
- **No test login** → same verdict, and name it as the blocker. Never test on a real hotel's production data to get around it.
- **No board connection** → still verify the screen, and say which ticket you could not read.

## Non-negotiables (these hold even if nothing else loaded)
- Answer in the language they wrote in.
- Never ask a technical question — no file paths, no tables, no component names. Need a decision? Two options and a recommendation, in business words.
- Never invent a ticket, an id, a status, a date or a number. Missing something? Say so and name the one step to fix it.
- Never write "đã xong"/"done" without evidence you can show.
- Write to the board one ticket at a time, only what you were asked to write, and echo it back.
