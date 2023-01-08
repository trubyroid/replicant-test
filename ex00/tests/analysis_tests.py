"""
This file contains buisness logic.
Here you may find test cases for each person.

...
Parameters
----------
age: int
    contains the number of answer for question about age
money: int
    contains the number of answer for question about money
mood: int
    contains the number of answer for question about mood
death: int
    contains the number of answer for question about death
sex: int
    contains the number of answer for question about sex
condition: list
    contains changing of person condition
"""


def test_age(age, condition):
    """
    Checks that old people started breath more often on question about sex

    ...
    Parameters
    ----------
    age: int
        contains the number of answer for question about age
    condition: list
        contains changing of person condition
    """
    if (age == 4 and condition[6].respiration <= 16):
        return -1
    return 0


def test_money(money, condition):
    """
    Checks that heart of angry people started moving faster

    ...
    Parameters
    ----------
    money: int
        contains the number of answer for question about money
    condition: list
        contains changing of person condition
    """
    if (money == 1 and condition[4].heart_rate < 80):
        return -1
    return 0


def test_sex(sex, condition):
    """
    Checks that people with pair started blushing on questing about sex
    after question about his boy/girl/hs/wf.

    ...
    Parameters
    ----------
    sex: int
        contains the number of answer for question about sex
    condition: list
        contains changing of person condition
    """
    if (sex == 1 and condition[5].blushing_level < 4):
        return -1
    return 0


def test_mood(mood, death):
    """
    Checks that people who always thinking about death not feeling "awesome".

    ...
    Parameters
    ----------
    mood: int
        contains the number of answer for question about mood
    condition: list
        contains changing of person condition
    """
    if (death == 3 and mood == 1):
        return -1
    return 0


def test_president(condition):
    """
    Checks that people not worried too much on question about president.

    ...
    Parameters
    ----------
    condition: list
        contains changing of person condition
    """
    if (condition[8].heart_rate == 150):
        return -5
    return 0
