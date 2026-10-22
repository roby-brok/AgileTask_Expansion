# AgileTask_Expansion

**Module:** SWE6301 Agile Programming, Week 4: The Scrum Framework
**Activity:** Sprint Zero: Establishing the Rhythm of Scrum through the "AgileTask" Expansion

In this repo we plan and start the expansion of AgileTask, our simple task manager. `app/logic.py` holds the code of the existing system, and `docs/` holds our Scrum documents.

## Scrum Team

| Role | Name | What they do |
|---|---|---|
| Product Owner | Adrian | Owns the Product Backlog, decides the priority of the stories and speaks for the customer. |
| Scrum Master | Blagoy | Runs the Scrum events, removes blockers and protects the team's process and pace. |
| Developer | Roberto Cassano Brocato | Estimates and builds the stories, writes the tests and follows the Definition of Done. |

## Structure

```
AgileTask_Expansion/
├── app/
│   ├── __init__.py
│   └── logic.py         # Task, TaskManager and the Notifier classes
├── docs/
│   ├── BACKLOG.md       # Product Backlog
│   ├── DOD.md           # Team Definition of Done
│   ├── RATIONALE.md     # Why we took our design decisions
│   └── REFLECTION.md    # Sprint Zero review answers
├── tests/
│   ├── __init__.py
│   └── test_logic.py    # Unit tests
├── .gitignore
└── README.md
```

## How to run the tests

You need Python 3.10 or newer. We only use `unittest` from the standard library, so there is nothing to install.

From the repo folder run:

```bash
python -m unittest discover -s tests -v
```

## Progression

`SETUP` (roles/repo) → `ADD` (DoD) → `UPDATE` (estimated backlog) → `REFACTOR` (spike / Boy Scout Rule) → `REFLECT`
