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
from wordlist import worldlewordlist
import random
from random import choice
from pySave import saveScore #save player score - H%

score  = 0  

def replay(name): #asks user if they would like to play again
    rep = input("Would you like to play again? type Y to continue: ")
    if rep == "Y" or rep == "y":
        gameloop(name)
    else:
        print("Thank you for playing Wordle!")
        #exit()

        input ("Press any keys to continue...") #  %H added
        import play_game #  to return back to game select - %H
    

def clear(): #clears the screen
    os.system('cls')

def gameloop(name):
    
    word = random.choice(worldlewordlist) #randomly selects word from list
    wordleword = list(word) #converts word to usable letters in list
    #print (word) #for testing purposes
    #print (wordleword)
    print("Welcome to Wordle! I'm sure you know how to play the game so let's get started!")   
    print("Y means the correct letter in correct position")
    print("C means the letter is in wrong position")
    print("X means the letter is not in the word")
    attempts = 5
    while attempts >0:

        userreturn = ""
        print (f"you have {attempts} attempts left")
        userinput = input("Guess the word1: ")
        if len(userinput) != 5:
            print("Please enter a 5 letter word")
            continue

        for i in range(len(userinput)):
            if userinput[i] == wordleword[i]:
                userreturn += "Y"
            elif userinput[i] in wordleword:
                userreturn += "C"
            else:
                userreturn += "X"
        if userinput != word:
            attempts -= 1
            print(userreturn)
            print("Attempts left: ", attempts)
        else:
            score = attempts + 10
            print("Congratulations! You guessed the word!")
            print("You scored: ", score) # I change a bit -H%
            saveScore(name, score, "wordle") #save player score - H%
            replay(name)     
    print("You have run out of attempts! The word was: ", word)
    replay(name)   
#clear()
#gameloop() 


# sources:
# https://github.com/Nextross/Wordle-python/blob/main/main.py
# 
