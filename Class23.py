#Class: 23
#Date: 2025-02-1
#Topic: project3


import random

while True:
    try:
        #user choice
        uchoice = int(input("Enter one among the following values (0,1,2): "))
        #computer choice
        cchoice = random.randint(0,2)

        print(f"User Choice: {uchoice}")
        print(f"Computer Choice: {cchoice}")

        if(uchoice > 2 or uchoice < 0):
            print("Invalid choice")
        elif(uchoice==cchoice):
            print("Draw")
        elif(uchoice==0 and cchoice==2):
            print("User Win")
        elif(cchoice==0 and uchoice==2):
            print("Computer Win")
        elif(uchoice < cchoice):
            print("Computer Win")
        else:
            print("User Win")

        break
    except Exception:
        print("The value entered is incorrect. Please try again.")
    
