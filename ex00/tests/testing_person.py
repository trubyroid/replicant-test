"""
This file contain function which conducts testing and
write a history about participants.
"""

from files.database import QA
from files.person import Anamnesis, get_answer
from files.anamnesis import get_anamnesis
from files.analisis import analysis
from random import randint
import json


def testing() -> str:
    """
    This function conducts testing, save results,
    write a history about participants and started collecting anamnesis

    ...
    Parameters
    ----------
    logs: dict
        contains questions and answers for history about participants
    digit_answ: list
        contains numbers of answers
    condition: list
        contains classes. each class - person condition after question
    """
    logs = {}
    digits_answ = []
    condition: Anamnesis = []

    with open("./json/history.json", "a") as write_file:
        write_file.write("\nCase# " + str(randint(1, 1000)) + ":\n")

    for n in QA:
        question = n[0]
        print("\nQuestion: ", question)

        answer_digit = get_answer(question)
        digits_answ.append(answer_digit)
        answer = n[1][answer_digit]
        print("Answer: ", answer)

        logs[question] = answer
        with open("./json/history.json", "a") as write_file:
            json.dump(logs, write_file)
            write_file.write("\n")
        del logs[question]

        condition.append(get_anamnesis())

    return analysis(condition, digits_answ)
