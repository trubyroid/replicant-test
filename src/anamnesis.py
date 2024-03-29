"""
This file collecting person conditions.
"""

from random import randint


def respiration():
    """Here we collect and validate the respiration"""
    val = input("Please enter the respiration bpm: ")
    if val == "":
        val = str(randint(11, 29))
    if not val.isdigit():
        print("It must be integer.")
        return respiration()
    if not 10 < int(val) < 30:
        print("Respiration bpm must be less than 30 and more than 10.")
        return respiration()
    return val


def heart_rate():
    """Here we collect and validate the heart rate"""
    val = input("Please enter the heart bpm: ")
    if val == "":
        val = str(randint(41, 199))
    if not val.isdigit():
        print("It must be integer.")
        return heart_rate()
    if not 40 < int(val) < 200:
        print("Heart rate must be less than 200 and more than 40.")
        return heart_rate()
    return val


def blushing_level():
    """Here we collect and validate the blushing level"""
    val = input("Please enter the blushing level: ")
    if val == "":
        val = str(randint(1, 6))
    if not val.isdigit():
        print("It must be integer.")
        return blushing_level()
    if int(val) not in [1, 2, 3, 4, 5, 6]:
        print("Blushing level must be in range 1-6.")
        return blushing_level()
    return val


def pupillary_dilation():
    """Here we collect and validate the pupillary dilation"""
    val = input("Please enter the pupillary dilation: ")
    if val == "":
        val = str(randint(2, 8))
    if not val.isdigit():
        print("It must be integer.")
        return pupillary_dilation()
    if not 1 < int(val) < 9:
        print("Pupillary dilation must be less than 9 and more than 1.")
        return pupillary_dilation()
    return val


def get_anamnesis():
    """This function enter values to dict"""
    anamnesis = {}

    anamnesis["respiration"] = respiration()
    anamnesis["heart rate"] = heart_rate()
    anamnesis["blushing level"] = blushing_level()
    anamnesis["pupillary dilation"] = pupillary_dilation()

    return anamnesis
