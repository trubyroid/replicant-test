"""
test_person.py
====================================
Main test cases of this project.
Upload information about person from json and check it.
"""

import json


file = open("./json/answers.json")
answers = json.load(file)
file.close()

file = open("./json/condition.json")
condition = json.load(file)
file.close()


def test_sex():
    """Checks that people blushing on talks about relationships"""
    if (answers[5] == '1' or answers[5] == '2'):
        assert int(condition[6]["blushing level"]) - \
            int(condition[5]["blushing level"]) > 1


def test_death():
    """Checks that old people fear the death"""
    if (answers[0] == '4'):
        assert int(condition[1]["heart rate"]) - \
            int(condition[0]["heart rate"]) > 5


def test_parents():
    """Checks that people don't live with dead parents"""
    if (answers[2] == '1'):
        assert answers[7] != '4'


def test_work():
    """Checks that people who loooking for job don't be richy"""
    if (answers[3] == '3'):
        assert answers[4] != '4'


def test_money():
    """Checks that heart of angry people started moving faster"""
    if (answers[4] == '1'):
        assert int(condition[4]["heart rate"]) - \
            int(condition[3]["heart rate"]) > 10


def test_condition():
    """Checks that people with bad mood don't have a large pupils"""
    if (answers[9] == '4'):
        assert int(condition[9]["pupillary dilation"]) < 6


def test_president():
    """Checks that people not worried too much on question about president"""
    assert int(condition[8]["heart rate"]) < 125
