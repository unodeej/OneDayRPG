import msvcrt as microsoft

def getInput():
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