# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:58:50 2020

@author: Kam Look
"""
import numpy as np
#import msvcrt as microsoft
import display as dis
import cliInput
#Tile list

class Player:
    icon='@'
    xpos=1
    ypos=1


def triggerEvent(game, mapName, xPos, yPos, char):
    game.TriggerMapEvent(mapName, xPos, yPos, char)
    
    # while game.mapEvent == True:
    #     print("map")

def split(word):
    return [char for char in word]

class Room:
    solids= ['|','+','=','-'] 
    canMove = True
    def updatePlayerPos(self):
        self.entityViewport.data[Player.ypos][Player.xpos]=Player.icon
        dis.render()
    #read contents of file and put into a list 
    def loadRoom(self,roomFile):
        #must be .txt file, floor1.txt
        file=open(roomFile, 'r')
        floorDisplay=file.readlines().copy()
        file.close()
    
        #remove white space
        floorDisplay[:] = [row.strip('\n') for row in floorDisplay]
        floorDisplay[:] = [row.strip('\t') for row in floorDisplay]
        floorDisplay[:] = [split(row) for row in floorDisplay]
        #initialize transparent layer for entities
        entityArray= np.full_like(floorDisplay, ' ')
    
        self.floorViewport=dis.addViewport(0,0,floorDisplay)
        self.entityViewport=dis.addViewport(0,0,entityArray,z =-1)
        self.updatePlayerPos()
    
        return self.entityViewport
    
    def Update(self):
        move=cliInput.getInput()
        if move =='up':
            newPos= Player.ypos -1
            self.CheckTile(newPos, Player.xpos, self.floorViewport.data[newPos][Player.xpos])
            if self.canMove == True:
                self.entityViewport.data[Player.ypos][Player.xpos] = ' '
                Player.ypos = newPos
                self.updatePlayerPos()
    
        if move == 'down':
            newPos=Player.ypos +1
            self.CheckTile(newPos, Player.xpos, self.floorViewport.data[newPos][Player.xpos])
            if self.canMove == True:
                self.entityViewport.data[Player.ypos][Player.xpos] = ' '
                Player.ypos = newPos
                self.updatePlayerPos()
    
        if move == 'right':
            newPos=Player.xpos +1
            self.CheckTile(Player.ypos, newPos, self.floorViewport.data[Player.ypos][newPos])
            if self.canMove == True:
                self.entityViewport.data[Player.ypos][Player.xpos] = ' '
                Player.xpos = newPos
                self.updatePlayerPos()
    
        if move == 'left':
            newPos= Player.xpos -1
            self.CheckTile(Player.ypos, newPos, self.floorViewport.data[Player.ypos][newPos])
            if self.canMove == True:
                self.entityViewport.data[Player.ypos][Player.xpos] = ' '
                Player.xpos = newPos
                self.updatePlayerPos()
    
        if move == 'quit':
            exit(0)
    def CheckTile(self, newYPos, newXPos, icon):
        if icon in self.solids:
            self.canMove=False
        elif 2<=newYPos<=3 and 2<=newXPos<=3:
            self.canMove=False, print('The bed DOES look enticing, but you are late :(') #triggerAction()
        
        elif 1<=newYPos<=4 and 17<=newXPos<=21:
            self.canMove=False, print('Your desk is cluttered, but you can clean it later...') #triggerAction()
        elif newYPos==7 and newXPos == 33:
            self.canMove=False, print("You can't go to school without your backpack!") #triggerAction()
        else: 
            self.canMove=True

room = Room()
