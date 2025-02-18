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

score = 0

def Quiz(): #changed this - H%
    Q1Valid = False
    while not Q1Valid:
        answerQ1 = input("First Question: 2 + 2 = ?")
        if not answerQ1.isnumeric():
            print("Please enter a number")
        else:
            if answerQ1 == "4":
                print("Great job! Let's move on to the next question.")
                score += 1
                Q1Valid = True
            else:
                print("Incorrect answer")
                Q1Valid = True

    Q2Valid = False
    while not Q2Valid:
        answerQ2 = input("Second Question: 5 - 3 = ?")
        if not answerQ2.isnumeric():
            print("Please enter a number")
        else:
            if answerQ2 == "2":
                print("You're killing it ! Next Question !")           
                score += 1
                Q2Valid = True
            else:
                print("Incorrect answer")
                Q2Valid = True



    Q3Valid = False
    while not Q3Valid:
        answerQ3 = input("Third Question: What's 8 x 9 ?")
        if not answerQ3.isnumeric():
            print("Please enter a number")
        else:
            if answerQ3 == "72":
                print("Dude you're on fire ! Next Question !")
                score += 1
                Q3Valid = True
            else:
                print("Incorrect answer")
                Q3Valid = True


    Q4Valid = False
    while not Q4Valid:
        answerQ4 = input("Fourth Question: What's 60 / 12 ?")
        if not answerQ4.isnumeric():
            print("Please enter a number")
        else:
            if answerQ4 == "5":
                print("You are breezing through this, just one more question to go !")
                score += 1
                Q4Valid = True
            else:
                print("Incorrect answer")
                Q4Valid = True

    Q5Valid = False
    while not Q5Valid:
        answerQ5 = input("Last Question: Given x = 24, what is 24 % 2 ?")
        if not answerQ5.isnumeric():
            print("Please enter a number")
        else:
            if answerQ5 == "0":
                print("Correct ! You've answered all the questions !")
                score += 1
                Q5Valid = True
            else:
                print("Incorrect answer")
                Q5Valid = True

    return score

def enter():
    question = input("Continue?")
    answer = str(question)

    if answer.lower() == "yes":
        print("Great ! Let's get started.")
        score = Quiz()
        return score
    elif answer.lower() == "no":
        print("Welp, there's other games to play ! Bye !")
        exit()
    else:
        print("Not sure what that means... try answering with a yes or no")
        return enter()
    
def play(name):
    print("Welcome to Adam's Math Quiz !")
    print("In this game you are going to answer some math quizzes :)")
    score = enter()

    print("You've answered all the questions !")
    print(f"Your score is {score} out of 5")
    print("Thanks for playing !")

    saveScore(name, score, "math quiz") #save player score - H%

    input ("Press any keys to contiue...")#  %H added 

#Call the play function to start the game
#play("Player") - I disable this -H%
