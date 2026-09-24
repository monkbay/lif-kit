---
name: needs-me
description: Cần bạn — một danh sách duy nhất mọi thứ đang chờ bạn quyết, mỗi dòng có hạn và có mặc định. Use when someone asks what needs them, what is waiting, what to approve, or what decisions are outstanding.
argument-hint: (để trống) hoặc tên người cần lọc
---

Filter: $ARGUMENTS

**First, load the `lif-kit:operator-kit` skill with the Skill tool**, and follow the Needs-me shape in its `references/templates.md`.

## Steps

1. **Preflight** (from the operator-kit skill), then collect only three kinds of row:
   - **Duyệt** — a build waiting for a person to approve it
   - **Chọn** — a question with two possible answers, blocking work
   - **Gỡ kẹt** — stalled on something only a person can do (a login, a credential, an owner)
2. **Every row carries**: what it changes in plain words · what it costs (size and credits, or `miễn phí — bảo hành`) · who raised it · how long it has waited · **the default and the time it applies**. Work the default out yourself if none exists, and label it as yours.
3. **Rank by what is blocking the most other work**, not by age. Anything urgent sits at the top, and if more than two per product are marked urgent, say so — that is a queue problem, not a priority.
4. **Sweep for stalls while you are here**: anything that has not moved in 12 hours joins the list as a `Gỡ kẹt` row with its age. The kit cannot push a message on its own, so this sweep is how a stall reaches a person.
5. **Surface**: one item → answer in chat. Two or more → build the page with real buttons, and put the count plus the link in chat.
6. **Never press a button for a person.** A default applies only once its stated time has passed, and applying one is announced.
7. Accept short replies: `1 duyệt`, `2 chọn b`, `3 gỡ kẹt: Gieng`. Act, then write what you did onto that row.

## If something is missing
- **No board connection** → say `Chưa kết nối bảng nên chưa thấy được việc đang chờ`, name the one step to fix it, and list only what is waiting inside this conversation. Never invent rows.
- **No page tool** → answer in chat as a numbered list; they reply with the number.

## Non-negotiables (these hold even if nothing else loaded)
- Answer in the language they wrote in.
- Never ask a technical question — no file paths, no tables, no component names. Need a decision? Two options and a recommendation, in business words.
- Never invent a ticket, an id, a status, a date or a number. Missing something? Say so and name the one step to fix it.
- Never write "đã xong"/"done" without evidence you can show.
- Write to the board one ticket at a time, only what you were asked to write, and echo it back.
