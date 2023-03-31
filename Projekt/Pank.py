import csv
import sys
from time import *
from os import system, name, _exit
import hashlib
from getpass import getpass
from tqdm.std import trange

sisse_logitud = False
Väljunud = False

info = []
kasutaja = []
uus_raha = ""
loend_1 = 0
loend_2 = 0
loend_3 = 0
adminparool = "85d6385b945c0d602103db39b0b654b2af93b5127938e26a959c123f0789b948" #PIN: 2001

def salvestamine_lõpp():
    global info
    with open(file="kasutajad.csv", mode="w", encoding="utf8", newline="") as kas:
        uuskas = csv.writer(kas, delimiter=",")
        uuskas.writerows(info)
    clear()
    toolbar_width = 25
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))
    for i in trange(toolbar_width):
        sleep(0.1) 
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("]\n")
    clear()
    _exit(0)
    

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

def lugemine():
    global info
    with open(file="kasutajad.csv", mode="r", encoding="utf8") as n:
        reader = csv.reader(n, delimiter=",")
        info = list(reader)
    start()

def raha_salvestamine():
    global kasutaja
    global info
    lines = list(info)
    kasutaja_index = lines.index(kasutaja)
    global uus_raha
    lines[kasutaja_index][2] = float(uus_raha)
    kasutaja[2] = float(uus_raha)
    info = list(lines)

def kasutajad():
    clear()
    print("Teretulemast panka!"+"\n")
    print("[1] Logi sisse")
    print("[2] Loo uus kasutaja")
    print("[3] Välju")
    print("[4] Administraator")
    vastus = input("\n")
    try:
        vastus = int(vastus)
    except:
        clear()
        print("Vale sisend")
        sleep(3)
        clear()
        start()
    if vastus == 1:
        clear()
        sisse_logimine()
    elif vastus == 2:
        clear()
        kasutaja_tegemine()
    elif vastus == 3:
        clear()
        salvestamine_lõpp()
    elif vastus == 4:
        clear()
        sisend = str(getpass("Sisesta parool: "))
        sisend = hashlib.sha256(sisend.encode())
        if sisend.hexdigest() == adminparool:
            print(info)
            input("Väljumiseks vajuta Enter")
            clear()
            start()        
        else:
            clear()
            print("vale parool")
            sleep(3)
            clear()
            start()
    else:
        clear()
        print("Vale sisend")
        sleep(3)
        clear()
        start()

def sisse_logimine():
    global kasutaja
    global info
    global uus_raha
    nimi_1 = input("Sisesta enda eesnimi: ").capitalize()
    nimi_2 = input("Sisesta enda perenimi: ").capitalize()
    nimi = nimi_1 + " " + nimi_2
    for i in info:
        if nimi in i:
            k = list(i)
            kasutaja.append(k[0])
            kasutaja.append(k[1])
            kasutaja.append(k[2])
            parool = str(getpass("Sisesta PIN: "))
            try:
                parool = int(parool)
            except:
                clear()
                print("Parool koosneb numbritest")
                sleep(3)
                clear()
            if parool == int(kasutaja[1]):
                global sisse_logitud
                sisse_logitud = True
                uus_raha=kasutaja[2]
                clear()
                start()
            else:
                clear()
                print("Vale PIN")
                sleep(3)
                clear()
                start()
        else:
            clear()
            print("Kasutajat ei leitud")
            sleep(3)
            clear()
            start()
                    
def kasutaja_tegemine():
    global kasutaja
    global uus_raha
    kasutaja.clear()
    nimi_1 = input("Sisesta enda eesnimi: ").capitalize()
    nimi_2 = input("Sisesta enda perenimi: ").capitalize()
    nimi = nimi_1 + " " + nimi_2
    kasutaja.append(nimi)       
    parool = str(getpass("Sisesta soovitud PIN: "))
    parool_kontroll = str(getpass("Sisesta PIN uuesti: "))
    try:
        parool = int(parool)
        parool_kontroll = int(parool_kontroll)
    except:
        clear()
        print("Parool peab koosnema numbritest")
        sleep(3)
        clear()
    if parool != parool_kontroll:
        clear()
        print("PIN-id ei ühti")
        sleep(3)
        clear()
    elif len(str(parool)) < 4:
        clear()
        print("PIN peab olema vähemalt 4 numbrit")
        sleep(3)
        clear()
    else:
        kasutaja.append(parool)
        kasutaja.append(0)
        global sisse_logitud
        sisse_logitud = True
        info.append(kasutaja)
        uus_raha=kasutaja[2]
        clear()
        start()

