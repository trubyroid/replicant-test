"""
This is a parser. Here we pars question and answers from json.
"""

import json
import pathlib


def parsing():
    """Here we check the location, availability
    and occupancy of the json file. Then we parse it to dict.
    """
    path = pathlib.Path("./json/QA.json")
    if path.is_file():

        file = open("./json/QA.json")
        content = file.read()
        if not content:
            print("Please, fill QA.json.")
            exit()
        file.close()

        file = open("./json/QA.json")
        qa = json.load(file)
        return qa
    else:
        print("Please, put QA.json into docs.")
        exit()
