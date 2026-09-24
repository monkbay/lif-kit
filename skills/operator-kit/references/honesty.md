# Proving the current state

## Before you draw a "before"
1. Find the screen in the codebase to learn its route and what it is supposed to render.
2. Open it in the browser (the Claude Code Browser pane), sign in if needed, and take a screenshot. Read the accessibility tree or page text rather than screenshotting repeatedly — it is cheaper and more exact — and take the picture for layout, colour and images.
3. Check the console and network panels while you are there. An error on load is part of the current state.

## Three states for a frame, not two
Label every "before" frame with exactly one of these, and never leave it unlabelled:

1. **Ảnh chụp thật** — the screenshot itself, shown in the page, with the address and the time it was taken. Always prefer this: upload the image to the page rather than redrawing it (see `artifact-pattern.md`).
2. **Vẽ lại từ ảnh chụp** — redrawn from a screenshot you really took, when the image itself could not be placed in the page. Name the address and the time of the capture on the frame, so the reader knows the drawing came from something real. This is honest, and it is the common case.
3. **Phác thảo — chưa kiểm chứng** — a sketch. You never saw the screen. Say in one line why, and what would let you verify it.

A redrawing is not a sketch, and a sketch is never presented as either of the first two.

## If you could not capture it
Label the frame **`sketch — chưa kiểm chứng / not verified`**, say in one line why (no login, screen behind a flag, not deployed), and name the one thing that would let you verify it. Never quietly present a drawing as the live screen.

## Why reading the code is not enough
A component can exist, compile, and never be mounted on the page. A flag can be off. Staging can be stale. A page can render a placeholder. Each of these has happened on these products, and each looked like working code.

## Ages and stall times
Never take "last updated" as "last moved". Boards re-stamp tickets for their own reasons — triage sweeps, automated relabelling, nightly jobs — and on at least one board this happens every ninety minutes, which makes a ticket stuck for a week look fresh. Work an age out from **when it was raised** and **when its status last genuinely changed**. If you can only see last-updated, say that is what you are using, and say it may be wrong.

## Verdict words
- **Proven** — you saw it, and the evidence is attached.
- **Chưa chứng minh được / not proven** — you could not see it. Say what is needed.
- Never **done** or **deployed** without evidence attached.
