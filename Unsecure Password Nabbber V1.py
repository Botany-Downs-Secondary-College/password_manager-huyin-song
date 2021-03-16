#Unsecure password nabber V1.py
#To log in and store usernames and passwords
#Huyin Song, 22 February 2021

def menu(name, age): # A function that takes the user's inputted name and age

    print("Hello, ", name) # Greets the user with their inputted name

    if age < 13: # if condition to check if the user is old enough to access the code
        print("Sorry, you are not old enough to access this programme") # User is not old enough, is booted off the code
        exit()
    else: # User is old enough, the code tells them they are old enough
        print("You are old enough to access the programme")
        exit()

print("Welcome to Unsecure Password Nabber") # Welcomes the user to the code
name = input("What is your name? : ") # Asks the user for their name
age = int(input("What is your age? : ")) # Asks the user for their age

greeting_and_age = menu(name, age)