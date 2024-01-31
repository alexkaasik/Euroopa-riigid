from random import *

def find():
    sona = (str(input("inter a word: ")).lower()).capitalize()

    if sona in list(riik_pealinn.keys()):
        index = ( list(riik_pealinn.keys()).index(sona))
        sona2 = list(riik_pealinn.values())[index]
        print("riik -> pealinn")

    elif sona in list(riik_pealinn.values()):
        index = ( list(riik_pealinn.values()).index(sona) )
        sona2 = list(riik_pealinn.keys())[index]
        print("pealinn -> riik")
    
    else:
        YN = str(input("do u want add this word?: "))
        if YN[0].lower() == "y":
            add(sona)

    print(f"{sona} -> {sona2}")
    
def add(sona):
    if sona != "":
        while True:
            option = str(input("R/l")).lower()
            if option[0] == "r":
                r = sona
                break
            elif option[0] == "l":
                l = sona
                break

    while True:
        if option[0] != "r":
            riik = str(input("riik?: "))
        elif option[0] != "l":
            pealinn = str(input("pealinn"))
        print("\nis it right")
        option = "v"
        YN = str(input("do u want add this word?: "))
        if YN[0].lower() == "y":
            riik_pealinn[riik] = pealinn
            break
        if YN[0].lower() == "q":
            break

def show():
    i = 0
    for x in riik_pealinn:
        i += 1
        print(f"{i}:{x} {riik_pealinn[x]}")

def edit():
    show()
    pick = int(input("line: "))


riik_pealinn = dict()

f = open("riigid_pealinnd.txt", 'r')
for x in f:
    Euroopa = x.split("-")
    riik_pealinn[Euroopa[0]] = Euroopa[1][:-2]
f.close()

print("f = Find")
print("s = Show")
print("e = Edit")

mode = str(input("modes: ")).lower()

match mode[0]:
    case "f":
        find()
    case "s":
        show()
    case "e":
        edit()
    case "q":
        exit()




