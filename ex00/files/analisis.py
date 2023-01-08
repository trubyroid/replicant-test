"""
This file contain function for analisis person stats.
"""

from tests.analysis_tests import *


def analysis(condition: list, answers: list):
    """
    This function call tests and count the score which
    defines result of programm working. Also write result to
    history file. It's called by the end.

    ...
    Parameters
    ----------
    condition: list
        list with changing of person condition
    answers: list
        list with person answers
    """
    age = answers[0]
    death = answers[1]
    money = answers[4]
    sex = answers[6]
    mood = answers[9]
    score = 0

    score += test_age(age, condition)
    score += test_money(money, condition)
    score += test_sex(sex, condition)
    score += test_mood(mood, death)
    score += test_president(condition)

    if score >= 0:
        result = "human."
    else:
        result = "replicant!"

    with open("./json/history.json", "a") as write_file:
        write_file.write("{")
        write_file.write('"')
        write_file.write("Result")
        write_file.write('"')
        write_file.write(": ")
        write_file.write('"')
        write_file.write(result)
        write_file.write('"')
        write_file.write("}\n")

    return result
