null = 0 
üks = 0
kaks = 0 
kolm = 0
neli = 0
viis = 0

with open("arvud.csv") as arvud:
    for rida in arvud:
        rida = int(rida)
        if 0 <= rida <= 50:
            null = null + 1
        elif 50 < rida <= 60:
            üks = üks + 1
        elif 60 < rida <= 70:
            kaks = kaks + 1
        elif 70 < rida <= 80:
            kolm = kolm + 1
        elif 80 < rida <= 90:
            neli = neli + 1
        else:
            viis = viis + 1

print("0: ", null)
print("1: ", üks)
print("2: ", kaks)
print("3: ", kolm)
print("4: ", neli)
print("5: ", viis)