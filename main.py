import time
import os
import json
database = {}


def load():   # SHOULD BE RUN ONLY ONCE AT THE START OF THE PROGRAM TO PARSE THE DATA FROM THE JSON FILE IN THE DATABASE
    global database
    with open("database.json", "r") as file:
        database = json.load(file)


def save():  # SHOULD BE RUN TO SAVE THE ENTIRE DATABASE AS IT IS IN THE TXT WARNING: IT WILL REPLACE ALL DATA THERE WITH WHAT'S IN DATABASE
    with open("database.json", "w") as file:
        json.dump(database, file, indent=4)


def reset():
    while True:
        reset = input("Do you wish to reset the password of your account: y/n\n=> ")
        time.sleep(2)
        if reset in ["y", "Y", "Yes", "YES", "yes"]:
            os.system("cls")
            username = input("Enter the username you want to reset the password of: ")
            old_password = input("Enter your current password: ")
            os.system("cls")
            if username in database:
                if database[username] == old_password:
                    new_pass = input("Enter your new password: ")
                    confirm_new_pass = input("Confirm new password: ")
                    if new_pass == confirm_new_pass:
                        database[username] = new_pass
                        save()

                        print(f"Password for {username} has been succesfully reseted!")
                        time.sleep(2)
                        break
                    else:
                        print("passwords do not match please try again...")
                        time.sleep(2)
                        os.system("cls")
                else:
                    print("Incorrect password...Please try again..")
                    time.sleep(2)
                    os.system("cls")
            else:
                print("Username has not been found in database")
                time.sleep(2)
                os.system("cls")
        elif reset in ["N", "n", "No", "NO", "no"]:
            print("Password reset has been cancelled")
            time.sleep(2)
            os.system("cls")
            break
        else:
            print(f"Wrong input, {reset} is not a valid choice")
            time.sleep(2)
            os.system("cls")


def login():
    global name
    global tries
    tries = 1
    while True:
        if tries % 5 == 0:
            reset_create = input("Do you wish to reset the password of your account or create a new account(type r for reset c for create and n if you do not wish to): ")
            if reset_create.lower() == "r":
                reset()
            elif reset_create.lower() == "c":
                add()
            elif reset_create.lower() == "n":
                print("Ok...")
            else:
                print("Invalid input")
        name = input("Enter your username: ")
        password = input("Enter your password: ")
        time.sleep(2)
        if name in database:
            if database[name] == password:
                os.system("cls")
                print(f"Welcome {name}")
                time.sleep(2)
                os.system("cls")
                break
            else:
                print("Username or Password wrong")
                time.sleep(2)
                os.system("cls")
                tries += 1
        else:
            print("Username or Password wrong")
            time.sleep(2)
            os.system("cls")
            tries += 1



def add():
    new_user = input("Enter a new username: ")
    new_password = input("Enter a new password: ")
    if new_user in database:
        print("Username already exists...")
        time.sleep(2)
    else:
        database[new_user] = new_password
        save()
        print(f"New account: {new_user} succesfully added!")


def pop(account):
    if account in database:
        database.pop(account)
        save()
        print(f"{account} succesfully deleted!")
        time.sleep(2)
        os.system("cls")



def menu():
    while True:
        print("...Digital Login Interface V.1.0 By Anasteiro...\n")
        time.sleep(2)
        option = input("Options:\n1)Add a new account on the database\n2)Delete your account\n3)Logout\n4)Check your Account\n5)Exit\n=> ")
        if option == "1":
            add()
            os.system("cls")
            time.sleep(2)
        elif option == "2":
            os.system("cls")
            pop(name)
            time.sleep(2)
            in_or_up = input("Would you like to sign in or sign up?(type in if you have an account or up to create one)\n=> ")
            if in_or_up.lower() == "in":
                login()
            elif in_or_up.lower() == "up":
                add()
                login()

        elif option == "3":
            os.system("cls")

            login()

        elif option == "4":
            print(f"Username: {name}")
            print("password: " + len(database[name])*"*")
            time.sleep(3)
            reset()

        elif option == "5":
            print("See you soon!")
            break
        elif option == "hack":
            for value, key in database.items():
                print(f"USERNAME:{value} PASSWORD:{key}")
                time.sleep(1)
        else:
            print(f"Wrong input, {option} is not a valid choice")
            time.sleep(2)
            os.system("cls")

try:
    try:
        load()
    except FileNotFoundError:
        print("Creating database file...")
        time.sleep(2)
        with open("database.json", "w") as file:
            json.dump(database, file, indent=4)
    while True:
        os.system("cls")
        in_up = input("Hello, welcome to the digital login interface by Anasteiro, do you have an account?(y/n)\n=> ")
        if in_up.lower() in ["y", "yes"]:
            login()
            menu()
        elif in_up.lower() in ["n", "no"]:
            add()
            os.system("cls")
            time.sleep(2)
            login()
            menu()
        else:
            print(f"Wrong input, {in_up} is not a valid choice")
            time.sleep(2)
            os.system("cls")

except KeyboardInterrupt:
    print("\nProgram succesfully stopped by user keyboard interruption...")
