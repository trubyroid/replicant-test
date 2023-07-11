"""
test_person.py
====================================
Main test cases of this project.
Upload information about person from json and check it.
"""

import pytest


@pytest.mark.usefixtures("get_info")
def test_sex(get_info):
    """Checks that people blushing on talks about relationships"""
    if get_info.answers[5] == '1' or get_info.answers[5] == '2':
        assert int(get_info.condition[6]["blushing level"]) - \
            int(get_info.condition[5]["blushing level"]) > 1


@pytest.mark.usefixtures("get_info")
def test_death(get_info):
    """Checks that old people fear the death"""
    if get_info.answers[0] == '4':
        assert int(get_info.condition[1]["heart rate"]) - \
            int(get_info.condition[0]["heart rate"]) > 5


@pytest.mark.usefixtures("get_info")
def test_parents(get_info):
    """Checks that people don't live with dead parents"""
    if get_info.answers[2] == '1':
        assert get_info.answers[7] != '4'


@pytest.mark.usefixtures("get_info")
def test_work(get_info):
    """Checks that people who loooking for job don't be richy"""
    if get_info.answers[3] == '3':
        assert get_info.answers[4] != '4'


@pytest.mark.usefixtures("get_info")
def test_money(get_info):
    """Checks that heart of angry people started moving faster"""
    if get_info.answers[4] == '1':
        assert int(get_info.condition[4]["heart rate"]) - \
            int(get_info.condition[3]["heart rate"]) > 10


@pytest.mark.usefixtures("get_info")
def test_condition(get_info):
    """Checks that people with bad mood don't have a large pupils"""
    if get_info.answers[9] == '4':
        assert int(get_info.condition[9]["pupillary dilation"]) < 6


@pytest.mark.usefixtures("get_info")
def test_president(get_info):
    """Checks that people not worried too much on question about president"""
    assert int(get_info.condition[8]["heart rate"]) < 125
