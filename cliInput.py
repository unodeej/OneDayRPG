import os
import signal

if (os.name == 'posix'):
    import tty
    import sys
    import termios
    new = termios.tcgetattr(sys.stdin)
    new[3] &= ~termios.ECHO # turn off ECHO flag (don't show any characters that were typed)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new) # apply the above change to the terminal
    tty.setcbreak(sys.stdin) # set terminal to accept input one character at a time
else: # current os is windows
    import msvcrt as microsoft

def cleanUp(a, b):
    if (os.name == 'posix'):
        new = termios.tcgetattr(sys.stdin)
        new[3] |= termios.ECHO # turn off ECHO flag (don't show any characters that were typed)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, new)
    print("bye")
    quit()
signal.signal(signal.SIGINT, cleanUp)

def getInput():
    if (os.name == 'posix'):
        nextInput = sys.stdin.read(1)[0] # get next character for posix
    else: # current os is windows
        nextInput = microsoft.getwch() # get next character for windows

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
        cleanUp(0,0);
