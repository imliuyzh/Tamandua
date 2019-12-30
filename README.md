<img src="img/logo.png" width="370px">

# Tamandua
This program will notify the students in the University of California, Irvine (UCI) when the classes they want is open.

## Background
Enrolling classes that the students want is often a difficult task in the University of California, Irvine. This is largely due to the server's inability to handle a large amount of requests. Numerous tools attempt to register for classes have been created. However, it has shown that usually programs like these can be abused. Recently, there are reports indicate that some students will use these tools to keep making requests that ultimately overload the server, rendering the service incapable of adding students' classes. Consequently, class registration is not the focus of this project. Instead, this project will focus on class registration **NOTIFICATION**. It will tell the students to get the classes they want once they are open. The method of registering the classes will be students' choice. However, I recommend that students should use WebReg as the primary choice of performing this task because it is the legal and official way as specified by the registrar.

There is also another reason behind this project's motivation. Most applications, such as Coursicle, are mobile-focused; in other words, PC is not their target. As a result, PC users will face difficulty to automate checking class availability. This tool essentially performs the same task as Coursicle with the exception that both PC and other mobile devices like smartphones are supported.

## Naming
In the University of California, Irvine, Anteaters are the official mascot representing the school itself. If one can search the meaning of "Tamandua," he or she can find that "Tamandua" is the formal name for "Anteater." In order to echo the academic background of this project and to avoid others' tendency to name their projects with prefix such as "Zot" or "Ant," I decided to use "Tamandua" as the name for my work.

## Deployment/"Pseudo-Installation"
### Dependency
+ [Python](https://www.python.org/) (v3.6+)
+ [playsound](https://github.com/TaylorSMarks/playsound)
+ [PySide2](https://www.qt.io/qt-for-python) (Future Development)

### Process
1. Download Python from the link above.
2. Create a Python virtual environment with these tutorials:
    + [https://www.ics.uci.edu/~thornton/ics32/Notes/ThirdPartyLibraries/](https://www.ics.uci.edu/~thornton/ics32/Notes/ThirdPartyLibraries/) (Stop at the ```pip install pygame``` section)
    + [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html) (A bit more complicated to follow)
3. Open the ```Scripts``` folder in the command line and run the ```activate``` script
    + In Windows, you just type ```activate```
    + In Linux (Tested on Ubuntu), you type ```source bin/activate```
    + Sorry, I have no plan to support macOS
4. Type ```pip install playsound```
5. Open the ```src``` folder in the command line and type ```python3 tamandua.py```

## Example Usage
```
       _.---._
    .\/'       "--`\/\/           888888    db    8b    d8    db    88b 88 8888b.  88   88    db
  ./                 \ \            88     dPYb   88b  d88   dPYb   88Yb88  8I  Yb 88   88   dPYb
 /./\  )______   \__  \ \           88    dP__Yb  88YbdP88  dP__Yb  88 Y88  8I  dY Y8   8P  dP__Yb
./  / /\ \   | \ \  \  \_\          88   dP""""Yb 88 YY 88 dP""""Yb 88  Y8 8888Y"  `YbodP' dP""""Yb
   / /  \ \  | |\ \  \ 

[Fri Dec 27 21:49:16 2019] Enter the year term (e.g. 2016 FALL): 2020 WINTER
[Fri Dec 27 21:49:25 2019] Type the course code of the classes you want (separate them by space): 35590 35591
[Fri Dec 27 21:49:31 2019] Starting a request now. Press Ctrl+C to terminate the program.
[Fri Dec 27 21:49:31 2019] Stop the process for a moment to protect the WebSOC server.
[Fri Dec 27 21:49:35 2019] Starting a request now. Press Ctrl+C to terminate the program.
[Fri Dec 27 21:49:35 2019] Stop the process for a moment to protect the WebSOC server.
[Fri Dec 27 21:49:42 2019] Starting a request now. Press Ctrl+C to terminate the program.
[Fri Dec 27 21:49:42 2019] Stop the process for a moment to protect the WebSOC server.
[Fri Dec 27 21:49:47 2019] Starting a request now. Press Ctrl+C to terminate the program.
[Fri Dec 27 21:49:47 2019] Stop the process for a moment to protect the WebSOC server.
[Fri Dec 27 21:49:52 2019] Starting a request now. Press Ctrl+C to terminate the program.
[Fri Dec 27 21:49:53 2019] Stop the process for a moment to protect the WebSOC server.
[Fri Dec 27 21:49:55 2019] Starting a request now. Press Ctrl+C to terminate the program.
[Fri Dec 27 21:49:55 2019] Stop the process for a moment to protect the WebSOC server.
[Fri Dec 27 21:49:59 2019] Starting a request now. Press Ctrl+C to terminate the program.
[Fri Dec 27 21:49:59 2019] Stop the process for a moment to protect the WebSOC server.
[Fri Dec 27 21:50:07 2019] Program exits now. Thank you for using Tamandua.
```
```
       _.---._
    .\/'       "--`\/\/           888888    db    8b    d8    db    88b 88 8888b.  88   88    db
  ./                 \ \            88     dPYb   88b  d88   dPYb   88Yb88  8I  Yb 88   88   dPYb
 /./\  )______   \__  \ \           88    dP__Yb  88YbdP88  dP__Yb  88 Y88  8I  dY Y8   8P  dP__Yb
./  / /\ \   | \ \  \  \_\          88   dP""""Yb 88 YY 88 dP""""Yb 88  Y8 8888Y"  `YbodP' dP""""Yb
   / /  \ \  | |\ \  \ 

[Fri Dec 27 21:51:58 2019] Enter the year term (e.g. 2016 FALL): 2020 WINTER
[Fri Dec 27 21:52:01 2019] Type the course code of the classes you want (separate them by space): 21520
[Fri Dec 27 21:52:03 2019] Starting a request now. Press Ctrl+C to terminate the program.
[Fri Dec 27 21:52:03 2019] 21520 IS AVAILABLE. REGISTER IT RIGHT NOW!
[Fri Dec 27 21:52:03 2019] Stop the process for a moment to protect the WebSOC server.
[Fri Dec 27 21:52:06 2019] Starting a request now. Press Ctrl+C to terminate the program.
[Fri Dec 27 21:52:07 2019] Stop the process for a moment to protect the WebSOC server.
[Fri Dec 27 21:52:14 2019] Program exits now. Thank you for using Tamandua.
```

## Disclaimer
You can definitely modify this program to suit your needs. However, please **DO NOT** abuse this program. All consequences resulted from such actions will be on your own. This script **DOES NOT** enroll you into the classes you want, but instead telling you when you can enroll them.

## License
This project is licensed under the GNU License - see the LICENSE.md file for details.

## Credits
- The logo is based on an icon made by Freepik from www.flaticon.com
- UCI seal comes from https://brand.uci.edu/applying-the-brand/digital/
- The "beep" sound effect comes from https://freesound.org/people/AlaskaRobotics/sounds/221087/
- Alex Thornton (Without his ICS 32 class, I cannot formally step into the world of programming)
- Richard Pattis (Without his ICS 33 class, I cannot gain a solid exposure on various programming concepts)

<img src="img/uci_seal.jpg" width="70px">
