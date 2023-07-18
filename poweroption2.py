#import os
import os
import platform

def shutdown():
    if platform.system() == "Windows":
        os.system('shutdown -s')
    elif platform.system() == "Linux" or platform.system() == "Darwin": #MacOS
        os.system("shutdown -h now")
    else:
        print("Os not supported!")

def restart():
    if platform.system() == "Windows":
        os.system("shutdown -t 0 -r -f")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('reboot now')
    else:
        print("Os not supported!")


command = input("Use \'r\' for restart and \'s\' for shutdown: ").lower()

if command == "r":
    restart()
elif command == "s":
    shutdown()
else:
    print("Wrong letter Input try again:")

    
#The code defines two functions: shutdown() and restart(). 
# The shutdown() function checks if the operating system is Windows,
#  Linux or Darwin (MacOS) and then executes the appropriate command to 
# shutdown the computer. The restart() function does the same thing
#  but for restarting the computer.

