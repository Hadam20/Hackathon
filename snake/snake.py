import random

file = open("snake.txt", "r", encoding='utf-8')
minden = file.read()
file.close()
palya = []
for a in minden.split("\n"):
    palya.append(a)

kezdes = [random.randint(1, 30), random.randint(1, 60)]
templist = []
for b in palya[kezdes[0]]:
    templist.append(b)
templist[kezdes[1]] = "@"
tempword = ""
for c in templist:
    tempword += c
palya[kezdes[0]] = tempword

kigyo = kezdes
vege = False
while vege != True:
    for e in palya:
        print(e)
    print("Hova?")
    hova = input()
    if hova == "balra":
        print("balra")

        if palya[kigyo[0]][kigyo[1]-1] == "*":
            vege = True
        else:
            templist = []
            for f in palya[kigyo[0]]:
                templist.append(f)
                templist[kigyo[1]] = " "
                templist[kigyo[1]-1] = "@"
            tempword = ""
            for g in templist:
                tempword += g
            palya[kigyo[0]] = tempword
            kigyo[1] = kigyo[1]-1

    elif hova == "jobbra":
        print("jobbra")

        templist = []
        for f in palya[kigyo[0]]:
            templist.append(f)
        templist[kigyo[1]] = "@"
        tempword = ""
        for g in templist:
            tempword += g
        palya[kigyo[0]] = tempword

    elif hova == "fel":
        print("fel")

        templist = []
        for f in palya[kigyo[0]]:
            templist.append(f)
        templist[kigyo[1]] = "@"
        tempword = ""
        for g in templist:
            tempword += g
        palya[kigyo[0]] = tempword

    elif hova == "le":
        print("le")

        templist = []
        for f in palya[kigyo[0]]:
            templist.append(f)
        templist[kigyo[1]] = "@"
        tempword = ""
        for g in templist:
            tempword += g
        palya[kigyo[0]] = tempword

    elif hova == "meguntam":
        vege = True
    else:
        print("(balra / jobbra / fel / le / meguntam)")
else:
    print("Most ennyi volt, szép napot!")
