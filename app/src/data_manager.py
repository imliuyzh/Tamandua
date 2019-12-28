"""This module contains the core mechanism for Tamandua. In other words, it
shows how Tamandua really works in the background."""

import time
import random
import urllib.error
import urllib.request
import user_interface


class DataManager:
    """This class is responsible for monitoring the classes and store all the
    user inputs that are necessary for this program to work."""

    def __init__(self):
        '''Construct a DataManager object by initializing necessary
        instance variables.'''
        self._course_set = None
        self._year_term = None
        self._class_notification_status = dict()

    def set_year(self, year_term: str) -> None:
        '''Make clear that which quarter does the users want to look for.'''
        self._year_term = year_term

    def set_courses(self, course_set: set) -> None:
        '''Get the set of courses that the users want to look for.'''
        self._course_set = course_set

    def check_availbility(self) -> None:
        '''Check the courses in the course set if they are open or not.'''
        continue_program = True
        request = self._build_request()
        user_interface.UserInterface.show_message(
            f"[{time.asctime()}] Start a request now.")

        while continue_program:
            try:
                with urllib.request.urlopen(request) as response:
                    self._process_class_info(response.read()
                                             .decode()
                                             .splitlines())
            except KeyboardInterrupt:
                user_interface.UserInterface.show_message(
                    f"[{time.asctime()}] Program exits now. Thank you for " \
                        + "using Tamandua, I wish you can get your classes:)")
                continue_program = False
            except urllib.error.HTTPError as error_object:
                user_interface.UserInterface.show_message(
                    f"[{time.asctime()}] Network returns error code: " \
                        + f"{error_object.code}")
                continue_program = False
            finally:
                user_interface.UserInterface.show_message(
                    f"[{time.asctime()}] Stop the process for a moment to " \
                        + "protect the WebSoc server.")
                time.sleep(random.uniform(2, 9))

    def _build_request(self) -> urllib.request.Request:
        '''Create a Request object so that the urlopen() function can use the
        POST method.'''
        parameters = bytes(f"Results&YearTerm={self._year_term}&Breadth=ANY&" \
            + "Dept=+ALL&Division=ANY&ClassType=ALL&FullCourses=ANY&" \
            + "CancelledCourses=Exclude&" \
            + f"CourseCodes={'+'.join(self._course_set)}", 'utf-8')
        return urllib.request.Request("https://www.reg.uci.edu/perl/WebSoc",
                                      data=parameters)

    def _process_class_info(self, data: [str]) -> None:
        pass
