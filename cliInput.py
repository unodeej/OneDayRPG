import os

if (os.name == 'posix'):
    import tty
    import sys
else: # current os is windows
    import msvcrt as microsoft

def getInput():
    if (os.name == 'posix'):
        tty.setcbreak(sys.stdin)
        nextInput = sys.stdin.read(1)[0]
    else: # current os is windows
        nextInput = microsoft.getwch()
    if nextInput in "aA":
        return 'left'
    if nextInput in "dD":
        return 'right'
    if nextInput in "wW":
        return 'up'
    if nextInput in "sS":
        return 'down'
    if nextInput in "qQ":
        print("quitting...")
        exit(0);