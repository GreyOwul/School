#This code prints a palindrome half/full pyramid of numbers

#Take row numbers as input from user
rowNumber = int(input("Enter the desired number of rows: "))

#Provide choice of display
Display=input("Would you like a full or half pyramid? (Full/Half): ")


#Write the code to print half/full pyramid
if Display=="Half":
    
    print()#Create Space
    print("Half Pyramid:")
    print()


    for i in range (1, rowNumber+1): #Inlude "+1" so that it prints the correct number of desired lines
        for k in range (1, i):
            print(k, end="") #Including "end" ensures that the next number is printed in the same line
            for k in range (i, 0, -1): 
                print(k, end="")
                print() #Creates new line for everytime the loop is ran
                
if Display=="Full":
    
    Peer_Review=input("Peer review alternative? (Y/N): ")
    
    if Peer_Review=="N":
        
        print() #Create space
        print("Full Pyramid:")
        print() #Create space

        for i in range (1, rowNumber+1): 
            for k in range(1, rowNumber-i+1): #we need the number of spaces to decrease by 1 as we go from each line
                print(end=" ") #This will create the spaces within each line
            for k in range (1, i):
                print (k, end="")
            for k in range (i, 0, -1):
                print (k, end="")
            print()

    if Peer_Review=="Y":
       
        print() #Create space
        print("Full Pyramid:")
        print() #Create space

        for i in range (1, rowNumber+1): 
            print(" "*(rowNumber-i), end="") #we need the number of spaces to decrease by 1 as we go from each line
            for k in range (1, i):
                print (k, end="")
            for k in range (i, 0, -1):
                print (k, end="")
            print()
