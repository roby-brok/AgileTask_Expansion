"""AgileTask: task logic.

Spike SP-01: when a task is completed, TaskManager now passes it to a list of
Notifier objects. To add a new kind of notification we write a new Notifier
class and TaskManager stays the same (Open-Closed Principle). See RD-003 in
docs/RATIONALE.md.
"""

from abc import ABC, abstractmethod


class TaskNotFoundError(KeyError):
    """Raised when there is no task with the given id.

    It is a KeyError, so old code that catches KeyError still works.
    """


class Task:
    """One task in AgileTask."""

    def __init__(self, task_id: int, title: str, description: str = "") -> None:
        if not title.strip():
            raise ValueError("Task title can't be empty")
        self.task_id = task_id
        self.title = title.strip()
        self.description = description
        self.completed = False

    def mark_complete(self) -> None:
        """Mark the task as done. Calling it again changes nothing."""
        self.completed = True


class Notifier(ABC):
    """Interface for anything that wants to know when a task is completed."""

    @abstractmethod
    def notify(self, task: Task) -> None:
        """React to a task that has just been completed."""


class ConsoleLogNotifier(Notifier):
    """Prints the [LOG] line that complete_task() used to print."""

    def notify(self, task: Task) -> None:
        print(f"[LOG] Task completed: {task.title}")


class EmailNotifier(Notifier):
    """Prints the [EMAIL] line that complete_task() used to print."""

    def notify(self, task: Task) -> None:
        print(f"[EMAIL] Sending email: task '{task.title}' is completed")


class TaskManager:
    """Keeps the tasks and tells the notifiers when a task is completed."""

    def __init__(self, notifiers: list[Notifier] | None = None) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1
        self._notifiers: list[Notifier] = list(notifiers or [])

    def register_notifier(self, notifier: Notifier) -> None:
        """Add one more notification channel."""
        self._notifiers.append(notifier)

    def add_task(self, title: str, description: str = "") -> Task:
        """Create a new task, store it and return it."""
        task = Task(self._next_id, title, description)
        self._tasks[task.task_id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Task:
        """Return the task with this id, or raise TaskNotFoundError."""
        try:
            return self._tasks[task_id]
        except KeyError:
            raise TaskNotFoundError(f"No task with id {task_id}") from None

    def complete_task(self, task_id: int) -> Task:
        """Mark the task as done and tell every notifier."""
        task = self.get_task(task_id)
        task.mark_complete()
        self._notify(task)
        return task

    def list_tasks(self) -> list[Task]:
        """Return all the tasks in the order they were added."""
        return list(self._tasks.values())

    def _notify(self, task: Task) -> None:
        for notifier in self._notifiers:
            notifier.notify(task)
