# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:22:59 2019

@author: seand
"""

from grove_library import arduinoInit, speakerInit, arduinoAnalogRead, arduinoDigitalRead, speakerPlayNote
import time
import sys, pygame
import random

pygame.init()

connection = arduinoInit('COM4')
speakerInit(4, connection)

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (218, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (238, 130, 238)
white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.SysFont('Comic Sans MS', 30)

X,Y=750,750
Size = (X,Y)

display_surface = pygame.display.set_mode(Size) 

Highscore_List=[["Easy sample",1,2,3],["Medium sample",1,2,3],["Hard sample",1,2,3]]


def GetDirection():
    X = arduinoAnalogRead(0) - 512
    Y = arduinoAnalogRead(1) - 522

    if (Y ** 2 + X ** 2) <= 625:
        print(X, Y)
        print("none")
        return 'N'
    if Y >= X and Y >= (-1) * X:
        print(X, Y)
        print("right")
        return 'R'
    if Y >= X and Y <= (-1) * X:
        print(X, Y)
        print("up")
        return 'U'
    if Y < X and Y >= (-1) * X:
        print(X, Y)
        print("down")
        return 'D'
    if Y < X and Y < (-1) * X:
        print(X, Y)
        print("left")
        return 'L'


def applenoise():
    speakerPlayNote(800, 0.3)
    time.sleep(0.1)  # THIS SLEEP IS ONLY HERE BECAUSE OF BROKEN SPEAKER, WE CAN SWITCH AFTER
    speakerPlayNote(1000, 0.3)
    time.sleep(0.1)


def deathnoise():
    speakerPlayNote(300, 0.3)
    time.sleep(0.3)
    speakerPlayNote(200, 0.3)
    time.sleep(0.3)
    speakerPlayNote(100, 0.3)


def buttonpress():
    b = arduinoDigitalRead(2)
    return b


def clear():
    X, Y = 750, 750
    Size = (X, Y)

    display_surface = pygame.display.set_mode(Size)
    pygame.display.update()
    time.sleep(0.001)


def countdown():
    X, Y = 750, 750
    Size = (X, Y)

    display_surface = pygame.display.set_mode(Size)
    fontcountdown = pygame.font.SysFont('comic sans', 60)
    countdown_3 = fontcountdown.render("3", True, white)
    display_surface.blit(countdown_3, (360, 375))
    pygame.display.update()
    time.sleep(1)
    clear()

    countdown_2 = fontcountdown.render("2", True, white)
    display_surface.blit(countdown_2, (360, 375))
    pygame.display.update()
    time.sleep(1)
    clear()

    countdown_1 = fontcountdown.render("1", True, white)
    display_surface.blit(countdown_1, (360, 375))
    pygame.display.update()
    time.sleep(1)
    death()


def pregame():
    while True:
        time.sleep(0.1)
        X, Y = 750, 750
        Size = (X, Y)

        display_surface = pygame.display.set_mode(Size)
        fontstartgame = pygame.font.SysFont('comic sans', 50)
        presstostart = fontstartgame.render("press button to start game", True, green)
        display_surface.blit(presstostart, (140, 340))
        pygame.display.update()

        if buttonpress() == True:
            clear()
            countdown()




def death():
    deathnoise()

    X, Y = 750, 750
    Size = (X, Y)

    display_surface = pygame.display.set_mode(Size)
    fontdeath = pygame.font.SysFont('comic sans', 100)
    you_died = fontdeath.render('YOU DIED', True, red)
    display_surface.blit(you_died, (200, 330))
    pygame.display.update()
    time.sleep(2)
    clear()

    score = 100
    display_surface = pygame.display.set_mode(Size)
    fontscore = pygame.font.SysFont('comic sans', 75)
    totalscore = fontscore.render(f'total score: {score} pts', True, green)
    display_surface.blit(totalscore, (120, 320))
    pygame.display.update()
    time.sleep(2)
    clear()

    selection = 2
    while 1:

        if selection == 1:
            display_surface = pygame.display.set_mode(Size)
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('->play again', True, green)
            display_surface.blit(playagain, (220, 300))

            quit = fontplayagain.render('   quit', True, white)
            display_surface.blit(quit, (220, 400))
            pygame.display.update()

            if buttonpress():
                pregame()

        if selection == 2:
            display_surface = pygame.display.set_mode(Size)
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('   play again', True, white)
            display_surface.blit(playagain, (220, 300))

            quit = fontplayagain.render('->quit', True, green)
            display_surface.blit(quit, (220, 400))
            pygame.display.update()

            if buttonpress():
                sys.exit()
                


        if selection == 1 and GetDirection() == 'D':
            selection = 2

        if selection == 2 and GetDirection() == 'U':
            selection = 1

        time.sleep(0.25)

def Main_Menu():

    X, Y = 750, 750
    Size = (X, Y)
    display_surface = pygame.display.set_mode(Size)
    selection = 2
    

    time.sleep(0.25)
    while 1:
        display_surface = pygame.display.set_mode(Size)
        Snake = pygame.image.load("Snake.jpg")
        Snake_rect = Snake.get_rect()
        Snake_rect_position = [0,0]
        Snake_rect = Snake_rect.move(Snake_rect_position)
        display_surface.blit(Snake,Snake_rect)    
        
        font_title = pygame.font.SysFont("comic sans",100)
        Title = font_title.render('snake.', True, yellow)
        Title_rect=Title.get_rect()
        Title_rect.center=(X//2,100)
        display_surface.blit(Title,Title_rect)
        
        font_Author = pygame.font.SysFont("comic sans",50)
        Author = font_Author.render('By Sean Drover and Martha King', True, yellow)
        Author_rect=Author.get_rect()
        Author_rect.center=(X//2,175)
        display_surface.blit(Author,Author_rect)
        pygame.display.update()

        if selection == 1:
            
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('->Play Game', True, green)
            display_surface.blit(playagain, (220, 300))

            quit = fontplayagain.render('   Quit', True, white)
            display_surface.blit(quit, (220, 400))
            
            Highscores = fontplayagain.render('   Highscores', True, white)
            display_surface.blit(Highscores, (220, 500))
            pygame.display.update()

            if buttonpress():
                Game_Diff()

        if selection == 2:
            
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('   Play Game', True, white)
            display_surface.blit(playagain, (220, 300))

            quit = fontplayagain.render('->Quit', True, green)
            display_surface.blit(quit, (220, 400))
            pygame.display.update()
            
            Highscores = fontplayagain.render('   Highscores', True, white)
            display_surface.blit(Highscores, (220, 500))
            pygame.display.update()

            if buttonpress():
                sys.exit()

        if selection == 3:
            
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('   Play Game', True, white)
            display_surface.blit(playagain, (220, 300))

            quit = fontplayagain.render('   Quit', True, white)
            display_surface.blit(quit, (220, 400))
            
            Highscores = fontplayagain.render('->Highscores', True, green)
            display_surface.blit(Highscores, (220, 500))
            pygame.display.update()

            if buttonpress():
                Highscore()

        if selection != 1 and GetDirection() == 'U':
            selection -=1

        if selection != 3 and GetDirection() == 'D':
            selection +=1

def Highscore():
    
    time.sleep(.25)
    
    X, Y = 750, 750
    Size = (X, Y)
    display_surface = pygame.display.set_mode(Size)
    selection = 1
    
    while 1:
        display_surface = pygame.display.set_mode(Size)
        if selection == 1:
            
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            Easy = fontplayagain.render('->Easy', True, yellow)
            display_surface.blit(Easy, (220, 300))

            Medium = fontplayagain.render('   Medium', True, white)
            display_surface.blit(Medium, (220, 400))

            Hard = fontplayagain.render('   Hard', True, white)
            display_surface.blit(Hard, (220, 500))
            
            Back= fontplayagain.render('   Back', True, white)
            display_surface.blit(Back, (220, 600))
            pygame.display.update()

            if buttonpress():
                Highscore_Display(0)

        if selection == 2:
            
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            Easy = fontplayagain.render('   Easy', True, white)
            display_surface.blit(Easy, (220, 300))

            Medium = fontplayagain.render('->Medium', True, orange)
            display_surface.blit(Medium, (220, 400))

            Hard = fontplayagain.render('   Hard', True, white)
            display_surface.blit(Hard, (220, 500))
            
            Back = fontplayagain.render('   Back', True, white)
            display_surface.blit(Back, (220, 600))
            pygame.display.update()

            if buttonpress():
                Highscore_Display(1)

        if selection == 3:
            
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            Easy = fontplayagain.render('   Easy', True, white)
            display_surface.blit(Easy, (220, 300))

            Medium = fontplayagain.render('   Medium', True, white)
            display_surface.blit(Medium, (220, 400))

            Hard = fontplayagain.render('->Hard', True, red)
            display_surface.blit(Hard, (220, 500))
           
            Back = fontplayagain.render('   Back', True, white)
            display_surface.blit(Back, (220, 600))
            pygame.display.update()

            if buttonpress():
                Highscore_Display(2)

        if selection == 4:
            
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            Easy = fontplayagain.render('   Easy', True, white)
            display_surface.blit(Easy, (220, 300))

            Medium = fontplayagain.render('   Medium', True, white)
            display_surface.blit(Medium, (220, 400))
            
            Hard = fontplayagain.render('   Hard', True, white)
            display_surface.blit(Hard, (220, 500))            
            
            Back = fontplayagain.render('->Back', True, green)
            display_surface.blit(Back, (220, 600))
            pygame.display.update()

            if buttonpress():
                Main_Menu() 
                
        if selection != 1 and GetDirection() == 'U':
            selection -=1

        if selection != 4 and GetDirection() == 'D':
            selection +=1
            
def Play_Game():
    filler=0
    filler+=1
    
def initialize():
    pregame()
    
def Highscore_Display(Diff):
    global Highscore_List
    time.sleep(.25)
    Difficulty_Colour_List=[yellow,orange,red]
    X, Y = 750, 750
    Size = (X, Y)
    display_surface = pygame.display.set_mode(Size)
    selection = 1
    ticker=0
    fontplayagain = pygame.font.SysFont('comic sans', 70)

    while 1:
        display_surface = pygame.display.set_mode(Size)
        for e in Highscore_List[Diff]:
            Thing = fontplayagain.render(f'{e}', True, Difficulty_Colour_List[Diff])
            display_surface.blit(Thing, (X//2, 100+ticker*100))
            ticker+=1
            pygame.display.update
        ticker=0
        if selection == 1:
            
            Back = fontplayagain.render(f'->Back  {Diff}', True, green)
            display_surface.blit(Back, (30, Y//2))
            pygame.display.update()
            if buttonpress():
                Highscore()
    
def Game_Diff():
    time.sleep(.25)
    
    X, Y = 750, 750
    Size = (X, Y)
    display_surface = pygame.display.set_mode(Size)
    selection = 1
    
    while 1:
        display_surface = pygame.display.set_mode(Size)
        if selection == 1:
            
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            Easy = fontplayagain.render('->Easy', True, yellow)
            display_surface.blit(Easy, (220, 300))

            Medium = fontplayagain.render('   Medium', True, white)
            display_surface.blit(Medium, (220, 400))

            Hard = fontplayagain.render('   Hard', True, white)
            display_surface.blit(Hard, (220, 500))
            
            Back= fontplayagain.render('   Back', True, white)
            display_surface.blit(Back, (220, 600))
            pygame.display.update()

            if buttonpress():
                countdown_new(0)

        if selection == 2:
            
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            Easy = fontplayagain.render('   Easy', True, white)
            display_surface.blit(Easy, (220, 300))

            Medium = fontplayagain.render('->Medium', True, orange)
            display_surface.blit(Medium, (220, 400))

            Hard = fontplayagain.render('   Hard', True, white)
            display_surface.blit(Hard, (220, 500))
            
            Back = fontplayagain.render('   Back', True, white)
            display_surface.blit(Back, (220, 600))
            pygame.display.update()

            if buttonpress():
                countdown_new(1)

        if selection == 3:
            
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            Easy = fontplayagain.render('   Easy', True, white)
            display_surface.blit(Easy, (220, 300))

            Medium = fontplayagain.render('   Medium', True, white)
            display_surface.blit(Medium, (220, 400))

            Hard = fontplayagain.render('->Hard', True, red)
            display_surface.blit(Hard, (220, 500))
           
            Back = fontplayagain.render('   Back', True, white)
            display_surface.blit(Back, (220, 600))
            pygame.display.update()

            if buttonpress():
                countdown_new(2)

        if selection == 4:
            
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            Easy = fontplayagain.render('   Easy', True, white)
            display_surface.blit(Easy, (220, 300))

            Medium = fontplayagain.render('   Medium', True, white)
            display_surface.blit(Medium, (220, 400))
            
            Hard = fontplayagain.render('   Hard', True, white)
            display_surface.blit(Hard, (220, 500))            
            
            Back = fontplayagain.render('->Back', True, green)
            display_surface.blit(Back, (220, 600))
            pygame.display.update()

            if buttonpress():
                Main_Menu() 
                
        if selection != 1 and GetDirection() == 'U':
            selection -=1

        if selection != 4 and GetDirection() == 'D':
            selection +=1
            
def countdown_new(Diff):
    X, Y = 750, 750
    Size = (X, Y)
    Difficulty_Colour_List=[yellow,orange,red]
    Difficulty_Time_List=[0.20,0.15,0.10]

    display_surface = pygame.display.set_mode(Size)
    fontcountdown = pygame.font.SysFont('comic sans', 60)
    for num in range(1,11,1):
        countdown=fontcountdown.render("o"*(10-num), True, Difficulty_Colour_List[Diff])
        display_surface.blit(countdown,(360,375))
        pygame.display.update()
        time.sleep(Difficulty_Time_List[Diff])
        clear()
        
    death_new(Diff,"yeet!")
    
def death_new(Diff,score):
    deathnoise()
    
    global Highscore_List
    Highscore_List[Diff].append(score)

    
    X, Y = 750, 750
    Size = (X, Y)

    display_surface = pygame.display.set_mode(Size)
    fontdeath = pygame.font.SysFont('comic sans', 100)
    you_died = fontdeath.render('YOU DIED', True, red)
    display_surface.blit(you_died, (200, 330))
    pygame.display.update()
    time.sleep(2)
    clear()
    
    display_surface = pygame.display.set_mode(Size)
    fontscore = pygame.font.SysFont('comic sans', 75)
    totalscore = fontscore.render(f'total score: {score} pts', True, green)
    display_surface.blit(totalscore, (120, 320))
    pygame.display.update()
    time.sleep(2)
    clear()

    selection = 2
    while 1:

        if selection == 1:
            display_surface = pygame.display.set_mode(Size)
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('->Play Again', True, green)
            display_surface.blit(playagain, (220, 300))

            MM = fontplayagain.render('   Main Menu', True, white)
            display_surface.blit(MM, (220, 400))

            Quitting = fontplayagain.render('   Quit', True, white)
            display_surface.blit(Quitting, (220, 500))
            pygame.display.update()

            if buttonpress():
                countdown_new(Diff)

        if selection == 2:
            display_surface = pygame.display.set_mode(Size)
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('   Play Again', True, white)
            display_surface.blit(playagain, (220, 300))

            MM = fontplayagain.render('->Main Menu', True, green)
            display_surface.blit(MM, (220, 400))

            Quitting = fontplayagain.render('   Quit', True, white)
            display_surface.blit(Quitting, (220, 500))

            pygame.display.update()

            if buttonpress():
                Main_Menu()
                
        if selection == 3:
            display_surface = pygame.display.set_mode(Size)
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('   Play Again', True, white)
            display_surface.blit(playagain, (220, 300))

            MM = fontplayagain.render('   Main Menu', True, white)
            display_surface.blit(MM, (220, 400))
            
            Quitting = fontplayagain.render('->Quit', True, green)
            display_surface.blit(Quitting, (220, 500))
            pygame.display.update()

            if buttonpress():
                sys.exit()
                


        if selection != 1 and GetDirection() == 'U':
            selection -=1

        if selection != 3 and GetDirection() == 'D':
            selection +=1

#initialize()

Main_Menu()

#Highscore()

