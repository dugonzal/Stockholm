import os
import sys

def clear():
    if sys.platform == "win32"  or sys.platform == "win64":
        print('\n' * 100)
    else:
        os.system('clear')
