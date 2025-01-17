#Class: 18
#Date: 2025-01-10
#Topic: Project1 - Password Checking

print("\n****Password checking*****")
password='14'
while True:
    enteredpassword=input("Enter your password: ")
    if(enteredpassword==password):
        print("correct password")
        break
    else:
        print("incorrect password")
