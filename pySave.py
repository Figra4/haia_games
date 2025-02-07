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
#def save(name, sWordle, sHangman, sMath):

def saveScore(name, score, game_name):

    with open("score.txt", "a") as f: #<---- "a" is for append at end of file, f = score.txt
        f.write('\n' + name + ", " + str(score) + ", " + game_name)

def checkScore():
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("-------------------------------------------------------------")
    f = open('score.txt', 'r')
    file_contents = f.read() # reads contents
    print (file_contents) # prints contents
    f.close()
    print ("-------------------------------------------------------------")
    input ("Press any keys to return to games selection...")
    import play_game
