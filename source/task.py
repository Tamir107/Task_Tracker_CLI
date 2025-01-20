import datetime
import json

class Task:

    def __init__(self, description, task_id):
        self.task_id = task_id
        self.description = description
        self.status = "To_Do"
        self.createdAt = datetime.datetime.now().__str__()
        self.updatedAt = datetime.datetime.now().__str__()

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


    def update(self, json_path, new_description):
        with open(json_path, 'r+') as file:
            data = json.load(file)
            if self.task_id.__str__() in data.keys():
                data[self.task_id.__str__()]['description'] = new_description
                file.seek(0)
                file.write(json.dumps(data))
                file.truncate()
                print(f'Task #{self.task_id} has been updated successfully.')
            else:
                print(f'Task #{self.task_id} does not exist.')

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