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


if __name__ == "__main__":
    main()
