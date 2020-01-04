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
        print("left")
    if nextInput in "dD":
        print("right")
    if nextInput in "wW":
        print("up")
    if nextInput in "sS":
        print("down")
    if nextInput in "qQ":
        print("quitting...")
        exit(0);

while(True):
    getInput()
