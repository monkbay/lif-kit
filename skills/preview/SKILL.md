---
name: preview
description: Xem trước — thấy ảnh của thứ bạn muốn trước khi ai đó xây, rồi mới tạo ticket. Also how a bug is reported. Use when someone describes a change to a screen, something that looks wrong, or something they want added.
argument-hint: bạn muốn gì, nói bằng lời của bạn (kèm ảnh chụp màn hình nếu là về giao diện)
---

The operator wrote:

$ARGUMENTS

**First, load the `lif-kit:operator-kit` skill with the Skill tool.** It carries the rules, the reply shapes and the references named below. Work in the language they wrote in.

## Steps

1. **Run the preflight** from the operator-kit skill. One line, then continue.
2. **Never ask a technical question.** No file paths, no tables, no component names, no "which environment". If you need a decision, ask a business question with two options and a recommendation.
3. **Decide the kind.** Screen exists and misbehaves → a bug, under warranty, say so. Otherwise a change or a new thing. Never make the operator classify it.
4. **Establish the current state before drawing it.** Find the screen in the code, then capture it for real — see `references/honesty.md` in the operator-kit skill. If you could not capture it, label the frame `sketch — chưa kiểm chứng` and say why in one line.
5. **Check for a duplicate** on the board before creating anything. If the request already exists, reuse that ticket and say so.
6. **If they attached a picture**, it is the specification. Read it, build what it shows — colours, spacing and wording included — and say in one line what you took from it. Never substitute your own design taste, and never quietly change a detail you think is wrong: name it instead.

7. **If they said it is urgent** (`gấp`, `urgent`, `critical`), say which of the two urgent slots it takes and what it pushes behind. Two at a time per product is the cap. Without a cap everything becomes urgent, which is how the word stopped meaning anything here.

8. **Three readings** of what they said, each a small picture, one marked `đề xuất`. Spatial words are always answered with a picture, never a sentence.
9. **Build the page** per `references/artifact-pattern.md`: environment strip · their words · three readings · before/after · numbered changes · what already exists · size · the operator buttons (see step 11 for which ones).
10. **Three lines in chat**: what you understood, the recommended reading, the link. Nothing more.
11. **Wait for their choice, then take the lane that fits the size.** Small things must not be slowed down; big things must not be waved through.

   **Nhanh · Fast lane — micro and small**, one screen, easily undone. The button reads `✓ Duyệt · tạo luôn`. On approval, file the ticket straight away with the approved picture attached, and reply in one line: what was created, its id, and its size. No second question. Most requests live here, and stopping them for a confirmation is the kind of friction that made people stop using the old flow.

   **Kỹ · Careful lane — medium, large and XL**, or anything that touches an integration, permissions, money, more than one hotel, or data that cannot be put back. The button reads `✓ Duyệt · xem ticket trước`. On approval, show the draft ticket before creating anything: what will be built in plain words · what it touches, named · the acceptance checks someone will test against · what happens to hotels that are already live · the split, if it should be more than one ticket. Then one confirmation creates it. If it should be split, say so here rather than letting a too-big ticket bounce back later.

   State which lane you are in when you show the preview, so nobody is surprised by what the button does. When a request sits on the line, say why you put it where you did in half a line — and when in doubt on something irreversible, take the careful lane.

## If something is missing
- **No page tool available** → write the page to a file in the current folder and give them the path, plus the same three lines in chat. Never claim a link exists.
- **No browser, or the screen will not open** → continue with a labelled sketch and name the one thing that would let you verify it.
- **Size, not money** → state the size (micro · small · medium · large · XL) and stop. No credit figures, no price, no what-it-is-worth. Cost questions go to Kien.
- **No board connection** → build the preview anyway, and end with: `Chưa tạo được ticket — chưa kết nối bảng. Bạn duyệt trước, mình tạo sau.` Never invent a ticket id.

## Non-negotiables (these hold even if nothing else loaded)
- Answer in the language they wrote in.
- Never ask a technical question — no file paths, no tables, no component names. Need a decision? Two options and a recommendation, in business words.
- Never invent a ticket, an id, a status, a date or a number. Missing something? Say so and name the one step to fix it.
- Never write "đã xong"/"done" without evidence you can show.
- Write to the board one ticket at a time, only what you were asked to write, and echo it back.
