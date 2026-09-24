---
description: Find one thing by name, description or ticket id — where it stands and where it lives
argument-hint: a feature name, a description, or a ticket id
model: sonnet
---

Trace: $ARGUMENTS

Load the `operator-kit` skill.

1. **Match on anything.** A ticket id, a feature name, a screen name, or a loose description in Vietnamese or English. Search titles, descriptions and comments across every status, not only active lanes — nobody remembers ticket numbers. Several matches: list up to five with one line each and ask which. No match: say so and offer the closest two.
2. **Answer in chat, short**, with:
   - a timeline: raised → built → waiting since (dates, and how many days)
   - what it is waiting on, in one sentence
   - **one** named owner and **one** action, with a time estimate
   - a default if nobody acts, and what breaks if they do not
3. **If they asked about a screen rather than a ticket**, answer where it lives instead: the screen in staff words, the link, which hotels have it on, what it does, and the open tickets touching it.
4. **Never leave it at a status word.** "In review", "deployed" and "done" mean nothing on their own; say what a person would see.
5. Stay in chat. Only draw a page if they ask for the whole product map, or if the answer needs a picture of a screen.
