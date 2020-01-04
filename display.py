import numpy as np
import os
import time

displayWidth = 100
displayHeight = 30
__viewports = []

class Viewport:
    def __init__(self, x, y, data, z=0):
        self.x = x;
        self.y = y;
        self.data = np.asarray(data);
        self.z = z;

    def renderTo(self, buffer):
        buffer[self.y:self.y + self.data.shape[0], self.x: self.x + self.data.shape[1]:] = self.data

def addViewport(x, y, data, z=0):
    newViewport = Viewport(x, y, data, z)
    __viewports.append(newViewport)
    __viewports.sort(key = lambda vp: vp.z)
    return newViewport

def removeViewport(viewport):
    return __viewports.remove(viewport)

def __clearScreen():
    if os.name == "posix":
        os.system('clear')
    else: # current os is windows
        os.system('cls')

def render():
    __clearScreen()
    frameBuffer = np.full([displayHeight, displayWidth], ".")
    for viewport in __viewports:
        viewport.renderTo(frameBuffer)
    for row in frameBuffer:
        for point in row:
            print(point, end = "")
        print()

def demo():
    square = addViewport(10, 0, np.ones([10,20]))
    render()
    for i in range(20):
        square.x += 1
        square.y += 1
        time.sleep(.1)
        render()
