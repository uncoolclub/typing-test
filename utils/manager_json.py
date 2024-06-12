import json
import os

def set_file_path(nickname):
    return f"../User/personal/{nickname}.json"

def create_file(nickname):
    file_path = set_file_path(nickname)
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding="UTF-8") as file:
            json.dump({}, file, indent=4)

def read_json(nickname):
    file_path = set_file_path(nickname)
    with open(file_path, 'r', encoding="UTF-8") as file:
        return json.load(file)