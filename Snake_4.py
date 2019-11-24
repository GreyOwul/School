from grove_library import arduinoInit, speakerInit, arduinoAnalogRead, arduinoDigitalRead, speakerPlayNote
import time
import sys, pygame

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


def GetDirection():
    X = arduinoAnalogRead(0) - 512
    Y = arduinoAnalogRead(1) - 522

    if (Y ** 2 + X ** 2) <= 625:
        print(X, Y)
        print("none")
        return 'N'
    if Y >= X and Y >= (-1) * X:
        print(X, Y)
        print("up")
        return 'U'
    if Y >= X and Y <= (-1) * X:
        print(X, Y)
        print("left")
        return 'L'
    if Y < X and Y >= (-1) * X:
        print(X, Y)
        print("right")
        return 'R'
    if Y < X and Y < (-1) * X:
        print(X, Y)
        print("down")
        return 'D'


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

    i = 1
    selection = 2
    while i:

        if selection == 1:
            display_surface = pygame.display.set_mode(Size)
            fontplayagain = pygame.font.SysFont('comic sans', 70)
            playagain = fontplayagain.render('->play again', True, green)
            display_surface.blit(playagain, (220, 300))

            fontquit = pygame.font.SysFont('comic sans', 70)
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

            fontquit = pygame.font.SysFont('comic sans', 70)
            quit = fontplayagain.render('->quit', True, green)
            display_surface.blit(quit, (220, 400))
            pygame.display.update()

            if buttonpress():
                quit(0.5)


        if selection == 1 and GetDirection() == 'D':
            selection = 2

        if selection == 2 and GetDirection() == 'U':
            selection = 1

        time.sleep(0.05)

def initialize():
    pregame()


initialize()