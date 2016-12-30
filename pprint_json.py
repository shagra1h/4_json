import json
import os.path


def load_data(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as file_handler:
        jdata = json.load(file_handler)
        return jdata


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True))

if __name__ == '__main__':
    print("Enter the path to json file:")
    while True:
        path = input()
        if load_data(path) is None:
            print("Incorrect path to the file! Try again!")
        else:
            break
    json_data = load_data(path)
    pretty_print_json(json_data)
