# Changelog

Every release bumps the version, because the plugin cache is keyed by it: without a bump, `/plugin update` reports success and keeps serving the old copy. An update only takes effect in a new session — restart after updating.

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
