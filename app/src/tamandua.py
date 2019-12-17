"""This module marks the starting point of the program (which means people
should run the program here)."""

import user_interface as ui
import data_manager as dm
import command_processor as cp


def execute_program() -> None:
    """Initialize all the variables that are necessary to run the user
    interface and prompt the users to enter their class selection."""
    user_interface = ui.UserInterface()
    data_manager = dm.DataManager()
    command_processor = cp.CommandProcessor(user_interface, data_manager)
    command_processor.emerge()



if __name__ == "__main__":
    execute_program()
