# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:58:50 2020

@author: Kam Look
"""
import numpy as np
#import msvcrt as microsoft
import display as dis
import cliInput

def updatePlayerPos(entityViewport):
    entityViewport.data[Player.ypos][Player.xpos]=Player.icon
    dis.render()

#Tile list
class Player:
    icon='@'
    xpos=0
    ypos=0

def triggerEvent(game, mapName, xPos, yPos, char):
    game.TriggerMapEvent(mapName, xPos, yPos, char)
    
    # while game.mapEvent == True:
    #     print("map")


#read contents of file and put into a list 
def loadRoom(roomFile):
    #must be .txt file, floor1.txt
    file=open(roomFile, 'r')
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
    updatePlayerPos(entityViewport)

    return entityViewport

def split(word):
    return [char for char in word]

def Update(entityViewport, game):
    move=cliInput.getInput()
    if Player.xpos == 2 and Player.ypos == 2:
        triggerEvent(game, 'map1', 2, 2, ' ')
    if move =='up':
        entityViewport.data[Player.ypos][Player.xpos] = ' '
        Player.ypos -= 1
        updatePlayerPos(entityViewport)

    if move == 'down':
        entityViewport.data[Player.ypos][Player.xpos] = ' '
        Player.ypos += 1
        updatePlayerPos(entityViewport)

    if move == 'right':
        entityViewport.data[Player.ypos][Player.xpos] = ' '
        Player.xpos += 1
        updatePlayerPos(entityViewport)

    if move == 'left':
        entityViewport.data[Player.ypos][Player.xpos] = ' '
        Player.xpos -= 1
        updatePlayerPos(entityViewport)

    if move == 'quit':
        exit(0)
