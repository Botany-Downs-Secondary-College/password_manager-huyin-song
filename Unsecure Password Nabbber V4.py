#Unsecure password nabber V4.py
#To log in and store usernames and passwords
#Huyin Song, 22 February 2021

passwords = ["CoolLiquid312", "BT7274"]

try:
    def menu(name, age): # A function that takes the user's inputted name and age

        print("Hello, ", name) # Greets the user with their inputted name

        if age < 13: # if condition to check if the user is old enough to access the code
            print("Sorry, you are not old enough to access this programme") # User is not old enough, is booted off the code
            exit()
        else: # User is old enough, the code prints options for the user to select
            mode = input("""Select a mode with the following numbers-
1. Add passwords
2. View passwords
3. Exit programme
Please choose a mode : """).strip() # Strips their input of spaces
            return mode

    print("Welcome to Unsecure Password Nabber") # Welcomes the user to the code
    name = input("What is your name? : ") # Asks the user for their name
    age = int(input("What is your age? : ")) # Asks the user for their age

    while True: 
        chosen_mode = menu(name, age) # Calls the funtion, gives user's name and age

        if chosen_mode == "1": # If the user chose mode 1
            passwords.append(input("What is the password you wish to add? : ")) # Asks and adds user inputs to passwords list
        else:
            print("That was incorrect man") # If the user chose something other than the available modes, tells them its incorrect
except(ValueError):
    print("Please input a correct value")