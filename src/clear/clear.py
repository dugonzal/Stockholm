import os
import sys

def clear():
    if sys.platform == "win32"  or sys.platform == "win64":
        os.system("cls") # Clear the terminal
    else:
        os.system('clear') # Clear the terminal
