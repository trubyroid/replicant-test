import json
import pytest


def create_summary(answers, condition):
    with open("./json/answers.json", "w") as write_file:
        json.dump(answers, write_file)
    with open("./json/condition.json", "w") as write_file:
        json.dump(condition, write_file)


def analysis(answers: list, condition: list):

    create_summary(answers, condition)

    result = int(pytest.main())
    if result == 1:
        print("\nWARNING: Responding subject is REPLICANT.")
    elif result == 0:
        print("\nResponding subject is human.")
