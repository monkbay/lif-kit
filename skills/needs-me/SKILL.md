---
name: needs-me
description: Cần bạn — một danh sách duy nhất mọi thứ đang chờ bạn quyết, mỗi dòng có hạn và có mặc định. Use when someone asks what needs them, what is waiting, what to approve, or what decisions are outstanding.
argument-hint: (để trống) hoặc tên người cần lọc
model: opus
---

Filter: $ARGUMENTS

**First, load the `lif-kit:operator-kit` skill with the Skill tool**, and follow the Needs-me shape in its `references/templates.md`.

## Steps

1. **Preflight** (from the operator-kit skill), then collect only three kinds of row:
   - **Duyệt** — a build waiting for a person to approve it
   - **Chọn** — a question with two possible answers, blocking work
   - **Gỡ kẹt** — stalled on something only a person can do (a login, a credential, an owner)
2. **Every row carries**: what it changes in plain words · what it costs (size and credits, or `miễn phí — bảo hành`) · who raised it · how long it has waited · **the default and the time it applies**. Work the default out yourself if none exists, and label it as yours.
3. **Rank by what is blocking the most other work**, not by age.
4. **Surface**: one item → answer in chat. Two or more → build the page with real buttons, and put the count plus the link in chat.
5. **Never press a button for a person.** A default applies only once its stated time has passed, and applying one is announced.
6. Accept short replies: `1 duyệt`, `2 chọn b`, `3 gỡ kẹt: Gieng`. Act, then write what you did onto that row.

## If something is missing
- **No board connection** → say `Chưa kết nối bảng nên chưa thấy được việc đang chờ`, name the one step to fix it, and list only what is waiting inside this conversation. Never invent rows.
- **No page tool** → answer in chat as a numbered list; they reply with the number.
