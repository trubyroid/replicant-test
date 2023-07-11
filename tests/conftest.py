import pytest
import json


@pytest.fixture(scope="function")
def answers():
    """Gets person answers"""
    with open("./json/answers.json", 'r') as file:
        return json.load(file)

    
@pytest.fixture(scope="function")
def condition():
    """Gets info about person condition"""
    with open("./json/condition.json", 'r') as file:
        return json.load(file)
