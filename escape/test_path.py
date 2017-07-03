import unittest
import os
import shutil
from escape import path

class TestInputReaders(unittest.TestCase):

    def test_is_binary_on_path(self):
        cases = {
            "ls": True,
            "aoifjwoeifjaoijef": False,
            "": False
        }
        for test, expected in cases.iteritems():
            self.assertEqual(path.is_binary_on_path(test), expected, test)

    def test_add_binary_to_path(self):
        previousPath = os.environ["PATH"]
        os.environ["PATH"] = "test_path"
        os.mkdir("test_path")
        with open("test_file.txt", "w") as f:
            f.write("test")
        self.assertFalse(os.path.exists("test_path/test_file.txt"))
        self.assertTrue(path.add_binary_to_path("test_file.txt"))
        self.assertTrue(os.path.exists("test_path/test_file.txt"))
        shutil.rmtree("test_path")
        os.environ["PATH"] = previousPath

    def test_get_path(self):
        previousPath = os.environ["PATH"]
        os.environ["PATH"] = "yo"
        self.assertEqual(path.get_path(), "yo")
        os.environ["PATH"] = previousPath


    def test_parse_path_string(self):
        cases = {
            "": [],
            "/test": ["/test"],
            "/test:/test2": ["/test", "/test2"]
        }
        for test, expected in cases.iteritems():
            self.assertEqual(path.parse_path_string(test), expected)


