# AgileTask Expansion: Product Backlog

**Prioritised by:** Adrian (Product Owner), on business value
**Estimated by:** Development Team in the Planning Game, with Blagoy (Scrum Master) running the session
**Scale:** story points 1, 2, 3, 5, 8

The PO decides **what** is most important. The Developers decide **how much** each story costs. Story points measure complexity and risk compared with the other stories, not hours.

| Priority | ID | Story | Points |
|---|---|---|---|
| 1 | US-01 | Categorise tasks | 3 |
| 2 | US-02 | Set a due date on a task | 2 (reference) |
| 3 | US-03 | Filter tasks by category and status | 5 |
| 4 | SP-01 | **Technical Spike:** notification support | Timeboxed, 1 day (no points) |
| 5 | US-04 | Real-time task notifications | Not estimated yet (about 5 after SP-01) |
| | | **Total (estimated stories)** | **10** |

**Reference story:** US-02 (2 points). It is the smallest and clearest story, so we compared all the others with it. The reasons for the order are in `docs/RATIONALE.md` (RD-002).

US-04 is not in the total because it doesn't have a real estimate yet. We will confirm it in the next Planning Game.

---

## US-01: Categorise Tasks
**Story:** As a user, I want to give each task a category (Work, Personal or Study), so that I can organise my tasks by the different areas of my life.
**Estimate:** 3 Story Points.
**Justification:** It is bigger than US-02 because it adds a field with a fixed list of allowed values and an error case, but it only changes how a single task is created and edited.
**Acceptance Criteria:**
* When I create a task and choose Work, Personal or Study, I see the task in my list with that category.
* If I don't choose a category, the task is saved as "Uncategorised".
* If I try to use a category that is not in the list (for example "Holiday"), the task is not created and I see "Unknown category".
* I can change the category of a task I already have, and I see the new category straight away.

## US-02: Set a Due Date on a Task
**Story:** As a user, I want to give a task a due date, so that I know what to do first and I don't miss my deadlines.
**Estimate:** 2 Story Points (reference story).
**Justification:** It is our reference story and the smallest one, because it is one optional field with one simple date check and it doesn't change any other feature.
**Acceptance Criteria:**
* I can add a due date when I create or edit a task, and I see it next to the task.
* A task without a due date is still accepted.
* When I create a task, a due date in the past is not accepted and I see "Due date can't be in the past".
* An open task whose due date has passed is shown as "Overdue", and a completed task is never shown as "Overdue".

## US-03: Filter Tasks by Category and Status
**Story:** As a user with a lot of tasks, I want to filter my list by category and by status (open or completed), so that I can focus only on the tasks that matter right now.
**Estimate:** 5 Story Points.
**Justification:** It is the biggest story because it needs US-01 first, it has two filters that must work together, and it has more edge cases (no results, clearing the filters) than the other two.
**Acceptance Criteria:**
* When I choose a category, I see only the tasks in that category.
* When I choose "Open" or "Completed", I see only the tasks with that status.
* I can use both filters together, for example Work + Open shows only the open Work tasks.
* If no task matches, I see "No tasks match your filters" and not an empty screen.
* When I clear the filters, I see all my tasks again.

---

## SP-01: Technical Spike for Notification Support
**Type:** Technical Spike. It is research and a small prototype, not a feature for the user.
**Timebox:** 1 day. A spike doesn't get story points, because what it gives us is knowledge, not working features.
**Why we need it:** The customer wants real-time notifications (US-04), but we couldn't estimate it. In the old code `complete_task()` prints the log line and the email line directly inside the method. That design is Rigid: every new channel means changing `TaskManager` again. We didn't know how much work it would be to change this safely.
**Question to answer:** Can we add a new notification channel without touching `TaskManager`, and without breaking the log and email messages we already have?
**Status:** Done in Sprint Zero.
**Result:**
* `complete_task()` now uses a `Notifier` interface (Open-Closed Principle). The details are in RD-003.
* A test adds a new `PushNotifier` without any change to `TaskManager`, so a new channel is just a new class.
* A test checks that the old `[LOG]` and `[EMAIL]` output is exactly the same as before.
* Now the team thinks US-04 is about **5 points**. The hard part is not the code in `TaskManager` any more, but the real push service and the user settings.

## US-04: Real-Time Task Notifications
**Story:** As a user, I want to get a notification straight away when a task is completed, so that I know about progress without opening the app all the time.
**Estimate:** Not estimated yet. After SP-01 our first guess is about 5 points, to confirm at the next Planning Game.
**Justification:** We couldn't estimate it before the spike because we didn't know how rigid the code was. Now we know the change in `TaskManager` is small, but connecting a real push service and adding the settings is still more work and more risk than US-01.
**Acceptance Criteria (draft, to refine with the PO):**
* When a task is completed, I get a push notification within 5 seconds.
* The notification shows the title of the task.
* If I switch push notifications off in my settings, I don't get any.
* The log message and the email message still work as before.
