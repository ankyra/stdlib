import unittest
import escape
import sys
import json
import os

class TestOutputs(unittest.TestCase):
    def test_get_outputs(self):
        outputs = {
            "test": "my output",
        }
        with open("outputs.json", "w") as f:
            f.write(json.dumps(outputs))
        sys.argv = ["program-name", "outputs.json"]
        outputs = escape.get_outputs()
        self.assertEqual(outputs["test"], "my output")
        os.unlink("outputs.json")

    def test_set_output_and_save(self):
        outputs = {
            "test": "my output",
        }
        with open("outputs.json", "w") as f:
            f.write(json.dumps(outputs))
        sys.argv = ["program-name", "outputs.json"]
        outputs = escape.get_outputs()
        outputs.set_output("test", "override")
        self.assertEqual(outputs["test"], "override")
        outputs.save()
        with open("outputs.json", "r") as f:
            result = json.loads(f.read())
        self.assertEqual(result["test"], "override")
        os.unlink("outputs.json")
