import json
import unittest
from unittest.mock import patch
import source.main as main
import contextlib
from io import StringIO


class TestTasksCLI(unittest.TestCase):

    def setUp(self):
        with open('../tasks.json', 'w') as file:
            file.seek(0)
            file.write(json.dumps({}))
            file.truncate()

    @patch('sys.argv', ['main.py'])
    def test_entry_point(self):
        stdout_response = StringIO()
        with contextlib.redirect_stdout(stdout_response):
            main.main()
        print(stdout_response.getvalue().strip())
        self.assertEqual(stdout_response.getvalue().strip(), 'Please choose an action: add, update, delete, list, mark_in_progress, mark_done')

    @patch('sys.argv', ['main.py', 'add', 'MyTask1'])
    def test_add_task(self):
        stdout_response = StringIO()
        with contextlib.redirect_stdout(stdout_response):
            main.main()
        print(stdout_response.getvalue().strip())
        self.assertEqual(stdout_response.getvalue().strip(), 'New task (#ID: 1) has been created')

    @patch('sys.argv', ['main.py', 'add', 'MyTask1'])
    def test_update_task(self):
        stdout_response = StringIO()
        with contextlib.redirect_stdout(stdout_response):
            main.main()
            with patch('sys.argv', ['main.py', 'update', '1', 'MyAnotherTask']):
                main.main()
        print(stdout_response.getvalue().strip())
        self.assertEqual(stdout_response.getvalue().strip(), 'New task (#ID: 1) has been created\nTask #1 has been updated successfully.')

    @patch('sys.argv', ['main.py', 'add', 'MyTask1'])
    def test_delete_task(self):
        stdout_response = StringIO()
        with contextlib.redirect_stdout(stdout_response):
            main.main()
            with patch('sys.argv', ['main.py', 'delete', '1']):
                main.main()
        print(stdout_response.getvalue().strip())
        self.assertEqual(stdout_response.getvalue().strip(), 'New task (#ID: 1) has been created\nTask #1 has been removed')

    @patch('sys.argv', ['main.py', 'add', 'MyTask1'])
    def test_mark_done_task(self):
        stdout_response = StringIO()
        with contextlib.redirect_stdout(stdout_response):
            main.main()
            with patch('sys.argv', ['main.py', 'mark_done', '1']):
                main.main()
        print(stdout_response.getvalue().strip())
        self.assertEqual(stdout_response.getvalue().strip(), 'New task (#ID: 1) has been created\nTask #1 has been marked "Done"')


    @patch('sys.argv', ['main.py', 'add', 'MyTask1'])
    def test_create_two_and_list(self):
        stdout_response = StringIO()
        with contextlib.redirect_stdout(stdout_response):
            main.main()
            with patch('sys.argv', ['main.py', 'add', 'MyTask2']):
                main.main()
            with patch('sys.argv', ['main.py', 'list']):
                main.main()

        print(stdout_response.getvalue().strip())
        self.assertEqual(stdout_response.getvalue().strip(), 'New task (#ID: 1) has been created\nNew task (#ID: 2) has been created')


if __name__ == "__main__":
    unittest.main()