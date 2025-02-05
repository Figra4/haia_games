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