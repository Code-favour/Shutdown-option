# Shutdown-option
This is a Python code that allows you to either shutdown or restart your computer depending on the user’s input
The code imports two modules: os and platform. The os module provides a way of using operating system dependent
functionality like reading or writing to the file system. The platform module provides an interface to various 
services that interact with the operating system.

The code defines two functions: shutdown() and restart(). The shutdown() function checks if the operating system is Windows,
Linux or Darwin (MacOS) and then executes the appropriate command to shutdown the computer. The restart() function does the same thing but for restarting the computer.


The os.system() function is used to execute a command in the shell. In this case, the command is “shutdown -t 0 -r -f”.

The -t 0 option specifies the time-out period before shutdown or restart to be 0 seconds. The -r option specifies that the computer should be restarted after shutdown. The -f option specifies that any running applications should be forced to close immediately.

So, the command “shutdown -t 0 -r -f” will immediately shutdown and restart the computer without any time-out period and force any running applications to close.

The input() function is used to get input from the user. In this case, the prompt "Use ‘r’ for restart and ‘s’ for shutdown: " is displayed to the user and the user is expected to enter either ‘r’ or ‘s’.

The input is then stored in the variable command. The code then checks if the value of command is ‘r’ or ‘s’ and calls the appropriate function (restart() or shutdown()) based on the value of command

The code then prompts the user to enter either ‘r’ for restart or ‘s’ for shutdown. If the user enters ‘r’, it calls the restart() function. If the user enters ‘s’, it calls the shutdown() function. If the user enters anything else, it prints “Wrong letter Input try again”.
