"""
test_person.py
====================================
Main test cases of this project.
Upload information about person from json and check it.
"""

import pytest


@pytest.mark.usefixtures("get_info")
def test_sex(self):
    """Checks that people blushing on talks about relationships"""
    if self.answers[5] == '1' or self.answers[5] == '2':
        assert int(self.condition[6]["blushing level"]) - \
            int(self.condition[5]["blushing level"]) > 1


@pytest.mark.usefixtures("get_info")
def test_death(self):
    """Checks that old people fear the death"""
    if self.answers[0] == '4':
        assert int(self.condition[1]["heart rate"]) - \
            int(self.condition[0]["heart rate"]) > 5


@pytest.mark.usefixtures("get_info")
def test_parents(self):
    """Checks that people don't live with dead parents"""
    if self.answers[2] == '1':
        assert self.answers[7] != '4'


@pytest.mark.usefixtures("get_info")
def test_work(self):
    """Checks that people who loooking for job don't be richy"""
    if self.answers[3] == '3':
        assert self.answers[4] != '4'


@pytest.mark.usefixtures("get_info")
def test_money(self):
    """Checks that heart of angry people started moving faster"""
    if self.answers[4] == '1':
        assert int(self.condition[4]["heart rate"]) - \
            int(self.condition[3]["heart rate"]) > 10


@pytest.mark.usefixtures("get_info")
def test_condition(self):
    """Checks that people with bad mood don't have a large pupils"""
    if self.answers[9] == '4':
        assert int(self.condition[9]["pupillary dilation"]) < 6


@pytest.mark.usefixtures("get_info")
def test_president(self):
    """Checks that people not worried too much on question about president"""
    assert int(self.condition[8]["heart rate"]) < 125
