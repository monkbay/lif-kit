# Changelog

Every release bumps the version, because the plugin cache is keyed by it: without a bump, `/plugin update` reports success and keeps serving the old copy. An update only takes effect in a new session — restart after updating.

## 0.5.0 — 2026-09-24
- `/needs-me` gains a fourth row type: **Kiểm tra** — built and waiting for a person to check it on screen. Finished but unverified work is not done, and a pile of it looks like progress while none of it has been seen. Grouped with a count past three, ranked by what reaches real users first.
- `/brief` states how many items are built and unchecked.
- The preview page ships as a template, `references/preview-page.html`, rather than being rebuilt from a written description each time — same palette, same structure, same labels for every operator.

## 0.4.1 — 2026-09-24
- The 1:1 redraw is named as the normal route for a "before" frame, because a browser screenshot arrives as an image in the conversation and not as a file that can be uploaded. The kit no longer spends a cycle attempting an upload that cannot complete; the upload route applies only when a real image file exists.

## 0.4.0 — 2026-09-24
Found by a live run of all five commands against the Kaydo board and product.
- A frame now has **three** honest states, not two: the real screenshot, redrawn from a screenshot you took (address and time named), or a sketch you never verified. A redrawing is not a sketch.
- `artifact-pattern.md` says how a real screenshot gets into the page — uploaded to the page's asset store and referenced by the URL returned — so the capture taken during `/preview` has somewhere to go.
- Ages and stalls are measured from when work was raised and when its status last really changed, never from last-updated. A board that re-stamps its tickets on a timer was making week-old blockages look fresh, which silently defeated the stall sweep.
- The preflight line is written in the reader's language, not always Vietnamese.

## 0.3.0 — 2026-09-24
- `product-map` states plainly that it applies to Lifrooms and Bellhop only, so the kit carries no hotel assumptions into another product.
- `/brief` asks the board for a window rather than everything, and says when a result was truncated.
- `/needs-me` caps at ten and names a long queue as the problem itself.
- `/preview` leaves the preview and stops in an unattended run instead of waiting or deciding for someone.
- Added `scripts/check.py` — release invariants, run it before every release.

## 0.2.0 — 2026-09-24
- Trivial, unambiguous requests (a typo, exact wording, a colour given) get one line and a fast-lane ticket. The full three-reading preview is reserved for requests that could be read more than one way.
- Stand-down rules: the kit stays out of engineering work, deliberate technical questions, and repos whose own `CLAUDE.md` covers the work — those always win.
- Size only. No credits, no prices, anywhere operator-facing.
- Two approval lanes on `/preview`: small work files on approval; medium and up, or anything irreversible, shows the draft ticket and its acceptance checks first.

## 0.1.0 — 2026-09-24
- Five commands — `/preview`, `/needs-me`, `/proof`, `/track`, `/brief` — and the `operator-kit` skill behind them.
- Preflight, degraded-mode behaviour, and four hard limits: credentials, money, acting for a person, and bulk writes to the board.
