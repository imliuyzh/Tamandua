<img src="img/logo.png" width="370px">

# Tamandua
This program will notify the student users at the University of California, Irvine (UCI) when the classes they want are open.

## Background
Enrolling classes that students want is often a difficult task in the University of California, Irvine. This is largely due to the server's inability to handle a large number of requests. Numerous tools attempting to register for classes have been created. However, it has shown that usually programs like these can be abused. Recently, there are reports indicate that some students will use these tools to keep making requests that ultimately overloads the server, rendering the server incapable of adding students' classes. Consequently, class registration is not the focus of this project. Instead, this project will focus on class registration **NOTIFICATION**. It will tell the students to get the classes they want once they are open. The method of registering for the classes will be the students' choice. However, I recommend that students should use WebReg as the primary choice of performing this task because it is the legal and official way as specified by the registrar.

There is also another reason behind this project's motivation. Most applications, such as Coursicle, are mobile-focused; in other words, PC devices are not their target. As a result, PC users will face difficulty to automate checking class availability. This tool essentially performs the same task as Coursicle with the exception that it mainly targets PC devices.

### Naming
In the University of California, Irvine, Anteaters are the official mascot representing the school itself. If one can search the meaning of "Tamandua," he or she can find that "Tamandua" is the formal name for a type of anteater. In order to echo the academic background of this project and to avoid others' tendency to name their projects with a prefix such as "Zot" or "Ant," I decided to use "Tamandua" as the name for my work.

## Installation
Since Tamandua is technically still in development, there is no installer like in Windows that you may feel used to (although you can package it using third-party libraries like PyInstaller). Instead, you grab the scripts and run them in a Python environment with dependencies.

### Dependency
+ [Python](https://www.python.org/) (v3.6+)
+ [Pygame](https://www.pygame.org/news)

### Process
1. Download Python
2. Follow this tutorial to set up a virtual environment:
    + [https://www.ics.uci.edu/~thornton/ics32/Notes/ThirdPartyLibraries/](https://www.ics.uci.edu/~thornton/ics32/Notes/ThirdPartyLibraries/)
3. Open the ```src``` folder in the command line and type ```python3 tamandua.py```
    + Note that you can list the classes you want in ```preset.py``` to avoid further typing when the program starts
4. Press ```Ctrl+C``` in the command line if you want to terminate Tamandua

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
You can modify this program to suit your needs. However, please **DO NOT** abuse this program. All consequences resulted from such actions will be on your own. This script **DOES NOT** enroll you into the classes you want, but it instead tells you when you can enroll them.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Credits
- The logo is based on an icon made by Freepik from www.flaticon.com
- UCI seal comes from https://brand.uci.edu/applying-the-brand/digital/
- The "beep" sound effect comes from https://freesound.org/people/AlaskaRobotics/sounds/221087/

<img src="img/uci_seal.jpg" width="70px">
