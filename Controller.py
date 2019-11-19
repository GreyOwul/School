# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:25:43 2019

@author: seand
"""

X=arduinoAnalogRead(0)
Y=arduinoAnalogRead(1)

def GetDirection(X, Y):

    X-=512
    Y-=522
    if (Y**2+X**2)<=625:
        print(X,Y)
        return 4 #NONE
    if Y>=X and Y>=(-1)*X:
        print(X,Y)
        return 1 #UP
    if Y>=X and Y<(-1)*X:
        print(X,Y)
        return 0 #RIGHT
    if Y<X and Y>=(-1)*X:
        print(X,Y)
        return 2 #LEFT
    if Y<X and Y<(-1)*X:
        print(X,Y)
        return 3 #DOWN
