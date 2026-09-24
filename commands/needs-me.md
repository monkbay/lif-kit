---
description: One list of everything waiting on this person, each row with a deadline and a default
argument-hint: (nothing) or a name to filter by
model: opus
---

Build the one queue of everything currently waiting on a human. Filter: $ARGUMENTS

Load the `operator-kit` skill and follow the Needs-me contract in `references/templates.md`.

1. **Collect** from the ticket board and from this project's open work, three kinds of row only:
   - **Duyệt** — a build waiting for someone to approve it
   - **Chọn** — a question with two possible answers, blocking work
   - **Gỡ kẹt** — something stalled on an action only a person can take (a login, a credential, an owner)
2. **Every row must carry**: what it changes in plain words, what it costs (size and credits, or "free — warranty"), who raised it, how long it has waited, and **a default that applies if nobody answers by a stated time**. A row without a default is not ready to show — work out the sensible default yourself and label it as yours.
3. **Rank** by what is blocking the most other work, not by age.
4. **Surface**: one waiting item → answer in chat. Two or more → build the page (`references/artifact-pattern.md`) with real buttons, and put the count plus the link in chat.
5. **Never press a button on a person's behalf.** A default applies only when its stated time has passed, and applying one is announced.
6. Accept short answers back: `1 duyệt`, `2 chọn b`, `3 gỡ kẹt: Gieng`. Act on them, then write what you did onto the same row.
