"""This module is responsible for handling inputs from the users and modifying
the data in the DataManager object."""

from re import match
from time import asctime
import preset
import user_interface as ui


TERM_DICT = {"FALL": "92", "WINTER": "03", "SPRING": "14"}

class InputProcessor:
    """This class will fulfill the 'Controller' part in the
    Modal-View-Controller design pattern."""

    def __init__(self, user_interface: 'UserInterface',
                 data_manager: 'DataManager'):
        """Construct an instance of the InputProcessor class by initializing
        all instance variables that are necessary to run."""
        self._user_interface, self._data_manager = user_interface, data_manager

    def execute_program(self) -> None:
        """Start the user interface and wait for the users' input."""
        try:
            self._user_interface.emerge()
            year_term, course_set = self._initialize_data()
            self._data_manager.set_year(year_term)
            self._data_manager.set_courses(course_set)
            self._data_manager.check_availbility()
        except KeyboardInterrupt:
            ui.UserInterface.show_message(f"[{asctime()}] " \
                + "Program exits now. Thank you for using Tamandua.")

    def _initialize_data(self) -> (str, set):
        """Return user-defined input data in the file preset.py or ask users to
        give one."""
        ui.UserInterface.show_message(f"[{asctime()}] Checking existing "
                                      + "settings in the file preset.py...")
        year_term, course_set = None, None
        try:
            year_term = InputProcessor.check_year_term_input(
                preset.YEAR_TERM.upper())
            course_set = InputProcessor._check_course_set_input(
                preset.COURSE_SET)
        except (AssertionError, TypeError, AttributeError):
            year_term = self._user_interface.prompt_year_term()
            course_set = self._user_interface.prompt_course_selection()
        return (year_term, course_set)

    @staticmethod
    def check_year_term_input(data: str) -> str:
        """See if the format for the year term is correct."""
        assert match(r"^(\d{4}) (FALL|WINTER|SPRING){1}$", data) is not None
        return f"{data[0:4]}-{TERM_DICT[data[5:]]}"

    @staticmethod
    def check_course_numbers_input(data: str) -> set:
        """Check the correctness of the format for the course numbers."""
        assert match(r"\d{5}", data) is not None
        return InputProcessor._check_course_set_input(set(data.split()))

    @staticmethod
    def _check_course_set_input(test_set: set) -> set:
        """Check the correctness of the format for the course set."""
        for course_code in test_set:
            assert course_code.isnumeric() == True and len(course_code) == 5
        return test_set
