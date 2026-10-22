import io
import unittest
from contextlib import redirect_stdout

from app.logic import (
    ConsoleLogNotifier,
    EmailNotifier,
    Notifier,
    Task,
    TaskManager,
    TaskNotFoundError,
)


class PushNotifier(Notifier):
    """A new channel written only here. TaskManager is not changed for it."""

    def __init__(self) -> None:
        self.sent: list[str] = []

    def notify(self, task: Task) -> None:
        self.sent.append(f"[PUSH] {task.title} is done")


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task_returns_task_with_id_and_title(self):
        task = self.manager.add_task("Write report")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Write report")

    def test_new_task_is_open(self):
        task = self.manager.add_task("Write report")
        self.assertFalse(task.completed)

    def test_complete_task_marks_task_as_done(self):
        task = self.manager.add_task("Write report")
        with redirect_stdout(io.StringIO()):
            self.manager.complete_task(task.task_id)
        self.assertTrue(task.completed)

    def test_list_tasks_returns_every_task_in_order(self):
        self.manager.add_task("Write report")
        self.manager.add_task("Book room")
        titles = [task.title for task in self.manager.list_tasks()]
        self.assertEqual(titles, ["Write report", "Book room"])

    def test_empty_title_is_rejected(self):
        for title in ["", "   "]:
            with self.subTest(title=title):
                with self.assertRaises(ValueError):
                    self.manager.add_task(title)
        self.assertEqual(self.manager.list_tasks(), [])

    def test_get_task_with_unknown_id_raises_task_not_found(self):
        with self.assertRaises(TaskNotFoundError):
            self.manager.get_task(99)

    def test_complete_task_with_unknown_id_raises_task_not_found(self):
        with self.assertRaises(TaskNotFoundError):
            self.manager.complete_task(99)

    def test_mark_complete_twice_keeps_task_done(self):
        task = self.manager.add_task("Write report")
        task.mark_complete()
        task.mark_complete()
        self.assertTrue(task.completed)


class TestNotifications(unittest.TestCase):

    def test_old_log_and_email_output_is_preserved(self):
        manager = TaskManager([ConsoleLogNotifier(), EmailNotifier()])
        task = manager.add_task("Write report")
        output = io.StringIO()
        with redirect_stdout(output):
            manager.complete_task(task.task_id)
        self.assertEqual(
            output.getvalue(),
            "[LOG] Task completed: Write report\n"
            "[EMAIL] Sending email: task 'Write report' is completed\n",
        )

    def test_new_push_notifier_plugs_in_without_changing_task_manager(self):
        manager = TaskManager([ConsoleLogNotifier()])
        push = PushNotifier()
        manager.register_notifier(push)
        task = manager.add_task("Write report")
        with redirect_stdout(io.StringIO()):
            manager.complete_task(task.task_id)
        self.assertEqual(push.sent, ["[PUSH] Write report is done"])


if __name__ == "__main__":
    unittest.main()
