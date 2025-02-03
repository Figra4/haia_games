import os

def clear(): #<---- clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def congrats():
    print ("=============================================================")
    print ("Congratulations! You have completed the game!")
    print ("=============================================================")

#greet and get user name
clear()
print ("=============================================================")
print ("Welcome to HAIA games!")
print ("=============================================================")
name = input ("Please enter your name: ")
    
while True:
    #game selection
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
        
        clear()
        congrats()
        input ("Press Enter to continue...")

    elif choice == "2":
        print ("You have chosen Hangman!")
        input ("Press Enter to play...")
        break
    elif choice == "3":
        print ("You have chosen Math Quiz!")
        input ("Press Enter to play...")
        break