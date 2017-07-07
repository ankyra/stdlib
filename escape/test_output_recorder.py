import unittest
import os
import sys
import escape

class TestOutputRecorder(unittest.TestCase):

    def test_get_string_input(self):
        result = escape.OutputRecorder().run_script(["/bin/echo", "-e", "test\ntest2"])
        self.assertEqual(result, ["test", "test2"])

