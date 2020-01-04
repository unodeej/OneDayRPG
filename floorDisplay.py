# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:58:50 2020

@author: Kam Look
"""
import numpy as np
import msvcrt as microsoft
import display as dis

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
        return 'quit'

def updatePlayerPos():
    entityViewport.data[Player.ypos][Player.xpos]=Player.icon
    dis.render()
    
#Tile list
class Player:
    icon='@'
    xpos=0
    ypos=0
    
def split(word): 
    return [char for char in word]  

#read contents of file and put into a list 
file=open('floor1.txt', 'r')
floorDisplay=file.readlines().copy()
file.close()

#remove white space 

floorDisplay[:] = [row.strip('\n') for row in floorDisplay]
floorDisplay[:] = [row.strip('\t') for row in floorDisplay]
floorDisplay[:] = [split(row) for row in floorDisplay]
originalFloor=floorDisplay
#initialize transparent layer for entities
entityArray= np.full_like(floorDisplay, ' ')

floorViewport=dis.addViewport(0,0,floorDisplay)
entityViewport=dis.addViewport(0,0,entityArray, z=-1)
updatePlayerPos()

while True:
    move=getInput()
    if move =='up':
        entityViewport.data[Player.ypos][Player.xpos] = ' '
        Player.ypos -= 1
        updatePlayerPos()
        
    if move == 'down':
        entityViewport.data[Player.ypos][Player.xpos] = ' '
        Player.ypos += 1
        updatePlayerPos()
        
    if move == 'right':
        entityViewport.data[Player.ypos][Player.xpos] = ' '
        Player.xpos += 1
        updatePlayerPos()
        
    if move == 'left':
        entityViewport.data[Player.ypos][Player.xpos] = ' '
        Player.xpos -= 1
        updatePlayerPos()
    
    if move == 'quit':
        exit(0)


