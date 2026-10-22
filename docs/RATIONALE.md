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

---

## RD-003: Spike SP-01, a Notifier interface for complete_task()

**Date:** 2026-10-22
**Decided by:** Development Team, agreed with the PO and the Scrum Master

**Context (the design smell):**
In the baseline code `TaskManager.complete_task()` did three jobs: it marked the task as done, it printed a `[LOG]` line and it printed an `[EMAIL]` line. The two prints were hard-coded inside the method.
- **Rigidity:** to add push notifications (US-04) we would have to open and change `complete_task()` again, and again for SMS or anything else later. A small new feature forces a change in a class that shouldn't care how the user is told.
- **Fragility:** every edit to that method could break the log or the email that already work. The 3 baseline tests didn't check the printed output at all, so we wouldn't even notice.
- `TaskManager` also changed the task's state directly (`task.completed = True`), so the rule of what "complete" means was outside the `Task` class.

**Options we looked at:**
1. Add a third `print` for push. It is the fastest, but it makes the smell worse.
2. A full event system with event names and subscribers. It is more flexible, but we don't need it now. It isn't the simplest thing that could possibly work.
3. A small `Notifier` interface with one method. **This is what we chose.**

**Decision:**
- `Notifier` is an abstract class with one method, `notify(task)`.
- `ConsoleLogNotifier` and `EmailNotifier` hold the old print lines, with exactly the same text.
- `TaskManager` gets its notifiers by constructor injection (`TaskManager([...])`), and more can be added later with `register_notifier()`.
- `complete_task()` marks the task as done and calls `_notify()`, a loop that calls `notify()` on every notifier. It doesn't know which channels exist.

This follows the Open-Closed Principle: `TaskManager` is open for extension (new `Notifier` classes) but closed for modification (we don't edit it for a new channel).

**Result:**
- 10 tests, all passing (`python -m unittest discover -s tests -v`).
- `test_new_push_notifier_plugs_in_without_changing_task_manager` writes a new `PushNotifier` only in the test file and plugs it in with `register_notifier()`. `TaskManager` was not touched.
- `test_old_log_and_email_output_is_preserved` checks that the output is exactly the old two lines. We also compared it with the baseline code from the SETUP commit, and it is identical.
- The spike gave us the data to estimate US-04 at about 5 points (see `docs/BACKLOG.md`).

**Trade-off:**
`TaskManager()` with no notifiers now prints nothing. The code that creates it has to pass `ConsoleLogNotifier()` and `EmailNotifier()` to get the old behaviour. Right now only the tests create a `TaskManager`, so this is fine. When we add a main program, it will set up the notifiers in one place.

**Boy Scout clean-up (same commit):**
- `Task.mark_complete()` now changes the task's state. It is idempotent: calling it twice is safe and the task stays done.
- New `TaskNotFoundError` and `get_task()`. An unknown id gives a clear message instead of a bare `KeyError`. It is still a subclass of `KeyError`, so old code that catches `KeyError` keeps working.
- A task with an empty title (or only spaces) is rejected with a `ValueError`.
- Type hints on every method.
- Docstrings on every class and public method.
- `tasks` and `next_id` are now private (`_tasks`, `_next_id`). Other code uses `list_tasks()` and `get_task()`.
- f-strings instead of joining strings with `+`.
