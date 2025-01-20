import os
import unittest

class TestTasksCLI(unittest.TestCase):

    run_main = 'py ..\source\main.py'

    def test_entry_point(self):
        response = os.system(f'{TestTasksCLI.run_main}')
        self.assertEqual(response, 'Please choose an action: add, update, delete, list, mark_in_progress, mark_done')