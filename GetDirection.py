from grove_library import *
from time import sleep




def GetDirection():
    arduinoInit(0)
    X= arduinoAnalogRead(0)-512
    Y= arduinoAnalogRead(1)-522

    if (Y**2+X**2)<=625:
        print(X,Y)
        print("none")
        return 'N' #NONE
    if Y>=X and Y>=(-1)*X:
        print(X,Y)
        print("up")
        return 'U' #UP
    if Y>=X and Y<=(-1)*X:
        print(X,Y)
        print("left")
        return 'L' #LEFT
    if Y<X and Y>=(-1)*X:
        print(X,Y)
        print("right")
        return 'R' #RIGHT
    if Y<X and Y<(-1)*X:
        print(X,Y)
        print("down")
        return 'D' #DOWN
