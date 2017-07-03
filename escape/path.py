import os
import shutil

def is_binary_on_path(binary, path_string = None):
    if path_string is None:
        path_string = get_path()
    dirs = parse_path_string(path_string)
    for d in dirs:
        p = os.path.join(d, binary)
        if os.path.isfile(p) and os.access(p, os.X_OK):
            return True
    return False

def add_binary_to_path(binary_location):
    path = get_path()
    for p in path.split(":"):
        target = os.path.join(p, os.path.basename(binary_location))
        try:
            shutil.copy(binary_location, target)
            print "Copied", binary_location, "to", target
            return True
        except:
            print "WARN: Couldn't copy", binary_location, "to", target
    return False

def get_path():
    return os.environ.get("PATH", "")

def parse_path_string(string):
    if string == "":
        return []
    return string.split(":")


