---
name: track
description: Theo dõi — gõ tên tính năng hoặc mô tả, không cần nhớ mã ticket. Nó đang ở đâu, chờ gì, và màn hình nằm ở đâu. Use when someone asks where something is, what is blocking it, what its status is, or which screen a feature lives on.
argument-hint: tên tính năng, mô tả, hoặc mã ticket
---

Trace: $ARGUMENTS

**First, load the `lif-kit:operator-kit` skill with the Skill tool.**

## Steps

0. **Decide what they asked about first.** A *screen* or an area of the product ("the onboarding screen", "sơ đồ phòng") is answered with where it lives — jump to step 3 and do not open with a list of tickets. A *thing being built* is answered with its timeline. If genuinely ambiguous, give the screen answer and add one line: the open tickets touching it.

1. **Match on anything** — a ticket id, a feature name, a screen name, or a loose description in Vietnamese or English. Search titles, descriptions and comments across **every** status, not only active lanes; nobody remembers ticket numbers. Rank by how well the words match what they asked, never by date — the newest ticket that merely mentions the word is rarely the one they mean. If the search was cut short, say how many matched and that you are showing the closest, never present a trimmed list as the whole truth. Drop nothing silently: tickets titled REVERT, REVERSED or superseded are shown as such, and never as the current state of a feature. Several real matches: list up to five, one line each, ask which. No match: say so and offer the closest two.
2. **Answer in chat, short**:
   - a timeline — raised → built → waiting since, with dates and days
   - what it is waiting on, in one sentence
   - **one** named owner and **one** action, with a time estimate
   - the default if nobody acts, and what breaks if they do not
3. **Asked about a screen rather than a ticket?** Answer where it lives instead: the screen in staff words · the link · which hotels have it on · what it does · the open tickets touching it.
4. **Never leave it at a status word.** `In review`, `deployed` and `done` mean nothing on their own — say what a person would see.
5. **Anything that has not moved in 12 hours gets the stall note** from the operator-kit templates, right here — one owner, one action, a default, a consequence. Nothing in this kit can push a message by itself, so a stall surfaces the moment someone runs a command.
6. Stay in chat. Draw only if they ask for the whole product map, or the answer needs a picture of a screen.

## If something is missing
- **No board connection** → say `Chưa kết nối bảng`, name the one step to fix it, and answer from the code and this conversation only, labelled as such. Never invent a ticket, a status, or a date.

## Non-negotiables (these hold even if nothing else loaded)
- Answer in the language they wrote in.
- Never ask a technical question — no file paths, no tables, no component names. Need a decision? Two options and a recommendation, in business words.
- Never invent a ticket, an id, a status, a date or a number. Missing something? Say so and name the one step to fix it.
- Never write "đã xong"/"done" without evidence you can show.
- Write to the board one ticket at a time, only what you were asked to write, and echo it back.
