import time
import os
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        username='root',
        password='Anas!007',
        host='localhost'
    )

    cursor = conn.cursor()

    cursor.execute('CREATE DATABASE IF NOT EXISTS login')
    conn.commit()
    cursor.execute('USE login')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS creds(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, username varchar(15) NOT NULL, password varchar(15) NOT NULL)')
    conn.commit()
except Error as e:
    print(f'Error connecting to MySQL: {e}')


def main_query(username, password):
    cursor.execute('SELECT * FROM creds WHERE username = %s AND password = %s', (username, password))
    results = cursor.fetchone()
    return results

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')




def reset():
    while True:
        reset = input("Do you wish to reset the password of your account: y/n\n=> ")
        time.sleep(2)
        if reset.lower() in ["y", "yes"]:
            clear_console()
            username = input("Enter the username you want to reset the password of: ")
            old_password = input("Enter your current password: ")
            clear_console()
            user_creds = main_query(username, old_password)
            if user_creds:
                    new_pass = input("Enter your new password: ")
                    confirm_new_pass = input("Confirm new password: ")
                    if new_pass == confirm_new_pass:
                        cursor.execute('UPDATE creds SET password = %s WHERE username = %s', (new_pass, username))
                        print(f"Password for {username} has been succesfully reseted!")
                        conn.commit()
                        time.sleep(2)
                        break
                    else:
                        print("passwords do not match please try again...")
                        time.sleep(2)
                        clear_console()

            else:
                print("Username or password has not been found in the database")
                time.sleep(2)
                clear_console()
        elif reset.lower() in ["n", "no"]:
            print("Password reset has been cancelled")
            time.sleep(2)
            clear_console()
            break
        else:
            print(f"Wrong input, {reset} is not a valid choice")
            time.sleep(2)
            clear_console()


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
        user_creds = main_query(name, password)
        if user_creds:
            clear_console()
            print(f"Welcome {name}")
            time.sleep(2)
            clear_console()
            break
        else:
            print("Username or Password wrong")
            time.sleep(2)
            clear_console()
            tries += 1



def add():
    while True:
        new_user = input("Enter a new username: ")
        new_password = input("Enter a new password: ")
        user_creds = main_query(new_user, new_password)
        if user_creds:
            print("Username already exists...")
            time.sleep(2)
        else:
            cursor.execute('INSERT INTO creds(username, password) VALUES(%s, %s)', (new_user, new_password))
            conn.commit()
            print(f"New account: {new_user} succesfully added!")
            break


def pop(username):
    cursor.execute('SELECT * FROM creds WHERE username = %s', (username,))
    user_creds = cursor.fetchone()
    if user_creds:
        cursor.execute('DELETE FROM creds WHERE username = %s', (username,))
        conn.commit()
        print(f"{username} succesfully deleted!")
        time.sleep(2)
        clear_console()



def menu():
    while True:
        print("...Digital Login Interface V.2.0 By Anasteiro...\n")
        time.sleep(2)
        option = input("Options:\n1)Add a new account on the database\n2)Delete your account\n3)Logout\n4)Check your Account\n5)Exit\n=> ")
        if option == "1":
            add()
            clear_console()
            time.sleep(2)
        elif option == "2":
            clear_console()
            pop(name)
            time.sleep(2)
            in_or_up = input("Would you like to sign in or sign up?(type in if you have an account or up to create one)\n=> ")
            if in_or_up.lower() == "in":
                login()
            elif in_or_up.lower() == "up":
                add()
                clear_console()
                login()
            else:
                print("Wrong Input...")
                time.sleep(1)
                clear_console()

        elif option == "3":
            clear_console()

            login()

        elif option == "4":
            print(f"Username: {name}")
            cursor.execute('SELECT password FROM creds WHERE username = %s', (name, ))
            tup_pass = cursor.fetchone()
            password = tup_pass[0]
            print("password: " + len(password)*"*")
            time.sleep(3)
            reset()

        elif option == "5":
            print("See you soon!")
            break
        elif option == "hack":
            cursor.execute('SELECT * FROM creds')
            user_creds = cursor.fetchall()
            print(user_creds)
            time.sleep(1)
        else:
            print(f"Wrong input, {option} is not a valid choice")
            time.sleep(2)
            clear_console()

try:
    while True:
        clear_console()
        in_up = input("Hello, welcome to the digital login interface by Anasteiro, do you have an account?(y/n)\n=> ")
        if in_up.lower() in ["y", "yes"]:
            login()
            menu()
        elif in_up.lower() in ["n", "no"]:
            add()
            clear_console()
            time.sleep(2)
            login()
            menu()
        else:
            print(f"Wrong input, {in_up} is not a valid choice")
            time.sleep(2)
            clear_console()

except KeyboardInterrupt:
    print("\nProgram succesfully stopped by user keyboard interruption...")
finally:
    cursor.close()
    conn.close()
