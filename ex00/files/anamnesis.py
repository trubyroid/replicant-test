"""
This module contain function that ask values
that describe person condition for now.
"""

from files.person import Anamnesis


def get_anamnesis():
    """
    This function asks, checks and saves four indicators of
    person condition: respiration, heart rate, blushing level and
    pupillary dilation. Next it return class with validated parameters.
    It's called for each question.
    """
    resp = input("Please enter the respiration bpm: ")
    assert resp.isdigit(), "It have to be integer"
    hr = input("Please enter the heart bpm: ")
    assert hr.isdigit(), "It have to be integer"
    bl = input("Please enter the blushing level: ")
    assert bl.isdigit(), "It have to be integer"
    pd = input("Please enter the pupillary dilation: ")
    assert pd.isdigit(), "It have to be integer"
    return Anamnesis(respiration=resp, heart_rate=hr,
                     blushing_level=bl, pupillary_dilation=pd)