def raha_väljavõtmine():
    global kasutaja
    try:
        väljavõetud_summa = float(input("Kui palju soovite raha välja võtta: "))
        raha = float(kasutaja[2])
        if väljavõetud_summa > raha:
            clear()
            print("Teil pole nii palju raha.")
            sleep(3)
            clear()
            start()
        elif väljavõetud_summa < 0.01:
            clear()
            print("Liiga väike summa")
            sleep(3)
            clear()
        else:
            global uus_raha
            uus_raha = raha - väljavõetud_summa
            clear()
            print(str(väljavõetud_summa) + '€ on Teie poolt välja võetud.')
            print('Raha alles ' + str(uus_raha) + '€')
            raha_salvestamine()
            sleep(3)
            clear()
    except:
        clear()
        print("Palun sisestage number")
        sleep(3)
        clear()

def raha_hoiustamine():
    try:
        hoiustus_hulk = input("Kui palju soovite raha sisestada: ")
        hoiustus_hulk = float(hoiustus_hulk)
        raha = float(kasutaja[2])
        if hoiustus_hulk < 0.01:
            clear()
            print("Rahahulk on liiga väike")
            sleep(3)
            clear()
        else:
            global uus_raha
            uus_raha = raha + hoiustus_hulk
            clear()
            print(str(hoiustus_hulk) + '€ on Teie kontole kantud.')
            print('Raha alles ' + str(uus_raha) + '€')
            raha_salvestamine()
            sleep(3)
            clear()
            start()
    except:
        clear()
        print("Palun sisestage raha hulk")
        sleep(3)
        clear()

def salvestamine():
    global info
    with open(file="kasutajad.csv", mode="w", encoding="utf8", newline="") as kas:
        uuskas = csv.writer(kas, delimiter=",")
        uuskas.writerows(info)
    clear()

def parooli_vahetamine():
    global kasutaja
    global info
    global loend_1
    global loend_2
    global loend_3
    try:
        uus_parool = str(getpass("Sisesta uus parool: "))
        uus_parool_kontroll = str(getpass("Siesta parool uuesti: "))
        if int(uus_parool) == int(uus_parool_kontroll):
            if len(str(uus_parool)) < 4:
                if loend_3 <= 3:
                    loend_3 = loend_3 + 1
                    clear()
                    print("Parool peab olema vähemalt 4 numbrit")
                    sleep(3)
                    clear()
                    parooli_vahetamine()
                else:
                    loend_3 = 0
                    clear()
                    print("Parool peab olema vähemalt 4 numbrit")
                    sleep(3)
                    clear()
            else:
                lines = list(info)
                kasutaja_index = lines.index(kasutaja)
                lines[kasutaja_index][1] = str(uus_parool)
                kasutaja[1] = str(uus_parool)
                info = list(lines)
        else:
            if loend_2 <= 3:
                loend_2 = loend_2 + 1
                clear()
                print("Paroolid ei ühti")
                sleep(3)
                clear()
                parooli_vahetamine()
            else:
                loend_2 = 0
                clear()
                print("Paroolid ei ühti")
                sleep(3)
                clear()
    except:
        if loend_1 <= 3:
            loend_1 = loend_1 + 1
            clear()
            print("Sisesta numbrid")
            sleep(3)
            clear()
            parooli_vahetamine()
        else:
            loend_1 = 0
            clear()
            print("Sisesta numbrid")
            sleep(3)
            clear()

def start ():
    global Väljunud
    global sisse_logitud
    global kasutaja
    global uus_raha
    while Väljunud == False:
        if sisse_logitud == False:
            kasutajad()
        else:
            print("Teretulemast "+ kasutaja[0]+"!"+"\n")
            print("[1] Raha välja võtmine")
            print("[2] Raha hoiustamine")
            print("[3] Kontojäägi kuvamine")
            print("[4] Parooli vahetamine")
            print("[5] Välju")
            res = input()
            try:
                res = int(res)
                if res == 1:
                    clear()
                    raha_väljavõtmine()
                elif res == 2:
                    clear()
                    raha_hoiustamine()
                elif res == 3:
                    clear()
                    print(f'Teie konto suurus on {uus_raha}€')
                    sleep(3)
                    clear()
                elif res == 4:
                    clear()
                    parooli_vahetamine()
                elif res == 5:
                    clear()
                    print("Nägemiseni")
                    sleep(3)
                    Väljunud = False
                    sisse_logitud = False
                    salvestamine()
                    clear()
                    start()
                else:
                    clear()
                    print("Vale sisend")
                    sleep(3)
                    clear()
            except:
                clear()
                print("Vale sisend")
                sleep(3)
                clear()

lugemine()