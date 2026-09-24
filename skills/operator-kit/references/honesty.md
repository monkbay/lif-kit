# Proving the current state

## Before you draw a "before"
1. Find the screen in the codebase to learn its route and what it is supposed to render.
2. Open it in the browser (the Claude Code Browser pane), sign in if needed, and take a screenshot. Read the accessibility tree or page text rather than screenshotting repeatedly — it is cheaper and more exact — and take the picture for layout, colour and images.
3. Check the console and network panels while you are there. An error on load is part of the current state.

## If you could not capture it
Label the frame **`sketch — chưa kiểm chứng / not verified`**, say in one line why (no login, screen behind a flag, not deployed), and name the one thing that would let you verify it. Never quietly present a drawing as the live screen.

## Why reading the code is not enough
A component can exist, compile, and never be mounted on the page. A flag can be off. Staging can be stale. A page can render a placeholder. Each of these has happened on these products, and each looked like working code.

## Verdict words
- **Proven** — you saw it, and the evidence is attached.
- **Chưa chứng minh được / not proven** — you could not see it. Say what is needed.
- Never **done** or **deployed** without evidence attached.
