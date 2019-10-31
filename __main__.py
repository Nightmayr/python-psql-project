import sys
import os
import json_handler
import database
import argparse


def main():
    parser = argparse.ArgumentParser(prog="python-psql-loader",
                                     description="Process a JSON file to be loaded to  a postgres database")
    parser.add_argument('json_path', type=str, nargs=1,
                        help='an absolute or relative path to the json file')

    args = parser.parse_args()

    if os.path.abspath(args.json_path[0]):
        json_file = args.json_path[0]
    else:
        json_file = os.getcwd()+'/'+args.json_path[0]

    if os.path.exists(json_file) == False:
        print("Incorrect JSON path")
        sys.exit(1)

    json_map = json_handler.json_reader(json_file)
    database.database_insert(json_map)
    database.database_select()


if __name__ == "__main__":
    main()
