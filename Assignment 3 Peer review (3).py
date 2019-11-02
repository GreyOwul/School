""" 

This code will take an input number then,
take input on whether a Full/Half pyramid is displayed, then
prints a palindrome Full/Half pyramid with that number of lines.

"""
 

#Takes row numbers as input from user 
numlines = int(input("How many rows would you like to print?: "))

#Choice of full/half pyramid
Pyramid_Choice=input("Would you like a full or half pyramid? (Full/Half): ")


if Pyramid_Choice == "Half":

#Section below prints the palindrome half pyramid for input number of lines
    for i in range(1,numlines+1):
        print((10**i//9)**2)
        #Note, The output for this function can be expressed with a pattern of inputs
            #Input 1, 1^2=1
            #Input 2, 11^2=121
            #Input 3, 111^2=12321
                #Line 21 takes advantage of a division rule for 9, and uses operand "//" to provide an integer value.
                    #10**i//9 == int(10**i/9)
                        #Input 1, int(10**1/9) = int(1.111...) = 1
                        #Input 2, int(10**2/9) = int(11.11...) = 11
                        #Input 3, int(10**3/9) = int(111.1...) = 111
                            #Note lines 23-25
    #Pyramid is printed, end of code.
                            
if Pyramid_Choice == "Full":
    for i in range(1,numlines+1):
        print(" "*(numlines-i), end="") #(, end="") allows for the next print function to concatenate on the same line. ("    "+"1")
        #Line above creates spacing for full pyramid
        print((10**i//9)**2)    
    #Pyramid is printed, end of code.