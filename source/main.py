import argparse
import os.path
import json
from source.task import Task

def main():
    json_path = '../tasks.json'

    if not os.path.exists(json_path):
        with open(json_path,'x') as file:
            file.write(json.dumps({}))
            print('New tasks file has been created')

    parser = argparse.ArgumentParser(prog='task-cli')

    subparser = parser.add_subparsers(dest='command')
    add = subparser.add_parser('add')
    update = subparser.add_parser('update')
    delete = subparser.add_parser('delete')
    mark_in_progress = subparser.add_parser('mark_in_progress')
    mark_done = subparser.add_parser('mark_done')
    list_command = subparser.add_parser('list')

    add.add_argument('task_description', type=str)
    update.add_argument('update_task_id', type=int)
    update.add_argument('updated_task_description', type=str)
    delete.add_argument('delete_task_id', type=int)
    mark_in_progress.add_argument('mark_in_progress_task_id', type=int)
    mark_done.add_argument('mark_done_task_id', type=int)
    list_command.add_argument('status', default='All',nargs='?', choices=['All','Done','To_Do','In_Progress'])

    args = parser.parse_args()

    if args.command == 'add':
        with open(json_path, 'r') as file:
            data = json.load(file)
            amount_of_tasks = len(data.keys())
            Task(args.task_description, amount_of_tasks + 1).add(json_path)
    elif args.command == 'update':
        with open(json_path, 'r+') as file:
            data = json.load(file)
            if str(args.update_task_id) in data.keys():
                data[str(args.update_task_id)]['description'] = args.updated_task_description
                file.seek(0)
                file.write(json.dumps(data))
                file.truncate()
                print(f'Task #{args.update_task_id} has been updated successfully.')
            else:
                print(f'Task #{args.update_task_id} does not exist.')
    elif args.command == 'delete':
        with open(json_path, 'r+') as file:
            data = json.load(file)
            if str(args.delete_task_id) in data.keys():
                del data[str(args.delete_task_id)]
                file.seek(0)
                file.write(json.dumps(data))
                file.truncate()
                print(f'Task #{args.delete_task_id} has been removed')
            else:
                print(f'Task #{args.delete_task_id} does not exist')
    elif args.command == 'mark_in_progress':
        with open(json_path, 'r+') as file:
            data = json.load(file)
            if str(args.mark_in_progress_task_id) in data.keys():
                data[str(args.mark_in_progress_task_id)]['status'] = 'In_Progress'
                file.seek(0)
                file.write(json.dumps(data))
                file.truncate()
                print(f'Task #{args.mark_in_progress_task_id} has been marked "In Progress"')
            else:
                print(f'Task #{args.mark_in_progress_task_id} does not exist')
    elif args.command == 'mark_done':
        with open(json_path, 'r+') as file:
            data = json.load(file)
            if str(args.mark_done_task_id) in data.keys():
                data[str(args.mark_done_task_id)]['status'] = 'Done'
                file.seek(0)
                file.write(json.dumps(data))
                file.truncate()
                print(f'Task #{args.mark_done_task_id} has been marked "Done"')
            else:
                print(f'Task #{args.mark_done_task_id} does not exist')
    elif args.command == 'list':
        with open(json_path, 'r') as file:
            data = json.load(file)
        filtered_tasks = [
            f'Task #{key}, Description: {value["description"]}, Status: {value["status"]}, Created At: {value["createdAt"]}'
            f', Updated At: {value["updatedAt"]}'
            for key, value in data.items()
            if args.status == "All" or value['status'] == args.status
        ]
        print(filtered_tasks)
    else:
        print('Please choose an action: add, update, delete, list, mark_in_progress, mark_done')

if __name__ == '__main__':
    main()