import json
import pathlib


def parsing():
    path = pathlib.Path("./json/database.json")
    if path.is_file():

        file = open("./json/database.json")
        content = file.read()
        if not content:
            print("Please, fill database.json.")
            exit()
        file.close()

        file = open("./json/database.json")
        qa = json.load(file)
        return qa
    else:
        print("Please, put database.json into docs.")
        exit()
