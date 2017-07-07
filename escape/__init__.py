import os
import json
import sys

# Disable output buffering
if hasattr(sys.stdout, "fileno"):
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)

import path
import kube
import process
from .process import OutputRecorder

def get_string_input(key):
    return os.environ["INPUT_" + key]

def get_list_input(key):
    i = get_string_input(key)
    if i == "":
        return []
    return json.loads(i)


class Outputs:
    def __init__(self, path, outputs):
        self.path = path
        self.outputs = outputs

    def __getitem__(self, k):
        return self.outputs[k]

    def set_output(self, k, v):
        self.outputs[k] = v
        return self

    def save(self):
        print "Saving", self.path
        with open(self.path, 'w') as f:
            f.write(json.dumps(self.outputs))

def get_outputs():
    j = open(sys.argv[1]).read()
    return Outputs(sys.argv[1], json.loads(j))
