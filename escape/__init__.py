import os

def get_string_input(key):
    return os.environ["INPUT_" + key]
