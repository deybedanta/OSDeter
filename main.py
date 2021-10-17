import platform
import os
import time

splash = """

  ______        _______. _______   _______ .___________. _______ .______      
 /  __  \      /       ||       \ |   ____||           ||   ____||   _  \     
|  |  |  |    |   (----`|  .--.  ||  |__   `---|  |----`|  |__   |  |_)  |    
|  |  |  |     \   \    |  |  |  ||   __|      |  |     |   __|  |      /     
|  `--'  | .----)   |   |  '--'  ||  |____     |  |     |  |____ |  |\  \----.
 \______/  |_______/    |_______/ |_______|    |__|     |_______|| _| `._____|
                                                                              

"""

windows = """

                 __
            ,-~Â¨^  ^Â¨-,           _,
           /          / ;^-._...,Â¨/
          /          / /         /
         /          / /         /
        /          / /         /
       /,.-:''-,_ / /         /
       _,.-:--._ ^ ^:-._ __../
     /^         / /Â¨:.._Â¨__.;
    /          / /      ^  /
   /          / /         /
  /          / /         /
 /_,.--:^-._/ /         /
^            ^Â¨Â¨-.___.:^

"""

darwin = """

                        .8 
                      .888
                    .8888'
                   .8888'
                   888'
                   8'
      .88888888888. .88888888888.
   .8888888888888888888888888888888.
 .8888888888888888888888888888888888.
.&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
`@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
 `00000000000000000000000000000000000'
  `000000000000000000000000000000000'
   `0000000000000000000000000000000'
     `###########################'
       `#######################'
         `#########''########'
           `#####'  `#### 

"""

linux = """

         _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' 

"""


def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Darwin':
        os.system('clear')

def begin():

    print(splash)
    print("")
    print("")
    print("Welcome to OSDeter. This program detects your Operating System and prints it out to you. Please type in 'd' to determine your OS. [Made by Bedanta Dey]")

    global inp  

    inp = input('> ')
    clear()

    if inp == 'd':
        deter()
    else:
        print('ERROR: Bad Input. Ending program in 3 seconds...')
        time.sleep(3)
        exit()

def deter():
    print("Please wait... determining your Operating System...")
    time.sleep(3)
    
    if platform.system() == 'Windows':
        print(windows)
        print("Your Operating System is detected to be WINDOWS.")
        print("")
        print("")
        print("Exiting program in 5 seconds...")
        time.sleep(5)
        exit()
    elif platform.system() == 'Darwin':
        print(darwin)
        print("Your Operating System is detected to be MACOS.")
        print("")
        print("")
        print("Exiting program in 5 seconds...")
        time.sleep(5)
        exit()
    elif platform.system() == 'Linux':
        print(linux)
        print("Your Operating System is detected to be LINUX.")
        print("")
        print("")
        print("Exiting program in 5 seconds...")
        time.sleep(5)
        exit()
    else:
        print("Could not detect your Operating System. This program cannot be run on this machine.")
        print("")
        print("")
        print("Exiting program in 5 seconds...")
        time.sleep(5)
        exit()

clear()
begin()



