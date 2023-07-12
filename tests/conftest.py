import pytest
import json


@pytest.fixture(scope="function")
def answers():
    """Receives person's answers"""
    with open("./json/answers.json", 'r') as file:
        return json.load(file)

    
@pytest.fixture(scope="function")
def condition():
    """Receives information about a person's condition"""
    with open("./json/condition.json", 'r') as file:
        return json.load(file)
