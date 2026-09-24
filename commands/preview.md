---
description: Show a change as a picture before anything is built, then file the ticket
argument-hint: what you want, in your own words (attach a screenshot if it is about a screen)
model: opus
---

The operator wants something changed or has found something broken. They wrote:

$ARGUMENTS

Load the `operator-kit` skill and follow the Preview contract in `references/templates.md`. Work in the language they used.

Do this in order:

1. **Do not ask a technical question.** No file paths, no tables, no component names, no "which environment". If you need to know something, ask a business question with two options and a recommendation.
2. **Decide what kind of request this is.** If the screen already exists and misbehaves, it is a bug (warranty, not billed) — say so plainly. Otherwise it is a change or a new thing. Never make the operator classify it.
3. **Read the current state before drawing it.** Search the codebase for the screen, and when a screen exists take a real screenshot through the browser (see `references/honesty.md`). If you could not capture it, label the frame `sketch — chưa kiểm chứng / not verified` and say why. Never draw a screen from code and present it as what is live.
4. **Check what already exists.** Search the ticket board for the same request; if it is already there, reuse that ticket and say so. Never open a duplicate.
5. **Offer three readings of what they said**, each as a small picture, with one marked as your recommendation. Spatial words ("sang phải", "chật", "to hơn") are always answered with a picture, never a sentence.
6. **Build the preview page** following `references/artifact-pattern.md`: environment strip, their words quoted, the three readings, before/after of the real screen, numbered changes, what already exists, size and credits, and the operator's buttons (Duyệt · Sửa #n · Tách nhỏ).
7. **In chat, three lines only**: what you understood, the recommended reading, the link. Nothing else.
8. **Wait.** File the ticket only after they choose, and attach the approved picture to it. If the request is too big for one ticket, propose the split and ask one yes/no question.

If anything blocks you, stop and write the stall note from `references/templates.md` instead of guessing.
