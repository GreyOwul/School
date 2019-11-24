# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:12:40 2019

@author: seand
"""

"""
Integers:
    
Diff = difficulty setting
Diff = 0 (easy)

Move = Right("R"),Up("U"),Left("L"),Down("D"),None("N")
    Move = "R"
    
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


Joystick goes in pin 0
button goes in pin 2
"""

from time import sleep
from Controller import *
import sys , pygame
from grove_library import *
pygame.init()

connection = arduinoInit('COM3')

red=(255,0,0)
orange=(255,165,0)
yellow=(218,255,0)
green=(0,255,0)
blue=(0,0,255)
indigo=(75,0,130)
violet=(238,130,238)
white=(255,255,255)
black=(0,0,0)

font = pygame.font.SysFont('Comic Sans MS', 30)

X,Y=750,750
Size = (X,Y)

display_surface = pygame.display.set_mode(Size) 



def Main_Menu():
    
    selection = 0
    
    Option_0 = font.render('Highscores', True, green, black)
    Option_1 = font.render('Play Game', True, green, black)
    Option_0Rect = Option_0.get_rect()
    Option_1Rect = Option_1.get_rect()
    Option_0Rect.center = (X // 2, (Y // 2)-15)
    Option_1Rect.center = (X // 2, (Y // 2)+15)

    Name = font.render('By Martha King and Sean Drover', True, green, black)
    NameRect = Name.get_rect()
    NameRect.center = (X // 2, (2*Y // 3))
   
    while 1:
        
        display_surface.fill(black) 
            
            
        if (GetDirection() == "D" or GetDirection() == "U")  and selection == 0:
            selection=1
        if (GetDirection() == "D" or GetDirection() == "U")  and selection == 1:
            selection=0
            
        if arduinoDigitalRead(2) == True and selection == 0:
            Highscore()
        if arduinoDigitalRead(2) == True and selection == 1:
            Play_Game()
            
        if arduinoDigitalRead(2) == False and selection == 0:
            Option_0 = font.render('Highscores', True, red, black)
            Option_1 = font.render('Play Game', True, green, black)
        if arduinoDigitalRead(2) == False and selection == 1:
            Option_1 = font.render('Play Game', True, red, black)
            Option_0 = font.render('Highscores', True, green, black)
            
        display_surface.blit(Option_0, Option_0Rect)
        display_surface.blit(Option_1, Option_1Rect)
        display_surface.blit(Name, NameRect)
            
        sleep(0.1)
    
    #Basic menu
   # Select    Highscore() / Play_Game()

def Highscore():
    
    selection = 0
    
    while 1:
        
        if GetDirection() == "U" and selection != 3:
            selection+=1
        if GetDirection() == "U" and selection == 3:
            selection=0
        
        if GetDirection() == "D" and selection == 0:
            selection=3
        if GetDirection() == "D" and selection != 0:
            selection-=1
        
        if arduinoDigitalRead(1) == True and selection == 0:
            Diff = 0 #Select easy difficulty
            Highscore_Display(Diff, Highscore)
        if arduinoDigitalRead(1) == True and selection == 1:
            Diff = 1 #Select medium difficulty
            Highscore_Display(Diff, Highscore)
        if arduinoDigitalRead(1) == True and selection == 2:
            Diff = 2 #Select hard difficulty
            Highscore_Display(Diff, Highscore)
        if arduinoDigitalRead(1) == True and selection == 3:
            Main_Menu()
            
        if arduinoDigitalRead(1) == False and selection == 0:
            #Highlight selection "Easy"
        if arduinoDigitalRead(1) == False and selection == 1:
            #Highlight selection "Medium"
        if arduinoDigitalRead(1) == False and selection == 2:
            #Highlight selection "Hard"
        if arduinoDigitalRead(1) == False and selection == 3:
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

        if GetDirection() == "U" and selection != 3
            selection+=1
        if GetDirection() == "U" and selection == 3:
            selection=0
        
        if GetDirection() == "D" and selection == 0:
            selection=3
        if GetDirection() == "D" and selection != 0:
            selection-=1
        
        if arduinoDigitalRead(1) == True and selection == 0:
            Diff = 0 #Select easy difficulty
            Start_Game(Diff)
        if arduinoDigitalRead(1) == True and selection == 1:
            Diff = 1 #Select medium difficulty
            Start_Game(Diff)
        if arduinoDigitalRead(1) == True and selection == 2:
            Diff = 2 #Select hard difficulty
            Start_Game
        if arduinoDigitalRead(1) == True and selection == 3:
            Main_Menu()
            
        if arduinoDigitalRead(1) == False and selection == 0:
            #Highlight selection "Easy"
        if arduinoDigitalRead(1) == False and selection == 1:
            #Highlight selection "Medium"
        if arduinoDigitalRead(1) == False and selection == 2:
            #Highlight selection "Hard"
        if arduinoDigitalRead(1) == False and selection == 3:
            #Highlight selection "Main Menu" 
        
        sleep(0.1)
    #Basic menu
    #Select    Main_Menu() / Start_Game(diff)
    
def Start_Game(Diff):
    while 1:
        if arduinoDigitalRead(1) == True:
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
    while 1:
        
        selection = 0
        
        if (GetDirection() == "D" or GetDirection() == "U")  and selection == 0:
            selection=1
        if (GetDirection() == "D" or GetDirection() == "U")  and selection == 1:
            selection=0
            
        if arduinoDigitalRead(1) == True and selection == 0:
            Game(Diff)
        if arduinoDigitalRead(1) == True and selection == 1:
            Diff = 1 #Select medium difficulty
    #Basic menu
    #Select    Main_Menu() / Game(diff)
    
def Death(diff, score):
    #Advanced Menu
    #Displays score
    #Appends score to highscore
    #Select     Game(diff) / Play_Game() / Main_Menu()
    
Main_Menu()