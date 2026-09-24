---
name: brief
description: Bản tin — 24 giờ qua xong gì, kẹt gì, cần bạn việc gì. Chỉ khi bạn gõ, không tự gửi. Use when someone asks what happened, what shipped, what is stuck, or to catch up after time away.
argument-hint: (để trống) hoặc khoảng thời gian, ví dụ "tuần này"
model: sonnet
---

Window: $ARGUMENTS (default: the last 24 hours)

**First, load the `lif-kit:operator-kit` skill with the Skill tool**, and follow the Brief shape in its `references/templates.md`.

## Steps

1. **Preflight**, then pull what **reached hotels** in the window, what **is waiting on a person**, and what **has not moved**. Group by product.
2. Write each line in what-a-person-sees language, not ticket titles. A ticket id goes in brackets at most.
3. Stuck items carry an owner and an age in days. Three days or more is called out as such.
4. End with the single thing that needs this person today, pointing at `/needs-me`.
5. **Chat only.** Plain text, phone-readable, under about twenty lines, a bar of blocks for counts. Never build a page for this. Never send it on a schedule — it runs when someone types it.

## If something is missing
- **No board connection** → say so in the first line, name the one step to fix it, and report only what this conversation and the code can show. An empty brief is correct; an invented one is not.
- **Nothing shipped in the window** → say that plainly. Do not pad it.
