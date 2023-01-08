"""
This file can be imported as a module. It contains a class for validate and
represent person condition and function that randomly choose and return
the answer for questions.

This script requires that `pydantic` and 'random' be installed within the
Python environment you are running this script in.
"""

from pydantic import BaseModel, validator
from random import randint


class Anamnesis(BaseModel):
    """
    A class used to validate and represent person condition

    ...

    Attributes
    ----------
    respiration : int
        interger to track respiration bpm
    heart_rate: int
        interger to track heart rate
    blushing_level: int
        interger to track blushing level (1-6)
    pupillary_dilation: int
        interger to track pupillary dilation (2-8)

    Methods
    -------
    resp_must_be()
        validate inputed value
    hr_must_be()
        validate inputed value
    bl_must_be()
        validate inputed value
    pd_must_be
        validate inputed value
    """
    respiration: int = None
    heart_rate: int = None
    blushing_level: int = None
    pupillary_dilation: int = None

    @validator('respiration')
    def resp_must_be(cls, resp):
        """
        Check respiration

        Parameters
        ----------
        cls : class
            this class
        resp: int
            respiration value

        Raises
        ------
        Value Error
            If respiration more than human can.
        """
        if resp > 20:
            raise ValueError("Invalid respiration.\
                Should be less than 20")
        if resp < 12 or resp > 16:
            print("\nWARNING: Person respiration unexpectable.\n")
        return resp

    @validator('heart_rate')
    def hr_must_be(cls, hr):
        """
        Check heart rate

        Parameters
        ----------
        cls : class
            this class
        hr: int
            heart rate value

        Raises
        ------
        Value Error
            If heart rate more or less than human heart can.
        """
        if not 40 <= hr <= 200:
            raise ValueError("Invalid heart rate.\
                Should be more than 40 and less than 200")
        if hr < 60 or hr > 100:
            print("\nWARNING: Person heart rate unexpectable.\n")
        return hr

    @validator('blushing_level')
    def bl_must_be(cls, bl):
        """
        Check blushing level

        Parameters
        ----------
        cls : class
            this class
        bl: int
            blushing level value

        Raises
        ------
        Value Error
            If blushing level not in 1-6
        """
        if bl not in [1, 2, 3, 4, 5, 6]:
            raise ValueError("Invalid blushing level.\
                Should be in 1-6")
        if bl in [4, 5, 6]:
            print("\nWARNING: Person blushing level unexpectable.\n")
        return bl

    @validator('pupillary_dilation')
    def pd_must_be(cls, pd):
        """
        Check pupillary dilation

        Parameters
        ----------
        cls : class
            this class
        pd: int
            pupillary dilation value

        Raises
        ------
        Value Error
            If pupillary dilation more or less than exist
        """
        if not 2 <= pd <= 9:
            raise ValueError("Invalid pupillary dilation.\
                Should be more than 2 and less than 9")
        if pd < 4 or pd > 6:
            print("\nWARNING: Person pupillary dilation unexpectable.\n")
        return pd


def get_answer(question):
    """
    This function randomly choose the answer for inputed question

    ...
    Parameters
    ----------
    question : str
        contains the question
    """
    if (question == "Are you living with your parents?" or
            question == "Do you work?"):
        return randint(1, 3)
    return randint(1, 4)
