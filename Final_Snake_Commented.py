from grove_library import arduinoInit, speakerInit, arduinoAnalogRead, arduinoDigitalRead, speakerPlayNote
import time
import sys, pygame
import random
import os

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

X, Y = 750, 750
Size = (X, Y)

display_surface = pygame.display.set_mode(Size)
os.environ['SDL_VIDEO_CENTERED'] = "True" #Centres window on screen

Scoreboard_List = [["Easy"], ["Medium"], ["Hard"]]   #We  must initially define these lists as a score will be appended to it each time a player finishes a game


def GetDirection():                   #This function uses geometry to determine which direction the joystick is being pointed in
    X = arduinoAnalogRead(0) - 512
    Y = arduinoAnalogRead(1) - 522

    if (Y ** 2 + X ** 2) <= 625: #No input
        return 'N'
    if Y >= X and Y >= (-1) * X: #right
        return 'R'
    if Y >= X and Y <= (-1) * X: #up
        return 'U'
    if Y < X and Y >= (-1) * X: #down
        return 'D'
    if Y < X and Y < (-1) * X: #left
        return 'L'


def applenoise():                #The noise that will play when a player picks up an apple
    speakerPlayNote(4,800, 0.2)
    speakerPlayNote(4,1000, 0.2)



def deathnoise():                 #The noise that will player when a player dies
    speakerPlayNote(4,300, 0.3)
    speakerPlayNote(4,200, 0.3)
    speakerPlayNote(4,100, 0.7)


def buttonpress():              #This function checks to see if the button has pressed
    b = arduinoDigitalRead(2)
    return b


def clear():                    #This function clears the screen
    X, Y = 750, 750
    Size = (X, Y)

    display_surface = pygame.display.set_mode(Size)
    pygame.display.update()
    time.sleep(0.001)


