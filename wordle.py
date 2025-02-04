# *************************************************************************
# Program: Wordle.py
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN
# Lecture / Lab Section: TC3L / TL3L
# Trimester: 2430
# Names: Imran Haris Bin Mohd Azli | MEMBER_NAME_2 | MEMBER_NAME_3 | MEMBER_NAME_4
# IDs: MEMBER_ID_1 | MEMBER_ID_2 | MEMBER_ID_3 | MEMBER_ID_3
# Emails: MEMBER_EMAIL_1 | MEMBER_EMAIL_2 | MEMBER_EMAIL_3 | MEMBER_EMAIL_3
# *************************************************************************


import os
from wordlist import worldlewordlist
import random
from random import choice

score  = 0  

def replay(): #asks user if they would like to play again
    rep = input("Would you like to play again? type Y to continue: ")
    if rep == "Y" or rep == "y":
        gameloop()
    else:
        print("Thank you for playing Wordle!")
        input ("Presss any keys...") #  %H added
        #exit()

        from main_game import play_game #  %H added
        play_game() #  %H added
    

def clear(): #clears the screen
    os.system('cls')

def gameloop():
    word = random.choice(worldlewordlist) #randomly selects word from list
    wordleword = list(word) #converts word to usable letters in list
    print (word) #for testing purposes
    print (wordleword)
    print("Welcome to Wordle! I'm sure you know how to play the game so let's get started!")   
    print("Y means the correct letter in correct position")
    print("C means the letter is in wrong position")
    print("X means the letter is not in the word")
    attempts = 5
    while attempts >0:  
        userreturn = " "
        userinput = input("Guess the word: ")
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
            print("Congratulations! You guessed the word!")
            print("You scored: ", attempts + 10)
            replay()     
    print("You have run out of attempts! The word was: ", word)
    replay()   
clear()
gameloop() 


# sources:
# https://github.com/Nextross/Wordle-python/blob/main/main.py
# 
