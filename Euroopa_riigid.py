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
        print(f"{i}:{x} {riik_pealinn[x]}")
    print()

def edit():
    show()
    max = len( list(riik_pealinn.keys()) )
    pick = int()
    while ( not (0 < pick <= max) ):
        pick1 = str(input("line: "))
        if pick1[0].lower() == "q":
            break
        if ( pick1.isnumeric() ):
            pick = int(pick1)
    
    lrp = ( ( list(riik_pealinn.keys()) )[pick-1] )
    op = str(input("r/l: "))
    while True:
        if op[0].lower() == 'l':
            nimi = (str(input("test: ")).lower()).capitalize()
            riik_pealinn[lrp] = nimi
            break
        elif op[0].lower() == 'r':
            riik = str(input("riik: ")).lower().capitalize()
                        
            riik_pealinn[riik] = riik_pealinn[lrp]
            riik_pealinn.pop(lrp)
            break
    
def game():
    win = int(0)
    max = len( list(riik_pealinn.keys()) )
    HMR = str
    while( type(HMR) != int ):
        
        HMR = str(input("word: "))
        if (HMR.isnumeric()):
            HMR = int(HMR)


    for x in range(HMR):
        r = randint(0,max)

        if ( randint(0,4096) % 2 == 0 ):
            print("Riik = Pealinn?")
            rp = (list(riik_pealinn.keys()))[r]
        else:
            print("Pealinn = Riik?")
            rp = {(list(riik_pealinn.values()))[r]}

        answer = (str(input(f"{rp} = ")).lower()).capitalize()
    
        if ( riik_pealinn[(list(riik_pealinn.keys()))[r]] == answer):
            win += 1
            print("oige")
        elif ( (list(riik_pealinn.keys()))[r] == answer ):
            win += 1
            print("oige")
        else:
            print("vale")

    print(f"{ (win/HMR)*100 }% is your score")
    print()

def save():

    max = len(list(riik_pealinn.keys()))
    f = open("riigid_pealinnd.back.txt", 'w')
    f.write("")
    f.close()

    f = open("riigid_pealinnd.back.txt", 'a')
    for x in range(max):
        f.write(f"{list(riik_pealinn.keys())[x]}-{list(riik_pealinn.values())[x]}\n")
    f.close()

riik_pealinn = dict()

f = open("riigid_pealinnd.txt", 'r')
for x in f:
    Euroopa = x.split("-")
    riik_pealinn[Euroopa[0]] = Euroopa[1][:-2]
f.close()

while True:
    print("f = Find")
    print("s = Show")
    print("e = Edit")
    print("g = Game")
    print("q = Quit")
    print("c = save")

    mode = str(input("modes: ")).lower()
    if not(mode):
        mode = " "

    match mode[0]:
        case "f":
            find()
        case "s":
            show()
        case "e":
            edit()
        case "g":
            game()
        case "q":
            exit()
        case "c":
            save()
        case "":
            pass