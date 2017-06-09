import unittest
import os
import sys
sys.path = ["../"] + sys.path
import escape

class TestInputReaders(unittest.TestCase):

    def test_get_string_input(self):
        os.environ["INPUT_test"] = "input"
        self.assertEqual(escape.get_string_input("test"), "input")

    def test_get_list_input(self):
        os.environ["INPUT_test"] = '["test1", "test2"]'
        self.assertEqual(escape.get_list_input("test")[0], "test1")
        self.assertEqual(escape.get_list_input("test")[1], "test2")

    def test_get_empty_list_input(self):
        os.environ["INPUT_test"] = ""
        self.assertEqual(escape.get_list_input("test"), [])
