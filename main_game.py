import os
from wordle import gameloop
from Math_Quiz import play
from Hangman import hangman

name = ""

def clear(): #<---- clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game(name):

    while True:
        #game selection
        clear()
        print("==============================================================")
        print ("Greetings", name, "! Here's a list of games you can play:")
        print ("1. Wordle")
        print ("2. Hangman")
        print ("3. Math Quiz")
        print ("Want to check your score? Press z")
        print("==============================================================")
        
        choice = input ("Which game would you like to play? : ")

        if choice == "1":

            gameloop(name) #open wordle game

        elif choice == "2":
            
            hangman(name)

        elif choice == "3":

            play(name)

        elif choice == "z":

            from pySave import checkScore
            checkScore()

def intro():
    clear()
    print ("=============================================================")
    print ("Welcome to HAIA games!")
    print ("=============================================================")
    global name 
    name = input ("Please enter your name: ")

    play_game(name)
