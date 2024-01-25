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
            #add()
            print("testing")

    print(f"{sona} -> {sona2}")
    
def add():
    while True:
        riik = str(input("riik?: "))
        pealinn = str(input("pealinn"))
        print("\nis it right")
        YN = str(input("do u want add this word?: "))
        if YN[0].lower() == "y":
            pealinn_riik[riik] = pealinn
            break


riik_pealinn = dict()
pealinn_riik = dict()
f = open("riigid_pealinnd.txt", 'r')
for x in f:
    Euroopa = x.split("-")
    riik_pealinn[Euroopa[0]] = Euroopa[1][:-2]
    pealinn_riik[Euroopa[1]] = Euroopa[0]
f.close()

print("Find")

mode = str(input("mode")).lower()

match mode[0]:
    case "f":
        find()
    case "q":
        exit()




