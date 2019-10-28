import sys
import os
import json_handler
import database


def main():
    # try:
    #     len(sys.argv) < 2
    # except:
    #     print("no arguments passed")
    if len(sys.argv) < 2:
        print("no arguments passed")
        sys.exit(1)

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
