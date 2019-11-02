#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 02:47:46 2019

@author: kendall772
"""

#This code prints a palindrome half/full pyramid of numbers
#Note, in the expected output, the interger value is related to an input of row number (n) such that output is (("1"*n)**2)
    #1^2=1
    #11^2=121
    #111^3=12321
    
n=int(input("number of rows: "))

if 0<n<10:
    for n in range(1,n+1):
        print(int("1"*n)**2)
#Note line 10

else:
    print("ERROR")
