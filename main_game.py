# *************************************************************************
# Program: HAIA_games.py
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN
# Lecture / Lab Section: TC3L / TL3L
# Trimester: 2430
# Names: Imran Haris  | HANA HUMAIRAH | MUHAMMAD ADAM HAZRIQ | ALISHA SOFEA
# IDs: 1221107067 | 242FC241PB | 242FC2422B | 242FC241YQ
# Emails: 1221107067@mmu.edu.my | HANA.HUMAIRAH.ZOOL@student.mmu.edu.my | MUHAMMAD.ADAM.HAZRIQ@student.mmu.edu.my | alisha.sofea.ali@student.mmu.edu.my
# *************************************************************************

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
