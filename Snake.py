# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:12:40 2019

@author: seand
"""

"""
Integers:
    
Diff = difficulty setting
Diff = 0 (easy)

Move = Right(0),Up(1),Left(2),Down(3)
    Move = 0
    
Score = Score of game, up by one
    Score = 0




Lists, Integers and strings:
    
Highscore = 2D list of all highscores, easy, medium, and hard
    2nd level list comprises of 3 digit string for name, and Integer for score
Highscore=[[],[],[]]


Lists, Integers:
    
Snake_Body = 2D list comprising of past positions of snake head
    1st level list comprises of index of position, while 2nd level comprises of X Y coord
Snake_Body = []

Snake_Head = 1D list comprising of head's position, used to references wheter Snake_Head is in Snake_Body (Death)
Snake_Head = []

Apple = 1D list comprising of X Y coord of apple
"""

from time import sleep
from Snake import *



def Main_Menu():
    
    selection = 0
    
    while 1:
        #Display
            #Snake
            #Play Game
            #Highscores
            #By Sean Drover and Martha King
            
        if ("JOYSTICK READ" == "down" or "JOYSTICK READ" == "UP")  and selection == 0:
            selection=1
        if ("JOYSTICK READ" == "down" or "JOYSTICK READ" == "UP")  and selection == 1:
            selection=0
            
        if "BUTTON READ" == True and selection == 0:
            Highscore()
        if "BUTTON READ" == True and selection == 1:
            Play_Game()
            
        if "BUTTON READ" == False and selection == 0:
            #Highlight selection "Highscores"
        if "BUTTON READ" == False and selection == 1:
            #Highlight selection "Play Game" 
            
        sleep(0.1)
    
    #Basic menu
    #Select    Highscore() / Play_Game()

def Highscore():
    
    selection = 0
    
    while 1:
        
        if "JOYSTICK READ" == "UP" and selection != 3
            selection+=1
        if "JOYSTICK READ" == "UP" and selection == 3:
            selection=0
        
        if "JOYSTICK READ" == "DOWN" and selection == 0:
            selection=3
        if "JOYSTICK READ" == "DOWN" and selection != 0:
            selection-=1
        
        if "BUTTON READ" == True and selection == 0:
            Diff = 0 #Select easy difficulty
            Highscore_Display(Diff, Highscore)
        if "BUTTON READ" == True and selection == 1:
            Diff = 1 #Select medium difficulty
            Highscore_Display(Diff, Highscore)
        if "BUTTON READ" == True and selection == 2:
            Diff = 2 #Select hard difficulty
            Highscore_Display(Diff, Highscore)
        if "BUTTON READ" == True and selection == 3:
            Main_Menu()
            
        if "BUTTON READ" == False and selection == 0:
            #Highlight selection "Easy"
        if "BUTTON READ" == False and selection == 1:
            #Highlight selection "Medium"
        if "BUTTON READ" == False and selection == 2:
            #Highlight selection "Hard"
        if "BUTTON READ" == False and selection == 3:
            #Highlight selection "Main Menu"
        sleep(0.1)
            
            
    #Basic menu
    #Select    Main_Menu() / Highscore_Display(Diff,Highscore)
    
def Highscore_Display(Diff, Highscore):
    #Advanced menu
    #Uses Diff to index whether easy medium or hard is displayed,
    #Select    Highscore()
    
def Play_Game():
    while 1:

        if "JOYSTICK READ" == "UP" and selection != 3
            selection+=1
        if "JOYSTICK READ" == "UP" and selection == 3:
            selection=0
        
        if "JOYSTICK READ" == "DOWN" and selection == 0:
            selection=3
        if "JOYSTICK READ" == "DOWN" and selection != 0:
            selection-=1
        
        if "BUTTON READ" == True and selection == 0:
            Diff = 0 #Select easy difficulty
            Start_Game(Diff)
        if "BUTTON READ" == True and selection == 1:
            Diff = 1 #Select medium difficulty
            Start_Game(Diff)
        if "BUTTON READ" == True and selection == 2:
            Diff = 2 #Select hard difficulty
            Start_Game
        if "BUTTON READ" == True and selection == 3:
            Main_Menu()
            
        if "BUTTON READ" == False and selection == 0:
            #Highlight selection "Easy"
        if "BUTTON READ" == False and selection == 1:
            #Highlight selection "Medium"
        if "BUTTON READ" == False and selection == 2:
            #Highlight selection "Hard"
        if "BUTTON READ" == False and selection == 3:
            #Highlight selection "Main Menu" 
        
        sleep(0.1)
    #Basic menu
    #Select    Main_Menu() / Start_Game(diff)
    
def Start_Game(Diff):
    while 1:
        if "BUTTON READ" == True:
            Game(Diff)
    #Advanced menu
    #Uses Diff to determine at what the difficulty the game will run at.
    #Select "Press Button to start game" Game(diff)
    
def Game(Diff):
    #Gamer time
    #Snake_Body
    #Snake_Head
    #Move
    #Apple
    #Score
    #DON'T clear game state
    #Either death condition or pause, must carry highscore
    
def Pause():
    #Basic menu
    #Select    Main_Menu() / Game(diff)
    
def Death(diff, score):
    #Advanced Menu
    #Displays score
    #Appends score to highscore
    #Select     Game(diff) / Play_Game() / Main_Menu()