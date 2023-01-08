"""
This file contains functions which start pytesting.
"""

import json
import pytest


def create_summary(answers, condition):
    """Here we write a json files wich contains histoty of
    answers and conditions of person"""
    with open("./json/answers.json", "w") as write_file:
        json.dump(answers, write_file)
    with open("./json/condition.json", "w") as write_file:
        json.dump(condition, write_file)


def analysis(answers: list, condition: list):
    """Here we run testing and output the result"""

    create_summary(answers, condition)

    result = int(pytest.main())
    if result == 1:
        print("\nWARNING: Responding subject is REPLICANT.")
    elif result == 0:
        print("\nResponding subject is human.")
