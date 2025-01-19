import datetime
import json

class Task:

    number_of_tasks = 0

    def __init__(self, description, task_id=number_of_tasks):
        self.task_id = task_id
        self.description = description
        self.status = "To Do"
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

    def mark(self, json_path, new_status):
        with open(json_path, 'r+') as file:
            data = json.load(file)
            if self.task_id.__str__() in data.keys():
                data[self.task_id.__str__()]['status'] = new_status
                file.seek(0)
                file.write(json.dumps(data))
                file.truncate()
                print(f'Task #{self.task_id} has been marked "{new_status}"')
            else:
                print(f'Task #{self.task_id} does not exist')

    @staticmethod
    def list_tasks(json_path, status='All'):
        with open(json_path, 'r') as file:
            data = json.load(file)
        filtered_tasks = [
            f'Task #{key}, Description: {value["description"]}, Status: {value["status"]}, Created At: {value["createdAt"]}'
            f', Updated At: {value["updatedAt"]}'
            for key, value in data.items()
            if status == "All" or value['status'] == status
        ]
        print(filtered_tasks)
        return filtered_tasks