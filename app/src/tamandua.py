"""This module marks the starting point of the program (which means people
should run the program here)."""

import user_interface as ui
import data_manager as dm
import input_processor as ip



if __name__ == "__main__":
    ip.InputProcessor(ui.UserInterface(), dm.DataManager()).execute_program()
