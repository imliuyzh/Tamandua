"""This module shows the user interface of this program."""


class UserInterface:
    @staticmethod
    def emerge() -> None:
        print(f'''
                   _.---._   
                ./'       "--`\//           888888    db    8b    d8    db    88b 88 8888b.  88   88    db    
              ./                 \ \          88     dPYb   88b  d88   dPYb   88Yb88  8I  Yb 88   88   dPYb   
             /./\  )______   \__  \ \         88    dP__Yb  88YbdP88  dP__Yb  88 Y88  8I  dY Y8   8P  dP__Yb  
            ./  / /\ \   | \ \  \  \_\        88   dP""""Yb 88 YY 88 dP""""Yb 88  Y8 8888Y"  `YbodP' dP""""Yb   
               / /  \ \  | |\ \  \ 
        ''')

    @staticmethod
    def prompt_course_selection() -> set:
        unformatted_input = input("Type the course code of the classes you \
            want (separate them by space)")
        formatted_input = unformatted_input.split()

        while True:
            try:
                course_set = set(int(course_code) for course_code
                    in formatted_input)
            except ValueError:
                print("Invalid input. Please try again.")
            else:
                return course_set
