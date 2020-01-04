import numpy as np
import os
import time

transparentTile = " " # to get a transparent character, type display.transparent
displayWidth = 160
displayHeight = 35
__viewports = []

class Viewport:
    def __init__(self, x, y, data, z=0):
        self.x = x;
        self.y = y;
        self.data = np.asarray(data);
        self.z = z;

    def replaceData(self, data):
        self.data = np.asarray(data);

    def renderTo(self, buffer):
        bufferSlice = buffer[self.y:self.y + self.data.shape[0], self.x: self.x + self.data.shape[1]:]
        buffer[self.y:self.y + self.data.shape[0], self.x: self.x + self.data.shape[1]:] = np.where(self.data == transparentTile, bufferSlice, self.data)

def addViewport(x, y, data, z=0):
    newViewport = Viewport(x, y, data, z)
    __viewports.append(newViewport)
    __viewports.sort(key = lambda vp: vp.z, reverse = True)
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
    frameBuffer = np.full([displayHeight, displayWidth], " ")
    for viewport in __viewports:
        viewport.renderTo(frameBuffer)
    for row in frameBuffer:
        for point in row:
            print(point, end = "")
        print()

def demo():
    # square = addViewport(10, 0, np.ones([10,20]))
    square = addViewport(10, 0, [['|', ' ', ' ', ' ', '|', transparentTile, transparentTile, transparentTile, '|'] * 3] * 10)
    render()
    for i in range(20):
        square.x += 1
        square.y += 1
        time.sleep(.1)
        render()
