# Building the page

## What a page is
A private web page published from this session. It can hold state, so button presses and notes survive, and they can be read back later. The operator opens a link, presses buttons, and never retypes anything in chat.

## Declare it with storage and identity
Publish with the `db` capability (so presses persist) and `user` (so a press is attributed). Load the `artifact-capabilities` skill before writing the page — it carries the exact call shapes.

**If the capabilities skill or the page tool is not available on this machine**, do not guess at the API. Write a self-contained HTML file into the current folder instead, tell them the path, and put the same three lines in chat. A local file that opens is worth more than a broken link.

## Putting a real screenshot in the page
A drawing of a screen is second best. Put the real image in:

1. Take the screenshot through the browser and save it to a file.
2. Declare the `assets` capability on the page alongside `db` and `user`.
3. Upload the image to the page's own asset store, and reference it by the URL the upload returns, exactly as given. Load the `artifact-capabilities` skill for the exact calls before writing the page — do not guess at them.
4. Caption it with the address and the time of capture.

If uploads are unavailable on this machine, redraw the screen and label the frame **Vẽ lại từ ảnh chụp**, naming the address and time of the capture — state 2 in `honesty.md`. Never present a redrawing as the screenshot itself.

## Documents to write
- `previews/<ticket-or-slug>` — the chosen reading, the verdict, and any note.
- `queue/<row-id>` — one document per waiting row: verdict, who, when.
- `outbox/<surface>` — written when the operator presses **Gửi / Send**: `{status:"ready", items:[...], at:<time>}`.

## How answers come back
1. A press saves immediately to the page's own store.
2. **Gửi / Send** at the bottom sets `outbox/<surface>` to `ready` with a timestamp.
3. At the start of the next turn — and whenever `/brief` or `/needs-me` runs — read the outbox, act on it, and write your answer back onto the same row so the operator sees it on the page.

A page cannot start a session on its own. Something has to collect it, and that something is the next command anyone runs. Say so honestly if asked; never imply it is instant.

## Cost discipline
Write the page **once**. After that, write data into it — a few lines per update, not a new page. Never rebuild a page to change three numbers. Never build a page for a single number.

## Visual conventions
- **Before on the left, after on the right**, aligned row by row with the row label running across both, so the eye compares horizontally.
- Green for the after state, red for the current state, and those two colours for nothing else.
- Vietnamese as the primary label, English underneath in a smaller, quieter line.
- The room grid is drawn as a grid: rooms down, dates across, channel colour blocks in the cells, and a marked cell where the change lands.
- Every button says exactly what will happen. `Duyệt` produces a ticket; the page then says a ticket was produced.
- Buttons that are only illustrations of what an operator will see are drawn with a dashed outline and labelled as such, so nobody presses a picture.
- It must read on a phone: one column under about 860px, no sideways scrolling.
