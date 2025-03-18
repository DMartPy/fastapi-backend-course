import json

class TaskStorage:
    def __init__(self, task_file) -> None:
        self.storage_file = task_file

    def load_tasks(self):
        try:
            with open(self.storage_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self, tasks):
        with open(self.storage_file, "w") as f:
            json.dump(tasks, f)