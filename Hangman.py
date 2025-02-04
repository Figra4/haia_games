#importing random features and counter from python programme
import random
from collections import Counter

#declaring variable for list of words that will be picked randomly
WordsCandidates = "pencil pen book cellotape calculator paper stapler marker ruler eraser"

#spliting each word in the string and choose it
WordsCandidates = WordsCandidates.split(' ')
Word = random.choice(WordsCandidates)

#user interface
print ("Guess the word! HINT: word is name of a stationery")

#printing empty spaces for letters of the word
for i in Word:
    print ('_', end=" ")
    playing = True # storing the letters guessed by the player
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

#Validation of a guess
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

#Print the word
                for char in Word:
                    if char in LetterGuessed and (Counter(LetterGuessed)) != (Counter(Word)):
                        print (char, end = '')

#If user has guessed all the letters; once the correct word is guessed
                    elif (Counter(LetterGuessed)) == (Counter(Word)):
                        print ("The word is ", end= '')
                        print(Word)
                        flag = flag + 1
                        print ('Congratulations, You won!')
                        break

                        break

                    else: print('_', end='')

            if chances <= 0 and (Counter(LetterGuessed)) != (Counter(Word)):
                print()
                print ("You lost!")

    except KeyboardInterrupt:
        print()
        print("Bye! Try again")
        exit()
