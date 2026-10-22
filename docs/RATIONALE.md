# Rationale Document

Here we write down why we took our main decisions. The code tells us what the system does, but not why we built it this way. Every entry has an ID so we can link to it from the backlog, the code and the reflection.

---

## RD-001: A shared Definition of Done before any story

**Date:** 2026-10-22
**Decided by:** whole team (Adrian, Blagoy, Roberto)

**Context:**
AgileTask has no common idea of "done". One person could think done means "it runs on my laptop", another could think it means "tested and reviewed". With that gap the quality drops a bit every sprint, and nobody notices until the code is hard to change.

**Decision:**
We wrote a 5-item DoD in `docs/DOD.md` before the backlog. Three items are required by the activity: "All unit tests pass", "Code is refactored (Boy Scout Rule applied)" and "Rationale document updated". We added two more:
- "Acceptance criteria shown to the PO", because a story is only done when it does what the customer asked, not just when the code works.
- "Peer reviewed and merged", because a second pair of eyes finds problems early and more than one person knows each part of the code.

**Consequence:**
Each story takes a bit longer to finish, but we don't build up hidden work like missing tests or messy code. The DoD is the same for every story and every sprint, so it is our backstop against backsliding.