def Main_Menu():                #This function displays the initial main menu
    X, Y = 750, 750
    Size = (X, Y)
    display_surface = pygame.display.set_mode(Size)
    selection = 2

    time.sleep(0.25)
    while 1:                                                  #Main Menu display will differ slightly depending on the selection
        display_surface = pygame.display.set_mode(Size)
        Snake = pygame.image.load("Snake.jpg")               ### IMPORTANT ### https://imgur.com/a/hycxPgJ download image as Snake.jpg and save in same folder as Final Snake
        Snake_rect = Snake.get_rect()
        Snake_rect_position = [0, 0]
        Snake_rect = Snake_rect.move(Snake_rect_position)
        display_surface.blit(Snake, Snake_rect)                    #Blits snake to display_surface in position Snake_rect

        font_title = pygame.font.SysFont("comic sans", 100) #Font assignment
        Title = font_title.render('snake.', True, yellow)
        Title_rect = Title.get_rect()
        Title_rect.center = (X // 2, 100) #Centred
        display_surface.blit(Title, Title_rect)

        font_Author = pygame.font.SysFont("comic sans", 50)
        Author = font_Author.render('By Sean Drover and Martha King', True, yellow)
        Author_rect = Author.get_rect()
        Author_rect.center = (X // 2, 175)
        display_surface.blit(Author, Author_rect)
        pygame.display.update()                   #Actually 'puts pen to paper' and makes the screen show what's going on. Without this none of the above cove would be displayed.

        if selection == 1:                        #Selection is manipulated by the input of the joystick.

            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('->Play Game', True, green)
            display_surface.blit(playagain, (220, 300))

            quit = fontplayagain.render('   Quit', True, white)
            display_surface.blit(quit, (220, 400))

            Scoreboard = fontplayagain.render('   Scoreboard', True, white)
            display_surface.blit(Scoreboard, (220, 500))
            pygame.display.update()

            if buttonpress():                     #Pressing the button on this selection will bring you to the game difficulty screen
                Game_Diff()

        if selection == 2:

            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('   Play Game', True, white)
            display_surface.blit(playagain, (220, 300))

            quit = fontplayagain.render('->Quit', True, green)
            display_surface.blit(quit, (220, 400))
            pygame.display.update()

            Scoreboard  = fontplayagain.render('   Scoreboard', True, white)
            display_surface.blit(Scoreboard, (220, 500))
            pygame.display.update()

            if buttonpress():
                sys.exit()                       #Pressing the button on this selection will close the game

        if selection == 3:

            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('   Play Game', True, white)
            display_surface.blit(playagain, (220, 300))

            quit = fontplayagain.render('   Quit', True, white)
            display_surface.blit(quit, (220, 400))

            Scoreboard = fontplayagain.render('->Scoreboard', True, green)
            display_surface.blit(Scoreboard, (220, 500))
            pygame.display.update()

            if buttonpress():
                Scoreboard()                     #Pressing the button on this selection will bring you to the difficulty selection for the scoreboards

        if selection != 1 and GetDirection() == 'U':
            selection -= 1

        if selection != 3 and GetDirection() == 'D':
            selection += 1


def Scoreboard():         #This function displays the difficulty choices for the scoreboard
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

            Back = fontplayagain.render('   Back', True, white)
            display_surface.blit(Back, (220, 600))
            pygame.display.update()

            if buttonpress():
                Scoreboard_Display(0)          #Pressing the button on this selection will display the scores for the 'easy' difficulty

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
                Scoreboard_Display(1)           #Pressing the button on this selection will display the scores for the 'medium' difficulty

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
                Scoreboard_Display(2)            #Pressing the button on this selection will display the scores for the 'hard' difficulty

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
                Main_Menu()                     #Pressing the button on this selection will return you to the Main Menu

        if selection != 1 and GetDirection() == 'U':           #These two 'if' statements explain how the selection will change based on the direction of the joystick
            selection -= 1

        if selection != 4 and GetDirection() == 'D':
            selection += 1


def Scoreboard_Display(Diff):                   #This function displays the scoreboard for each difficulty
    global Scoreboard_List
    time.sleep(.25)
    Difficulty_Colour_List = [yellow, orange, red]
    X, Y = 750, 750
    Size = (X, Y)
    display_surface = pygame.display.set_mode(Size)
    selection = 1
    ticker = 0
    fontplayagain = pygame.font.SysFont('comic sans', 70)

    while 1:
        display_surface = pygame.display.set_mode(Size)
        for e in Scoreboard_List[Diff]:                            #Iterates the scoreboard of a specific difficulty.
            Thing = fontplayagain.render(f'{e}', True, Difficulty_Colour_List[Diff])      #In the specific difficulty, assign element 'e' to 'Thing' over the 'for loop'. The colour is also determined by a psuedo deinition in the form of a list.
            display_surface.blit(Thing, (X // 2, 100 + ticker * 100))                    #Centres the score, then for every loop, places the next element 100 pixels lower
            ticker += 1
            pygame.display.update
        ticker = 0
        if selection == 1:

            Back = fontplayagain.render(f'->Back', True, green)
            display_surface.blit(Back, (30, Y // 2))
            pygame.display.update()
            if buttonpress():
                Scoreboard()              #Pressing the button on this selection will return you to scoreboard difficulty selection


def Game_Diff():        #This function displays the 3 difficulty choices for the game
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

            Back = fontplayagain.render('   Back', True, white)
            display_surface.blit(Back, (220, 600))
            pygame.display.update()

            if buttonpress():
                countdown_new(0)              #Pressing the button on this selection will begin the countdown for the easy difficulty game

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
                countdown_new(1)              #Pressing the button on this selection will begin the countdown for the medium difficulty game

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
                countdown_new(2)             #Pressing the button on this selection will begin the countdown for the hard difficulty game

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
                Main_Menu()                  #Pressing the button on this selection will return the user for the Main Menu

        if selection != 1 and GetDirection() == 'U':     #These two 'if' statements explain how the selection will change based on the direction of the joystick
            selection -= 1

        if selection != 4 and GetDirection() == 'D':
            selection += 1


def countdown_new(Diff):                #This function will display a brief countdown, and then commence the game
    X, Y = 750, 750
    Size = (X, Y)
    Difficulty_Colour_List = [yellow, orange, red]     #The colour of this countdown is dependant on the chosen difficulty
    Difficulty_Time_List = [0.20, 0.15, 0.10]

    display_surface = pygame.display.set_mode(Size)
    fontcountdown = pygame.font.SysFont('comic sans', 60)
    for num in range(1, 11, 1):
        countdown = fontcountdown.render("o" * (10 - num), True, Difficulty_Colour_List[Diff])
        display_surface.blit(countdown, (360, 375))
        pygame.display.update()
        time.sleep(Difficulty_Time_List[Diff])
        clear()

    Game(Diff)                          #Once the countdown has been completed, the game will begin


def death_new(Diff, Score):             #This function defines what will occur once a player dies
    deathnoise()                        #Death noise will be played

    global Scoreboard_List
    Scoreboard_List[Diff].append(Score)

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
    totalscore = fontscore.render(f'Total score: {Score} pts', True, green)       #Score will be displayed
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
                Game_Diff()                         #Pressing the button on this selection will bring the player to the diffuclty selection screen

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
                Main_Menu()                          #Pressing the button on this selection will return the player to the Main Menu screen

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
            selection -= 1

        if selection != 3 and GetDirection() == 'D':
            selection += 1


def AppleCheck(Snake_Body, Apple):                   #This function checks to see if the snake has picked up the apple
    for Body_part in Snake_Body:
        if Body_part == Apple:
            return True
    return False


def Game(Diff):                     #This function defines the game play component of Snake
    Score = 0
    Snake_head = [3, 12]
    Snake_Body = []
    Previous_Move = "R"                      #When the game starts, the snake will automatically be moving to the right
    Difficulty_Colour_List = [yellow, orange, red]
    Apple = [random.randint(5, 20), random.randint(5, 20)]
    X, Y = 750, 750
    Size = (X, Y)
    display_surface = pygame.display.set_mode(Size)

    while 1:

        Snake_Body.append(Snake_head)

        if GetDirection() == "U" and Previous_Move != "D":                     #The following if statements determine the direction the snake will travel base on the joystick inputs.
            Snake_head[1] -= 1                                                 #The snake's movement is also impacted by the direction of the previous joystick input ('Previous_Move')
            Previous_Move = "U"
        if GetDirection() == "D" and Previous_Move != "U":
            Snake_head[1] += 1
            Previous_Move = "D"
        if GetDirection() == "L" and Previous_Move != "R":
            Snake_head[0] -= 1
            Previous_Move = "L"
        if GetDirection() == "R" and Previous_Move != "L":
            Snake_head[0] += 1
            Previous_Move = "R"

        if GetDirection() == "U" and Previous_Move == "D":
            Snake_head[1] += 1
            Previous_Move = "D"
        if GetDirection() == "D" and Previous_Move == "U":
            Snake_head[1] -= 1
            Previous_Move = "U"
        if GetDirection() == "L" and Previous_Move == "R":
            Snake_head[0] += 1
            Previous_Move = "R"
        if GetDirection() == "R" and Previous_Move == "L":
            Snake_head[0] -= 1
            Previous_Move = "L"

        if GetDirection() == "N" and Previous_Move == "U":
            Snake_head[1] -= 1
        if GetDirection() == "N" and Previous_Move == "D":
            Snake_head[1] += 1
        if GetDirection() == "N" and Previous_Move == "L":
            Snake_head[0] -= 1
        if GetDirection() == "N" and Previous_Move == "R":
            Snake_head[0] += 1

        if Apple == Snake_head:                #If the snake picks up an apple, the apple noise will play and the user will gain a point
            applenoise()
            Score += 1
            print("point get")
            Apple = [random.randint(5, 20), random.randint(5, 20)]

        while len(Snake_Body) > Score:
            del Snake_Body[0]


        if (Snake_head[0] == 1 or Snake_head[0] == 25) or (Snake_head[1] == 1 or Snake_head[1] == 25):   #If the snake hits the border, the snake will die and the death sequence will begin

            death_new(Diff, Score)


        while AppleCheck(Snake_Body, Apple):                     #If the snake picks up an apple, a new apple will reappear
            Apple = [random.randint(5, 20), random.randint(5, 20)]

        pygame.draw.rect(display_surface, violet, [(Apple[0] - 1) * 30, (Apple[1] - 1) * 30, 30, 30])
        pygame.display.update()

        pygame.draw.rect(display_surface, Difficulty_Colour_List[Diff],
                         [(Snake_head[0] - 1) * 30, (Snake_head[1]) * 30, 30, 30])
        pygame.display.update()

        if Diff == 0:                        #Easy difficulty will have a sleep time 0.2 seconds making the game slower
            time.sleep(0.20)
        if Diff == 1:                        #Medium difficulty will have a sleep time of 0.15 seconds
            time.sleep(0.15)
        if Diff == 2:                        #Hard difficulty will have a sleep time of 0.10 seconds making the game faster
            time.sleep(0.10)


        clear()





Main_Menu()      #Call the Main Menu function to start the game