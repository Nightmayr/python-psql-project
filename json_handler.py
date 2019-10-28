import json


def json_reader(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
    return data


if __name__ == "__main__":
    json_reader("file.json")
