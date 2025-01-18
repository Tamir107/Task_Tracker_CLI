import datetime
import json

class Task:
    def __init__(self, task_id, description, status):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.createdAt = datetime.datetime.now()
        self.updatedAt = datetime.datetime.now()

    def add(self):
        task_data = {
            'id': self.task_id,
            'description': self.description,
            'status': self.status,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }