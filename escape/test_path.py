import unittest
from escape import path

class TestInputReaders(unittest.TestCase):

    def test_is_binary_on_path(self):
        cases = {
            "ls": True,
            "aoifjwoeifjaoijef": False,
            "": False
        }
        for test, expected in cases.iteritems():
            self.assertEqual(path.is_binary_on_path(test, ""), expected, test)

    def test_parse_path_string(self):
        cases = {
            "": [],
            "/test": ["/test"],
            "/test:/test2": ["/test", "/test2"]
        }
        for test, expected in cases.iteritems():
            self.assertEqual(path.parse_path_string(test), expected)


