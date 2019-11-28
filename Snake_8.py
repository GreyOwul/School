from grove_library import arduinoInit, speakerInit, arduinoAnalogRead, arduinoDigitalRead, speakerPlayNote
import sys, pygame
import random
import threading
from pygame.locals import *
from random import randint
import pygame
import time

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

Highscore_List = [["Easy"], ["Medium"], ["Hard"]]




def applenoise():
    speakerPlayNote(4, 800, 0.1)
    speakerPlayNote(4,1000, 0.1)



def deathnoise():
    speakerPlayNote(4, 300, 0.3)
    speakerPlayNote(4, 200, 0.3)
    speakerPlayNote(4, 100, 0.3)


def buttonpress():
    b = arduinoDigitalRead(2)
    return b


def clear():
    X, Y = 750, 750
    Size = (X, Y)

    display_surface = pygame.display.set_mode(Size)
    pygame.display.update()
    time.sleep(0.001)



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
        Snake_rect_position = [0, 0]
        Snake_rect = Snake_rect.move(Snake_rect_position)
        display_surface.blit(Snake, Snake_rect)

        font_title = pygame.font.SysFont("comic sans", 100)
        Title = font_title.render('snake.', True, yellow)
        Title_rect = Title.get_rect()
        Title_rect.center = (X // 2, 100)
        display_surface.blit(Title, Title_rect)

        font_Author = pygame.font.SysFont("comic sans", 50)
        Author = font_Author.render('By Sean Drover and Martha King', True, yellow)
        Author_rect = Author.get_rect()
        Author_rect.center = (X // 2, 175)
        display_surface.blit(Author, Author_rect)
        pygame.display.update()

        if selection == 1:

            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('->Play Game', True, green)
            display_surface.blit(playagain, (220, 300))

            quit = fontplayagain.render('   Quit', True, white)
            display_surface.blit(quit, (220, 400))

            Highscores = fontplayagain.render('   Scoreboard', True, white)
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

            Highscores = fontplayagain.render('   Scoreboard', True, white)
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

            Highscores = fontplayagain.render('->Scoreboard', True, green)
            display_surface.blit(Highscores, (220, 500))
            pygame.display.update()

            if buttonpress():
                Highscore()

        if selection != 1 and GetDirection() == 'U':
            selection -= 1

        if selection != 3 and GetDirection() == 'D':
            selection += 1


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

            Back = fontplayagain.render('   Back', True, white)
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
            selection -= 1

        if selection != 4 and GetDirection() == 'D':
            selection += 1


def Play_Game():
    filler = 0
    filler += 1


# def initialize():
#     pregame()


def Highscore_Display(Diff):
    global Highscore_List
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
        for e in Highscore_List[Diff]:
            Thing = fontplayagain.render(f'{e}', True, Difficulty_Colour_List[Diff])
            display_surface.blit(Thing, (X // 2, 100 + ticker * 100))
            ticker += 1
            pygame.display.update
        ticker = 0
        if selection == 1:

            Back = fontplayagain.render(f'->Back', True, green)
            display_surface.blit(Back, (30, Y // 2))
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

            Back = fontplayagain.render('   Back', True, white)
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
            selection -= 1

        if selection != 4 and GetDirection() == 'D':
            selection += 1


def countdown_new(Diff):
    X, Y = 750, 750
    Size = (X, Y)
    Difficulty_Colour_List = [yellow, orange, red]
    Difficulty_Time_List = [0.20, 0.15, 0.10]

    display_surface = pygame.display.set_mode(Size)
    fontcountdown = pygame.font.SysFont('comic sans', 60)
    for num in range(1, 11, 1):
        countdown = fontcountdown.render("o" * (10 - num), True, Difficulty_Colour_List[Diff])
        display_surface.blit(countdown, (360, 375))
        pygame.display.update()
        time.sleep(Difficulty_Time_List[Diff])
        clear()

    if Diff == 0:
        size = 750
    elif Diff == 1:
        size = 500
    else:
        size = 400

    theApp = App(size, Diff)
    theApp.on_execute()


def death_new(Diff, score):
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
                Game_Diff()

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
            selection -= 1

        if selection != 3 and GetDirection() == 'D':
            selection += 1


def GetDirection():
    X = arduinoAnalogRead(0) - 512
    Y = arduinoAnalogRead(1) - 522

    if (Y ** 2 + X ** 2) <= 625:
        #print(X, Y)
        #print("none")
        return 'N'
    if Y >= X and Y >= (-1) * X:
        #print(X, Y)
        #print("right")
        return 'R'
    if Y >= X and Y <= (-1) * X:
        #print(X, Y)
        #print("up")
        return 'U'
    if Y < X and Y >= (-1) * X:
        #print(X, Y)
        #print("down")
        return 'D'
    if Y < X and Y < (-1) * X:
        #print(X, Y)
        #print("left")
        return 'L'

class Apple:
    x = 0
    y = 0
    step = 44

    def __init__(self, x, y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))


class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)

        # initial positions, no collision.
        self.x[1] = 1 * 44
        self.x[2] = 2 * 44

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))


class Game:
    def isCollision(self, x1, y1, x2, y2, bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False


class App:
    player = 0
    apple = 0

    def __init__(self, size, Diff):
        self.windowWidth = size
        self.windowHeight = size
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.player = Player(3)
        self.apple = Apple(5, 5)
        self.score = 0
        self.Diff = Diff

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True

        if self.Diff == 0:
            self._image_surf = pygame.image.load("yellowblock.jpg").convert()
            self._apple_surf = pygame.image.load("whiteblock.jpg").convert()

        if self.Diff == 1:
            self._image_surf = pygame.image.load("orangeblock.jpg").convert()
            self._apple_surf = pygame.image.load("whiteblock.jpg").convert()

        if self.Diff == 2:
            self._image_surf = pygame.image.load("redblock.jpg").convert()
            self._apple_surf = pygame.image.load("whiteblock.jpg").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()

        # does snake eat apple?
        for i in range(0, self.player.length):
            if self.game.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], 44):
                self.apple.x = randint(2, 9) * 44
                self.apple.y = randint(2, 9) * 44
                self.player.length = self.player.length + 1
                applenoise()
                self.score += 1

        # does snake collide with itself?
        for i in range(2, self.player.length):
            if self.game.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 40):
                # print("You lose! Collision: ")
                # print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                # print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                # exit(0)
                self._running = False
                #death_new(self.Diff, self.score)

        if self.player.x[0]  < 0 or self.player.x[0] > self.windowHeight-10\
                or self.player.y[0] < 0 or self.player.y[0] > self.windowWidth-10:
            # print("You lose! Offscreen: ")
            # print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
            # print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
            self._running = False
            # death_new(self.Diff, self.score)
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()

    def on_cleanup(self):
        # pygame.quit()
        pass

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            d = GetDirection()
            if (d == 'R'):
                self.player.moveRight()

            if (d == 'L'):
                self.player.moveLeft()

            if (d == 'U'):
                self.player.moveUp()

            if (d == "D"):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()

            time.sleep(50.0 / 1000.0);
        self.on_cleanup()
        self.player = Player(3)
        death_new(self.Diff, self.score)


# initialize()

Main_Menu()

# Highscore()