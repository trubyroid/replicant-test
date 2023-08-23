"""
Here we ask questions, get the answers
and collect the conditions person.
"""

from files.anamnesis import get_anamnesis
from files.analisis import analysis
import random
import json


def create_history(qa, question, answer_digit):
    """Update history of participants"""
    logs = {}
    answer = qa[question][str(answer_digit)]
    logs[question] = answer
    with open("./json/history.json", "a") as write_file:
        json.dump(logs, write_file)
        write_file.write("\n")
    del logs[question]


def get_answer(qa, question) -> int:
    """Get or randomly create the digit of answer"""
    for answ in qa[question]:
        print(answ, end=".")
        print(qa[question][answ])
    answer = input("\nAnswer: ")
    if answer == "":
        answers = list(qa[question].keys())
        answer = random.choice(answers)
        return answer
    else:
        if answer in qa[question].values():
            for num, answ in qa[question].items():
                if answ == answer:
                    return num
        if answer in qa[question].keys():
            return answer
    print("Invalid answer.\n")
    return get_answer(qa, question)


def testing(qa: dict) -> str:
    """Create the process of whole test"""
    digits = []
    condition = []

    for question in qa:
        print("\nQuestion: ", question)
        answer = get_answer(qa, question)
        digits.append(answer)
        create_history(qa, question, answer)
        condition.append(get_anamnesis())

    analysis(digits, condition)
