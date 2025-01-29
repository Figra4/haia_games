'''
while True:
    name = input("Enter your name: ")
    score = input("Enter your score: ")
    with open("score.txt", "a") as f: #<---- "a" is for append at end of file, f = score.txt
        f.write(name + "," + score + '\n')

    print("Score saved successfully!")
    choice = input ("want to load the score? (y/n): ")

    if choice == "y":
'''

with open("score.txt", "r") as f:   # "r" is for read the file
    content = f.read()
    list = content.split('\n')
    for x in list:
        split = x.split(',')
        print(split[0] + " - " + split[1])

