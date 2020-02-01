"""This module shows the user interface of this program."""

from time import asctime
import input_processor as ip


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
        keep_going = True
        while keep_going:
            try:
                user_input = input(f"[{asctime()}] Enter the year term " \
                    + "(e.g. 2016 FALL): ").upper()
                year_term = ip.InputProcessor.check_year_term_input(user_input)
            except AssertionError:
                print(f"[{asctime()}] ERROR: Please check your input.")
            else:
                keep_going = False
        return year_term

    def prompt_course_selection(self) -> set:
        """Let the users put in the course number for classes that they want
        to be notified once they are open."""
        keep_going = True
        while keep_going:
            try:
                user_input = input(f"[{asctime()}] Type the course " \
                    + "code of the classes you want (separate them by " \
                    + "space): ")
                course_set = \
                    ip.InputProcessor.check_course_numbers_input(user_input)
            except AssertionError:
                print(f"[{asctime()}] Check your input. Please try again.")
            else:
                keep_going = False
        return course_set

    @staticmethod
    def show_message(message: str) -> None:
        """Let other classes print their messages in the user interface."""
        print(message)

    @staticmethod
    def play_sound():
        """Play the beep sound clip using the Pygame library."""
        # Please note that I do not like to put import statements here because
        # it is categorized as a code smell. However, I need this to get rid of
        # the message in the beginning that is forced upon every developer who
        # needs Pygame. On a side note, I am looking to replace Pygame with
        # PySide2 in the future.
        from os import environ
        environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "True"

        import pygame.mixer
        pygame.mixer.init()
        pygame.mixer.music.load("../../media/beep.wav")
        pygame.mixer.music.play()
