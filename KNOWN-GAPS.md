# Known gaps — what the kit cannot fix from the outside
Written 2026-09-24. Nothing here blocks the kit shipping; each one makes it better.

1. **A staging test login per product.** `/proof` opens the real screen. Without a stable test account on staging it falls back to production or to "not proven". This is the single highest-value item.
2. **Notify the person who raised a ticket** when it changes state. The kit can only answer when asked; it cannot push. Until then, nobody learns something is live without typing `/brief`.
3. **One environment label on every ticket** — staging or production, and which hotels the flag is on for. The kit currently infers this and sometimes cannot.
4. **Stop double-posting from the bot.** Roughly 97% of two channels is machine noise; the kit reduces what people must read but cannot silence the source.
5. **A parent link on every bug.** With it, warranty versus billable is automatic instead of presumed.
6. **Answer-length failures.** The long "❌ Có lỗi xảy ra" replies were mostly the model hitting its answer-length cap while writing a full spec. Splitting long replies fixes it at the source.
7. **A health check on the release pipeline.** A promote job logged "ok" for eight days while broken. The kit reports what it sees; it cannot watch the pipeline.
