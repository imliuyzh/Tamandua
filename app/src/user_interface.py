"""This module shows the user interface of this program."""

import re
import time


class UserInterface:
    """A class of various static methods that are responsible for showing
    messages and asking for inputs."""

    def emerge(self) -> None:
        """Show the welcome wizard messages when the program starts."""
        print("W E L C O M E  T O  T A M A N D U A!")
        print("-----------------------------------------")
        print("Type in the information as the prompt tells you will help " \
            + "you to set up the program. Also, please BE CAREFUL DO NOT " \
            + "TYPE ANYTHING EXTRA SUCH AS SPACES ALONG WITH YOUR INPUT.\n")
        print("DISCLAIMER: You can definitely modify this script to suit " \
            + "your needs. However, please DO NOT abuse this program. All " \
            + "consequences resulted from such actions will be handled on " \
            + "your own. This script DOES NOT enroll you into the classes " \
            + "you want, but instead telling you when you can enroll them.\n")

    def prompt_year_term(self) -> str:
        """Ask the users on which quarter does the classes belong to."""
        term_dict = {"FALL": "92", "WINTER": "03", "SPRING": "14"}
        keep_going = True
        while keep_going:
            try:
                user_input = input(f"[{time.asctime()}] Enter the year term " \
                    + "(e.g. 2016 FALL): ").upper()
                assert re.match(r'^(\d{4}) (FALL|WINTER|SPRING){1}$',
                                user_input) is not None
            except AssertionError:
                print(f"[{time.asctime()}] ERROR: Please check your input.")
            except KeyboardInterrupt:
                print(f"[{time.asctime()}] Program exits now. Thank you for " \
                    + "using Tamandua.")
                keep_going = False
            else:
                keep_going = False

        return f"{user_input[0:4]}-{term_dict[user_input[5:]]}"

    def prompt_course_selection(self) -> set:
        """Let the users put in the course number for classes that they want
        to be notified once they are open."""
        keep_going = True
        while keep_going:
            try:
                course_set = set(input(f"[{time.asctime()}] Type the course " \
                    + " code of the classes you want (separate them by " \
                    + "space): ").split())
                for course_code in course_set:
                    assert course_code.isnumeric() == True
            except AssertionError:
                print(f"[{time.asctime()}] Check your input. Please try again.")
            except KeyboardInterrupt:
                print(f"[{time.asctime()}] Program exits now. Thank you for " \
                    + "using Tamandua.")
                keep_going = False
            else:
                return course_set

    @staticmethod
    def show_message(message: str) -> None:
        '''Let other classes print their messages in the user interface.'''
        print(message)
