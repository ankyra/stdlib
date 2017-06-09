import os
import json

def get_string_input(key):
    return os.environ["INPUT_" + key]

def get_list_input(key):
    i = get_string_input(key)
    if i == "":
        return []
    return json.loads(i)
