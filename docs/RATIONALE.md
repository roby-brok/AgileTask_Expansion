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

---

## RD-002: Priority order of the backlog

**Date:** 2026-10-22
**Decided by:** Adrian (Product Owner), after the Planning Game with the team

**Context:**
We had three stories for the expansion: categories, due dates and filters. The PO orders them by value for the customer. The Developers estimated them, but the estimate is only one input for the PO, it doesn't decide the order alone.

**Decision:**
1. **US-01 Categorise tasks (3)** comes first. It gives the most value straight away, because users can finally organise a long list. It is also the base for US-03, which can't work without categories.
2. **US-02 Due date (2)** comes second. It is useful on its own and it is the smallest story, so it is a quick win. It doesn't depend on anything, so it can go in the same sprint as US-01 if there is space.
3. **US-03 Filter by category and status (5)** comes last. It gives a lot of value when the list is long, but it needs US-01 to be finished first, and it is the most complex story.

**Consequence:**
The first sprint can deliver US-01 and US-02 (5 points together), and US-03 follows when categories already work. If the customer changes their mind, the PO can reorder the backlog at the next Sprint Planning, because nothing is fixed yet.
