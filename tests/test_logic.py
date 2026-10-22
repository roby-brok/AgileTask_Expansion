import io
import unittest
from contextlib import redirect_stdout

from app.logic import TaskManager


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


if __name__ == "__main__":
    unittest.main()
