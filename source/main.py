import argparse
import os.path
import json
from task import Task

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
mark_in_progress = subparser.add_parser('mark-in-progress')
mark_done = subparser.add_parser('mark-done')
list_command = subparser.add_parser('list')

add.add_argument('task_description', type=str)
update.add_argument('update_task_id', type=int)
update.add_argument('updated_task_description', type=str)
delete.add_argument('delete_task_id', type=int)
mark_in_progress.add_argument('mark_in_progress_task_id', type=int)
mark_done.add_argument('mark_done_task_id', type=int)
list_command.add_argument('status', default='all',nargs='?', choices=['all','done','todo','in-progress'])

args = parser.parse_args()

if args.command == 'add':
    Task(args.task_description).add(json_path)
elif args.command == 'update':
    pass
    # task_to_update = Task(json_path, task_id= args.update_task_id)
    # task_to_update.update(json_path)
elif args.command == 'delete':
    print('you deleted something')
elif args.command == 'mark-in-progress':
    print('you marked something as "in progress"')
elif args.command == 'mark-done':
    print('you marked something as "done"')
elif args.command == 'list':
    if args.status == 'done':
        print('done listed items')
    elif args.status == 'todo':
        print('todo listed items')
    elif args.status == 'in-progress':
        print('in-progress listed items')
    else:
        print('all listed items')
else:
    print('Please choose an action: add, update, delete, list, mark-in-progress, mark-done')