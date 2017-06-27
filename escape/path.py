
import os

def is_binary_on_path(binary, path_string = None):
    if path_string is not None:
        path_string = get_path()
    dirs = parse_path_string(path_string)
    for d in dirs:
        p = os.path.join(d, binary)
        if os.path.isfile(p) and os.access(p, os.X_OK):
            return True
    return False

def get_path():
    return os.environ.get("PATH", "")

def parse_path_string(string):
    if string == "":
        return []
    return string.split(":")


