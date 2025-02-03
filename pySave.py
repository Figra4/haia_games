#def save(name, sWordle, sHangman, sMath):

name = 'john'
sWordle = '10'
sHangman = '20'
sMath = '30'

with open("score.txt", "a") as f: #<---- "a" is for append at end of file, f = score.txt
    f.write('\n' + name + "," + sWordle + "," + sHangman + "," + sMath)
print("Score saved successfully!")
choice = input ("want to load the score? (y/n): ")
    
if choice == "y":
    with open("score.txt", "r") as f:   # "r" is for read the file
        content = f.read()
        list = content.split('\n')
        for x in list:
            split = x.split(',')
            if len(split) == 4:
                print ("number of entries", {len(split)})
                print(split[0] + " - " + split[1] + " - " + split[2] + " - " + split[3])
            else:
                print (" ")
else:
    print ("No score loaded")
