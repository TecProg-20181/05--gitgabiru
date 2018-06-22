import unittest
import os
import subprocess
from diskspace import *

class TestClass(unittest.TestCase):

    def test_bytes_to_readable(self):
        blocks = 100
        self.assertEqual(bytes_to_readable(blocks), "50.00Kb")

    def test_subprocess_check_output(self):
        path = "/test/"
        self.assertEqual(subprocess_check_output(path),['/test'])
        
   def test_show_space_list(self):
    self.assertIsNone(show_space_list(directory='.', depth=-1, order=True))

suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
