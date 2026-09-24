---
name: track
description: Theo dõi — gõ tên tính năng hoặc mô tả, không cần nhớ mã ticket. Nó đang ở đâu, chờ gì, và màn hình nằm ở đâu. Use when someone asks where something is, what is blocking it, what its status is, or which screen a feature lives on.
argument-hint: tên tính năng, mô tả, hoặc mã ticket
model: sonnet
---

Trace: $ARGUMENTS

**First, load the `lif-kit:operator-kit` skill with the Skill tool.**

## Steps

1. **Match on anything** — a ticket id, a feature name, a screen name, or a loose description in Vietnamese or English. Search titles, descriptions and comments across **every** status, not only active lanes; nobody remembers ticket numbers. Several matches: list up to five, one line each, ask which. No match: say so and offer the closest two.
2. **Answer in chat, short**:
   - a timeline — raised → built → waiting since, with dates and days
   - what it is waiting on, in one sentence
   - **one** named owner and **one** action, with a time estimate
   - the default if nobody acts, and what breaks if they do not
3. **Asked about a screen rather than a ticket?** Answer where it lives instead: the screen in staff words · the link · which hotels have it on · what it does · the open tickets touching it.
4. **Never leave it at a status word.** `In review`, `deployed` and `done` mean nothing on their own — say what a person would see.
5. Stay in chat. Draw only if they ask for the whole product map, or the answer needs a picture of a screen.

## If something is missing
- **No board connection** → say `Chưa kết nối bảng`, name the one step to fix it, and answer from the code and this conversation only, labelled as such. Never invent a ticket, a status, or a date.
