import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print ("=============================================================")
    print ("Welcome to HAIA games!")
    print ("=============================================================")
    name = input ("Please enter your name: ")
    
    
    clear()
    print("==============================================================")
    print ("Greetings", name, "! Here's a list of games you can play:")
    print ("1. Wordle")
    print ("2. Hangman")
    print ("3. Math Quiz")
    print("==============================================================")
    
    choice = input ("Which game would you like to play? : ")

    if choice == "1":
        print ("You have chosen Wordle!")
        input ("Press Enter to play...")
        break
    elif choice == "2":
        print ("You have chosen Hangman!")
        input ("Press Enter to play...")
        break
    elif choice == "3":
        print ("You have chosen Math Quiz!")
        input ("Press Enter to play...")
        break