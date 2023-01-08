"""
Here we ask questions, get the answers
and collect the conditions person.
"""

from files.anamnesis import get_anamnesis
from files.analisis import analysis
import random


def get_answer(answers) -> int:
    """Randomly return the digit of answer"""
    return random.choice(answers)


def testing(qa: dict) -> str:
    """Create the process of whole test"""
    digits_answ = []
    condition = []

    for question in qa:
        print("\nQuestion: ", question)

        answer_digit = get_answer(list(qa[question].keys()))
        digits_answ.append(answer_digit)
        answer = qa[question][str(answer_digit)]
        print("Answer: ", answer)

        condition.append(get_anamnesis())

    analysis(digits_answ, condition)
