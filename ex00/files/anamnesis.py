"""
This module contain function that ask values
that describe person condition for now.
"""

from files.person import Anamnesis
from random import randint


def get_anamnesis():
    """
    This function asks, checks and saves four indicators of
    person condition: respiration, heart rate, blushing level and
    pupillary dilation. Next it return class with validated parameters.
    It's called for each question.
    """
    resp = input("Please enter the respiration bpm: ")
    if resp == "":
        resp = str(randint(10, 20))
    assert resp.isdigit(), "It have to be integer"
    hr = input("Please enter the heart bpm: ")
    if hr == "":
        hr = str(randint(40, 200))
    assert hr.isdigit(), "It have to be integer"
    bl = input("Please enter the blushing level: ")
    if bl == "":
        bl = str(randint(1, 6))
    assert bl.isdigit(), "It have to be integer"
    pd = input("Please enter the pupillary dilation: ")
    if pd == "":
        pd = str(randint(2, 8))
    assert pd.isdigit(), "It have to be integer"
    return Anamnesis(respiration=resp, heart_rate=hr,
                     blushing_level=bl, pupillary_dilation=pd)
