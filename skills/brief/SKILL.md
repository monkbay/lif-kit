---
name: brief
description: Bản tin — 24 giờ qua xong gì, kẹt gì, cần bạn việc gì. Chỉ khi bạn gõ, không tự gửi. Use when someone asks what happened, what shipped, what is stuck, or to catch up after time away.
argument-hint: (để trống) hoặc khoảng thời gian, ví dụ "tuần này"
---

Window: $ARGUMENTS (default: the last 24 hours)

**First, load the `lif-kit:operator-kit` skill with the Skill tool**, and follow the Brief shape in its `references/templates.md`.

## Steps

1. **Preflight**, then pull **only the window**, never the whole board — ask for the date range and a sensible limit, and if the answer came back truncated say how many there were rather than implying you saw everything. Pull what **reached hotels** in the window, what **is waiting on a person**, and what **has not moved**. Group by product.
2. Write each line in what-a-person-sees language, not ticket titles. A ticket id goes in brackets at most.
3. Stuck items carry an owner and an age in days, measured from the last real status change rather than last-updated — a board that re-stamps tickets makes week-old blockages look fresh. Anything past 12 hours gets the stall treatment — one owner, one action, a default — and three days or more is called out plainly as rolling.
4. **Say how much is built and unchecked.** One line: how many items are finished but nobody has looked at them yet. This number grows silently and is the best early warning that the board has stopped meaning anything.
5. End with the single thing that needs this person today, pointing at `/needs-me`.
6. **Chat only.** Plain text, phone-readable, under about twenty lines, a bar of blocks for counts. Never build a page for this. Never send it on a schedule — it runs when someone types it.

## If something is missing
- **No board connection** → say so in the first line, name the one step to fix it, and report only what this conversation and the code can show. An empty brief is correct; an invented one is not.
- **Nothing shipped in the window** → say that plainly. Do not pad it.

## Non-negotiables (these hold even if nothing else loaded)
- Answer in the language they wrote in.
- Never ask a technical question — no file paths, no tables, no component names. Need a decision? Two options and a recommendation, in business words.
- Never invent a ticket, an id, a status, a date or a number. Missing something? Say so and name the one step to fix it.
- Never write "đã xong"/"done" without evidence you can show.
- Write to the board one ticket at a time, only what you were asked to write, and echo it back.
