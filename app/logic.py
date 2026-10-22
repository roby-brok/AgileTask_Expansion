"""AgileTask: baseline task logic (the existing system)."""


class Task:
    def __init__(self, task_id, title, description=""):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = False


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title, description=""):
        task = Task(self.next_id, title, description)
        self.tasks[task.task_id] = task
        self.next_id = self.next_id + 1
        return task

    def complete_task(self, task_id):
        task = self.tasks[task_id]
        task.completed = True
        # tell the user the task is done
        print("[LOG] Task completed: " + task.title)
        print("[EMAIL] Sending email: task '" + task.title + "' is completed")
        return task

    def list_tasks(self):
        return list(self.tasks.values())
