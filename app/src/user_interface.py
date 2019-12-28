"""This module shows the user interface of this program."""

import re
import time


class UserInterface:
    """A class of various static methods that are responsible for showing
    messages and asking for inputs."""

    def emerge(self) -> None:
        """Show the welcome wizard messages when the program starts."""
        print("""       _.---._""")
        print("""    .\/'       "--`\/\/           888888    db    8b    """ \
              + """d8    db    88b 88 8888b.  88   88    db""")
        print("""  ./                 \ \            88     dPYb   88b  """ \
              + "d88   dPYb   88Yb88  8I  Yb 88   88   dPYb")
        print(""" /./\  )______   \__  \ \           88    dP__Yb  88YbdP88""" \
              + """  dP__Yb  88 Y88  8I  dY Y8   8P  dP__Yb""")
        print("""""""""./  / /\ \   | \ \  \  \_\          88   """"""""" \
              + """""""""dP\"\"\"\"Yb 88 YY 88 dP\"\"\"\"Yb 88  Y8 """"""""" \
              + """""""""8888Y\"  `YbodP' dP\"\"\"\"Yb""""""""")
        print("""   / /  \ \  | |\ \  \ """ + "\n")

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
                    + "code of the classes you want (separate them by " \
                    + "space): ").split())
                for course_code in course_set:
                    assert course_code.isnumeric() == True
            except AssertionError:
                print(f"[{time.asctime()}] Check your input. Please try again.")
            else:
                return course_set

    @staticmethod
    def show_message(message: str) -> None:
        '''Let other classes print their messages in the user interface.'''
        print(message)
