import msvcrt as microsoft

def getInput():
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
