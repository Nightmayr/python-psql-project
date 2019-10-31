import sys
import os
import json_handler
import database
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Process a JSON file to be loaded postgres database")
    parser.add_argument('json_path', type=str, nargs=1,
                        help='an absolute or relative path to the json file')

    args = parser.parse_args()
    print(args.json_path[0])
    if len(sys.argv) < 2:
        print("no arguments passed")
        sys.exit(1)

    if os.path.abspath(sys.argv[1]):
        json_file = sys.argv[1]
    else:
        json_file = os.getcwd()+'/'+sys.argv[1]
    print(json_file)

    if os.path.exists(json_file) == False:
        print("Incorrect JSON path")
        sys.exit(1)

    json_map = json_handler.json_reader(json_file)
    database.database_insert(json_map)
    database.database_select()


if __name__ == "__main__":
    main()
