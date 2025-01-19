import json
import unittest

from source.task import Task

class MyTestCase(unittest.TestCase):
    dummy_tasks = './dummy_tasks.json'

    def setUp(self):
        print('Setting up')
        with open(MyTestCase.dummy_tasks, 'w') as file:
            file.write(json.dumps({}))
            file.truncate()

    def tearDown(self):
        Task.number_of_tasks = 0

    def test_add_new_task(self):
        task = Task('test', 'To Do')
        task.add(MyTestCase.dummy_tasks)
        with open(MyTestCase.dummy_tasks, 'r') as file:
            data = json.load(file)

        self.assertEqual(data[f'{task.task_id}']['description'], task.description)
        print(data)

    def test_add_two_tasks(self):
        task1 = Task('First Task', 'Done')
        task2 = Task('Second Task', 'In Progress')
        task1.add(MyTestCase.dummy_tasks)
        task2.add(MyTestCase.dummy_tasks)
        with open(MyTestCase.dummy_tasks, 'r') as file:
            data = json.load(file)
        data_keys = data.keys()
        self.assertTrue(task1.task_id.__str__() in data_keys and task2.task_id.__str__() in data_keys)
        print(data)

    def test_delete_task(self):
        task = Task('Test', 'To Do')
        task.add(MyTestCase.dummy_tasks)
        with open(MyTestCase.dummy_tasks, 'r') as file:
            data_before_removal = json.load(file)

        print(data_before_removal)
        length_before_removal = len(data_before_removal.keys())
        task.remove(MyTestCase.dummy_tasks)
        with open(MyTestCase.dummy_tasks, 'r') as file:
            data_after_removal = json.load(file)
        length_after_removal = len(data_after_removal.keys())
        print(data_after_removal)
        print(length_before_removal)
        print(length_after_removal)
        self.assertTupleEqual((length_before_removal,length_after_removal),(1,0))


    def test_mark_task(self):
        pass




if __name__ == '__main__':
    unittest.main()
