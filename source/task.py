import datetime
import json

class Task:

    number_of_tasks = 0

    def __init__(self, description, status):
        self.task_id = Task.number_of_tasks
        self.description = description
        self.status = status
        self.createdAt = datetime.datetime.now().__str__()
        self.updatedAt = datetime.datetime.now().__str__()
        Task.number_of_tasks += 1

    def add(self, json_path):
        task_data = {
            'description': self.description,
            'status': self.status,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
        with open(json_path, 'r+') as file:
            data = json.load(file)
            if not self.task_id.__str__() in data.keys():
                data[self.task_id] = task_data
                file.seek(0)
                file.write(json.dumps(data))
                file.truncate()
                print(f'New task (#ID: {self.task_id}) has been created')
            else:
                print('There is already a task with that id')


    def remove(self, json_path):
        with open(json_path, 'r+') as file:
            data = json.load(file)
            if self.task_id.__str__() in data.keys():
                del data[self.task_id.__str__()]
                file.seek(0)
                file.write(json.dumps(data))
                file.truncate()
                print(f'Task #{self.task_id} has been removed')
            else:
                print(f'Task #{self.task_id} does not exist')
