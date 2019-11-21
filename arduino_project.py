from grove_library import arduinoInit, speakerInit, arduinoAnalogRead, arduinoDigitalRead, speakerPlayNote
import time

connection = arduinoInit('COM4')
speakerInit(4, connection)


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
    time.sleep(0.3)


def buttonpress():
    b = arduinoDigitalRead(2)
    return b



