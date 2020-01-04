# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:58:50 2020

@author: Kam Look
"""
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
originalFloor=floorDisplay
floorDisplay[:] = [row.strip('\n') for row in floorDisplay]
floorDisplay[:] = [row.strip('\t') for row in floorDisplay]
floorDisplay[:] = [split(row) for row in floorDisplay]

floorViewport=dis.addViewport(0,0,floorDisplay)
dis.render()

playerViewport= dis.addViewport(Player.xpos,Player.ypos, Player.icon,z= -1)

while True:
    move=getInput()
    if move =='up':
        playerViewport.y -= 1
        dis.render()
        
    if move == 'down':
        playerViewport.y += 1
        dis.render()
        
    if move == 'right':
        playerViewport.x += 1
        dis.render()
        
    if move == 'left':
        playerViewport.x -= 1
        dis.render()
    
    if move == 'quit':
        exit(0)

