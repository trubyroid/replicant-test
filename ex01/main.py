"""
This is a start point.
"""
from files.processor import testing
from files.pars import parsing
from time import sleep


def main():
    """Greetings, options, fast 'processing', parsing, working.

        ...
        Parameters
        ----------
        choice: str
            contain user answer
        qa: dict
            contain questions and answers

    """
    print("\nWELCOME to Voight-Kampff 3000!")
    while True:
        choice = input("\nChoose option (TEST or EXIT):")
        if choice == "TEST" or choice == "test":
            print("\nParsing...")
            sleep(0.3)
            print("Processing...")
            sleep(0.3)
            print("Person prepared...")
            sleep(0.3)
            print("Test started!")

            qa = parsing()
            testing(qa)
        elif choice == "EXIT" or choice == "exit":
            break


if __name__ == "__main__":
    main()
