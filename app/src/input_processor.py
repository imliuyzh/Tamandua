"""This module is responsible for handling inputs from the users and modifying
the data in the DataManager object."""

import user_interface as ui
import data_manager as dm


class InputProcessor:
    """This class will fulfill the 'Controller' part in the
    Modal-View-Controller design pattern."""
    def __init__(self, data_manager: 'DataManager'):
        """Construct the InputProcessor object by initializing all instance
        variables that are necessary to run."""
        self._data_manager = data_manager

    def execute_program(self) -> None:
        """The method that will start the user interface and wait for
        the users' input."""
        ui.UserInterface.emerge()
        course_set = ui.UserInterface.prompt_course_selection()
        self._data_manager.add_courses(course_set)
