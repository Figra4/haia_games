# *************************************************************************
# Program: HAIA_games.py
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN
# Lecture / Lab Section: TC3L / TL3L
# Trimester: 2430
# Names: Imran Haris  | HANA HUMAIRAH | MUHAMMAD ADAM HAZRIQ | ALISHA SOFEA
# IDs: 1221107067 | 242FC241PB | 242FC2422B | 242FC241YQ
# Emails: 1221107067@mmu.edu.my | HANA.HUMAIRAH.ZOOL@student.mmu.edu.my | MUHAMMAD.ADAM.HAZRIQ@student.mmu.edu.my | alisha.sofea.ali@student.mmu.edu.my
# *************************************************************************
from pySave import saveScore #save player score - H%

#importing random features and counter from python programme
import random
from collections import Counter

def hangman(name): #H%
    #declaring variable for list of words that will be picked randomly
    WordsCandidates = "pencil pen book cellotape calculator paper stapler marker ruler eraser"

    #spliting each word in the string
    WordsCandidates = WordsCandidates.split(' ')
    #returns a random element from a sequence
    Word = random.choice(WordsCandidates) 
    #print (Word) 
    #user interface
    print ("Guess the word! HINT: word is name of a stationery")

    #printing empty spaces for letters of the word
    for i in Word:
        print ('_', end=" ")
    #storing the letters guessed by the player
        LetterGuessed = ''
        chances = len(Word)+2
        correct = 0
        flag = 0
        try:
            while (chances != 0) and flag == 0:
    #when the player already start guessing and the guess is not correct since the flag is 0
                print()
                chances = chances-1
                try:
                    guess = str(input('Enter a letter to guess: '))
                except :
                    print ("Enter only a letter!")
                    continue

    #Validation of a guess .isalpha() is a method to check if all the all characters are alphabet in python. It returns true if correct and false if not alphabet
                if not guess.isalpha():
                    print ("Enter only a LETTER")
                    continue
                elif len(guess) >1:
                    print ("Enter only a SINGLE letter")
                    continue
                elif guess in LetterGuessed:
                    print ("You have already guessed that")
                    continue

    #If letter is guessed correctly
                if guess in Word:
                    LetterGuessedCounter = Word.count(guess)
                    for _ in range (LetterGuessedCounter):
                        LetterGuessed += guess

    #Print the word end = '' is to prevent starting new line for any string
                    for char in Word:
                        if char in LetterGuessed and (Counter(LetterGuessed)) != (Counter(Word)):
                            print (char, end = '')

    #If user has guessed all the letters; once the correct word is guessed
                        elif (Counter(LetterGuessed)) == (Counter(Word)):
                            score = 10 #H%
                            print ("The word is ", end= '')
                            print(Word)
                            flag = flag + 1
                            print ('Congratulations, You won!')
                            input ("Press any keys to continue...") #H%
                            saveScore(name, score, "wordle") #save player score - H%
                            
                            break


                        else: print('_', end='')

                if chances <= 0 and (Counter(LetterGuessed)) != (Counter(Word)):
                    score = 0 #H%
                    print()
                    print ("You lost!")

                    replay = input("Try again? (Y/N)") # %H

                    if replay == "y":
                        continue
                    else:
                        print ("Thanks for playing!")
                        input ("Press any keys to continue...")
                        saveScore(name, score, "wordle") #save player score - H%

                        import play_game #return to game select - H%

        except KeyboardInterrupt:
            print()
            print("Bye! Try again")
            exit()
