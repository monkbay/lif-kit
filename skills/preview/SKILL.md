---
name: preview
description: Xem trước — thấy ảnh của thứ bạn muốn trước khi ai đó xây, rồi mới tạo ticket. Also how a bug is reported. Use when someone describes a change to a screen, something that looks wrong, or something they want added.
argument-hint: bạn muốn gì, nói bằng lời của bạn (kèm ảnh chụp màn hình nếu là về giao diện)
model: opus
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
6. **Three readings** of what they said, each a small picture, one marked `đề xuất`. Spatial words are always answered with a picture, never a sentence.
7. **Build the page** per `references/artifact-pattern.md`: environment strip · their words · three readings · before/after · numbered changes · what already exists · size and credits · the operator buttons (`✓ Duyệt` · `✎ Sửa #n` · `Tách nhỏ`).
8. **Three lines in chat**: what you understood, the recommended reading, the link. Nothing more.
9. **Wait for their choice.** Only then file the ticket, with the approved picture attached. Too big for one ticket → propose the split, ask one yes/no.

## If something is missing
- **No page tool available** → write the page to a file in the current folder and give them the path, plus the same three lines in chat. Never claim a link exists.
- **No browser, or the screen will not open** → continue with a labelled sketch and name the one thing that would let you verify it.
- **No board connection** → build the preview anyway, and end with: `Chưa tạo được ticket — chưa kết nối bảng. Bạn duyệt trước, mình tạo sau.` Never invent a ticket id.
