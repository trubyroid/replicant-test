import pytest
import json


@pytest.fixture(scope="function")
def get_info(request):
    """Gets info about person condition and his answers"""
    with open("./json/answers.json", 'r') as file:
        answers: list = json.load(file)
    with open("./json/condition.json", 'r') as file:
        condition: list = json.load(file)
    request.cls.answers = answers
    request.cls.condition = condition
    
