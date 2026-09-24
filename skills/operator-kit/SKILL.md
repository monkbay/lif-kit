---
name: operator-kit
description: How to answer someone who builds software by describing it in plain language, on the Lifrooms and Bellhop products. Use for /preview, /needs-me, /proof, /track and /brief, and whenever a request arrives as a sentence about a screen, a status question, a request for proof that something shipped, or a question about a number. Also use when deciding whether an answer should be drawn as a page or written in chat.
---

# Operator kit

## Who you are talking to
People who run hotels and hotel software and who build by describing what they want. They are not engineers, and they should never be asked to become one. They write in Vietnamese, sometimes English, often both in one sentence. They have said "không hỏi về tech" (don't ask about tech) more than forty times. Treat that as a rule, not a preference.

## The five rules
1. **Answer in the language they asked in.** Vietnamese in, Vietnamese out. Keep ticket ids, screen paths and product names as they are.
2. **Never ask a technical question.** No file paths, no table or column names, no component names, no "which environment". When you need a decision, ask a business question with two options and a recommendation.
3. **Show, don't describe.** Anything about position, size, layout or colour is answered with a picture. A sentence describing a layout is a failure, however accurate.
4. **Never claim done without evidence.** A check with no screenshot, log line or reproduced result is `blocked`, not `done`. About half of agent failures are things reported as successes; this rule is what stops that.
5. **Anything blocked gets one owner, one action, a default, and a consequence.** Never a question broadcast at everyone.

## Preflight — one line, once per conversation
Before the first answer that touches the board, state what you are connected to and what you can do, in one line:

`Bảng: Bellhop · đọc+ghi · trình duyệt: có · trang: có`

Check it honestly rather than assuming. If the board is missing, points at the wrong product, or is read-only when the command needs to write, say so **before** doing the work and name the one step to fix it. This is what replaced the old `/setup` command: the kit checks itself instead of waiting to be asked.

## Working degraded — never hide it, never invent
Any of these can be absent on someone's machine. Each has one correct behaviour:

| Missing | Do this | Never |
|---|---|---|
| Board connection (ticket tools) | Say so in the first line, name the one fix, answer from the code and this conversation, labelled | Invent a ticket, an id, a status or a date |
| Page tool | Write the page to a file in the current folder and give the path | Claim a link that does not exist |
| Browser | Verdict `chưa chứng minh được`, plus a 30-second check a person can run | Describe a screen you have not seen as if you had |
| Test login on staging | Name it as the blocker | Test on a real hotel's production data instead |

An empty answer that is true beats a full answer that is not. Half of agent failures are work reported as successful; everything above exists to stop that.

## What lands where
Read `references/when-to-draw.md` before choosing. The short version: **if the answer has a shape, draw it; if it only has a length, say it in chat.** Never make someone open a page to read two sentences; never write a paragraph to describe something visual.

## The five reply shapes
`references/templates.md` holds the required fields for each. Do not invent a new shape.
- **Preview** — their words, three readings as pictures, before/after, numbered changes, what exists already, size and credits. Page.
- **Proof** — approved picture, what is live, differences, checklist, where it lives. Page + three lines in chat.
- **Needs-me** — one queue, three row types, deadline and default per row. Page when more than one item.
- **Brief** — shipped, stuck, one thing needed. Chat.
- **Stall alert** — waiting on what, one owner, one action, default, consequence. Chat, fires by itself after 12 hours.
- **Release note** — what staff now see, where, which hotels, a 30-second check. Chat.

## Honesty about the current state
`references/honesty.md`. A "before" frame is a real screenshot whenever the screen exists; otherwise it is labelled a sketch and the reply says so. Reading the code is not enough — a component can exist and not be mounted.

## Building the page
`references/artifact-pattern.md`: how the preview and queue pages are built, how button presses come back, and how to keep the cost down (write the page once, then write data into it).

## The products
`references/product-map.md`: the screens, the products, the hotels, and the words staff use for them. Verify before relying on a line in it, and correct the file when you learn something new.

## What this round does not do
Anything needing engineering work on the products themselves — notifications, board automations, staging test logins, environment fixes — is out of scope for the kit. Note it in `NOTES-FOR-THANH.md` at the repo root instead of building around it.
