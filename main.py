"""
This is a start point.
"""
from files.processor import testing
from files.pars import parsing
from time import sleep


def preprocessing():
    """Here we get name of particiant"""
    name = input("Please, enter your name: ")
    if name == "":
        name = "Unknown"
    with open("./json/history.json", "a") as write_file:
        write_file.write("\n")
        write_file.write("[")
        write_file.write(name)
        write_file.write("]")
        write_file.write("\n")


def main():
    """Greetings, options, parsing and start working.

        ...
        Parameters
        ----------
        choice: str
            contain user answer
        qa: dict
            contain questions and answers

    """
    print("\nWELCOME to Voight-Kampff 3000!")

    while 1:
        choice = input("Choose option (TEST or EXIT):")
        if choice == "TEST" or choice == "test":
            preprocessing()
            print("\nProcessing...")
            sleep(0.5)
            print("Test started!")

            qa = parsing()
            testing(qa)
        elif choice == "EXIT" or choice == "exit":
            break


if __name__ == "__main__":
    main()
