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
        """Construct a DataManager object by initializing necessary
        instance variables."""
        self._course_set = None
        self._year_term = None
        self._class_notification_status = None

    def set_year(self, year_term: str) -> None:
        """Make clear that which quarter does the users want to look for."""
        self._year_term = year_term

    def set_courses(self, course_set: set) -> None:
        '''Get the set of courses that the users want to look for.'''
        self._course_set = course_set
        self._class_notification_status = \
            {course: False for course in course_set}

    def check_availbility(self) -> None:
        """Initialize a connection to WebSOC in order to see if the courses in
        the course set are open or not."""
        keep_going = True
        request = self._build_request()
        while keep_going:
            user_interface.UserInterface.show_message(
                f"[{time.asctime()}] Starting a request now. Press Ctrl+C " \
                    + "to terminate the program.")
            try:
                with urllib.request.urlopen(request) as response:
                    self._process_class_info(response.read()
                                             .decode()
                                             .splitlines())
            except urllib.error.HTTPError as error_object:
                user_interface.UserInterface.show_message(
                    f"[{time.asctime()}] Server returns error code: " \
                        + f"{error_object.code}")
                keep_going = False
            except urllib.error.URLError as error_object:
                user_interface.UserInterface.show_message(
                    f"[{time.asctime()}] A network error occurs: " \
                        + f"{error_object.reason}")
                keep_going = False
            finally:
                user_interface.UserInterface.show_message(
                    f"[{time.asctime()}] Stop the process for a moment to " \
                        + "protect the WebSOC server.")
                time.sleep(random.uniform(2, 9))

    def _build_request(self) -> urllib.request.Request:
        """Create a Request object so that the urlopen() function can use the
        POST method."""
        parameters = bytes("Submit=Display+Text+Results&" \
            + f"YearTerm={self._year_term}&Breadth=ANY&" \
            + "Dept=+ALL&Division=ANY&ClassType=ALL&FullCourses=ANY&" \
            + "CancelledCourses=Exclude&" \
            + f"CourseCodes={'+'.join(self._course_set)}", 'utf-8')
        request = urllib.request.Request("https://www.reg.uci.edu/perl/WebSoc",
                                         data=parameters)
        request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) " \
            + "AppleWebKit/537.36 (KHTML, like Gecko) " \
            + "Chrome/79.0.3945.88 Safari/537.36 Edg/79.0.309.56")
        return request

    def _process_class_info(self, data: [str]) -> None:
        """Check which classes are open and notify the users."""
        course_tuple = tuple(self._course_set)
        for line in data:
            current_line = line.strip()
            if current_line.startswith(course_tuple) == True and \
                   self._class_notification_status[current_line[:5]] == False:

                if current_line.endswith("OPEN") == True:
                    user_interface.UserInterface.show_message(
                        f"[{time.asctime()}] {current_line[:5]} IS AVAILABLE. " \
                            + "REGISTER IT RIGHT NOW!")
                    self._class_notification_status[current_line[:5]] = True
                else:
                    self._class_notification_status[current_line[:5]] = False
