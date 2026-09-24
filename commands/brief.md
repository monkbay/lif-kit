---
description: The last 24 hours in one message — shipped, stuck, and the one thing that needs you
argument-hint: (nothing) or a window like "tuần này" / "this week"
model: sonnet
---

Window: $ARGUMENTS (default: the last 24 hours)

Load the `operator-kit` skill and follow the Brief contract in `references/templates.md`.

1. Pull from the ticket board what **reached hotels** in the window, what **is waiting on a person**, and what **has not moved**. Group by product (Bellhop, Lifrooms).
2. Write each line in what-a-person-sees language, not ticket titles. A ticket id belongs in brackets at most.
3. Stuck items carry an owner and an age in days. Anything stuck three days or more is called out as such.
4. End with the single thing that needs this person today, and point at `/needs-me`.
5. **Chat only.** Plain text, phone-readable, under about twenty lines, a simple bar of blocks for counts. Never build a page for this, and never send it on a schedule — it runs when someone types it.
