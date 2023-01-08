"""
This file contains main function. This is a start of programm.
"""

from time import sleep
from tests.testing_person import testing


def main():
    """
    Infinity loop for restart test after previos iteration.
    Choice for user and a little joke about old computers.

    ...
    Parameters
    ----------
    choice: str
        contain user answer
    """
    while True:
        choice = input("Choose option (TEST or EXIT):")
        if choice == "TEST" or choice == "test":
            print("\nPreprocessing...")
            sleep(1)
            print("Processing...")
            sleep(1)
            print("Person prepared...")
            sleep(1)
            print("Test started!")

            print("\nResponding subject is", testing(), '\n')
        elif choice == "EXIT" or choice == "exit":
            break


if __name__ == "__main__":
    main()
