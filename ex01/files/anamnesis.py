def respiration():
    val = input("Please enter the respiration bpm: ")
    if not val.isdigit():
        print("It must be integer.")
        return respiration()
    if not 10 < int(val) < 30:
        print("Respiration bpm must be less than 30 and more than 10.")
        return respiration()
    return val


def heart_rate():
    val = input("Please enter the heart bpm: ")
    if not val.isdigit():
        print("It must be integer.")
        return heart_rate()
    if int(val) < 40 or int(val) > 200:
        print("Heart rate must be less than 200 and more than 40.")
        return heart_rate()
    return val


def blushing_level():
    val = input("Please enter the blushing level: ")
    if not val.isdigit():
        print("It must be integer.")
        return blushing_level()
    if int(val) not in [1, 2, 3, 4, 5, 6]:
        print("Blushing level must be in range 1-6.")
        return blushing_level()
    return val


def pupillary_dilation():
    val = input("Please enter the pupillary dilation: ")
    if not val.isdigit():
        print("It must be integer.")
        return pupillary_dilation()
    if int(val) < 2 or int(val) > 8:
        print("Pupillary dilation must be less than 8 and more than 2.")
        return pupillary_dilation()
    return val


def get_anamnesis():
    anamnesis = {}

    anamnesis["respiration"] = respiration()
    anamnesis["heart rate"] = heart_rate()
    anamnesis["blushing level"] = blushing_level()
    anamnesis["pupillary dilation"] = pupillary_dilation()

    return anamnesis
