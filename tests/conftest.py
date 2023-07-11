import pytest
import json


@pytest.fixture
def get_info(request):
    """Gets info about person condition and his answers"""
    with open("./json/answers.json", 'r') as file:
        request.cls.answers = json.load(file)
    with open("./json/condition.json", 'r') as file:
        request.cls.condition = json.load(file)
