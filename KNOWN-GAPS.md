# Known gaps — what the kit cannot fix from the outside
None of these block the kit. Each one makes it better, and each needs work on the product rather than on the kit.

1. **A test login on staging, per product.** `/proof` opens the real screen. Without a stable test account it falls back to "not proven". This is the highest-value item by a distance.
2. **Notify the person who raised a ticket when it changes state.** The kit answers when asked; it cannot push. Until then nobody learns something is live without running `/brief`.
3. **One environment label on every ticket** — staging or production, and which customers have the feature switched on. The kit infers this today and sometimes cannot.
4. **Quieten duplicate bot posts.** The kit reduces what a person must read; it cannot silence the source.
5. **A parent link on every bug.** With it, warranty versus billable is automatic instead of presumed.
6. **Split long agent replies.** Replies that hit the model's answer-length cap fail silently and get retried by hand.
7. **A health check on the release pipeline.** The kit reports what it can see; it cannot watch a deploy job.
8. **A browser screenshot cannot be placed in a page as an image.** The capture reaches the agent as an image in the conversation, not as a file, so every "before" frame is a 1:1 redraw labelled with the address and capture time. Honest, and enough in practice. A pixel-exact frame would need a headless browser writing a real file, with its own logged-in session.
