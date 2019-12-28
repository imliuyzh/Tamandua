"""This module is responsible for handling inputs from the users and modifying
the data in the DataManager object."""

import time
import user_interface as ui


class InputProcessor:
    """This class will fulfill the 'Controller' part in the
    Modal-View-Controller design pattern."""

    def __init__(self, user_interface: 'UserInterface',
                 data_manager: 'DataManager'):
        """Construct an InputProcessor object by initializing all instance
        variables that are necessary to run."""
        self._user_interface = user_interface
        self._data_manager = data_manager

    def execute_program(self) -> None:
        """The method that will start the user interface and wait for
        the users' input."""
        try:
            self._user_interface.emerge()
            year_term = self._user_interface.prompt_year_term()
            self._data_manager.set_year(year_term)
            course_set = self._user_interface.prompt_course_selection()
            self._data_manager.set_courses(course_set)
            self._data_manager.check_availbility()
        except KeyboardInterrupt:
            ui.UserInterface.show_message(f"[{time.asctime()}] " \
                + "Program exits now. Thank you for using Tamandua.")
