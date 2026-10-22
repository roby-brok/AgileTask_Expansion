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
| | | **Total** | **10** |

**Reference story:** US-02 (2 points). It is the smallest and clearest story, so we compared all the others with it. The reasons for the order are in `docs/RATIONALE.md` (RD-002).

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
