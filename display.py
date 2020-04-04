import numpy as np
import os
import time

windows_compatibility_mode = False # Some windows versions may not support colors?
transparentTile = " " # to get a transparent character, type display.transparentTile -- using ASCII alt+255
width = 160
height = 35
__viewports = []

if os.name == "posix":
    os.system("clear")
else: # if the os is windows:
    os.system("windows_display.cmd")
    os.system("cls")

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

def clearViewports():
    for v in __viewports:
        __viewports.remove(v)

def __clearScreen(fast=False):
    # fast is used for when you have to do a lot of calls quickly,
    # like when you are walking around
    # it doesn't clear the screen, so it doesn't ever flicker
    # but if other text gets on the screen accidentally for some reason,
    # that text won't be cleared when fast==True
    if os.name == "posix":
        if fast:
            print("[100A", end="\r")
        else:
            os.system("clear")
    else: # current os is windows
        if fast and not windows_compatibility_mode:
            print("[100A", end="\r")
        else:
            os.system('cls')


def render(fast=False):
    __clearScreen(fast)
    frameBuffer = np.full([height, width], " ")
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

if __name__ == "__main__":
    demo()
