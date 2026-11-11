# File Handling and Storage: A crucial apsect of programming that allows you to work with files, enabling you to read data from files, write data to files, and manage file storage.

import json  # standard-library module


def save_routes(routes, filename):
    with open(filename, "w", encoding="utf-8") as f:    # "w" = write (overwrites)
        json.dump(routes, f, indent=2)

def load_routes(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:   # "r" = read
            return json.load(f)
    except FileNotFoundError:
        print(f"{filename} not found, starting with empty list")
        return []

def log_event(message, filename="matatu_log.txt"):
    with open(filename, "a", encoding="utf-8") as f:    # "a" = append (keeps old content)
        f.write(message + "\n")