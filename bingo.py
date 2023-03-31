import random
from turtle import mode
f = open("väljakud.txt", mode="w", encoding="utf8")
v = int(input("Sisesta mänguväljaku ruudu suurus (mitu arvu reas): "))
t = int(input("Sisesta korrutustabeli suurus(mis arvuni korrutatakse): "))
h = 0
m = int(input("Mitu tabelit: "))

arvud = []
print("Väljaku suuruses: ", v, "x", v)
print("Korrutustabeli suurus: ", t, "x", t)

print("\n")

while h < m:
    h = h + 1
    f.write(str(h)+". väljak"+"\n"+"\n")
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            a = random.randint(1, t)
            if a not in arvud:
                arvud.append(a)
            b = random.randint(1, t)    
            if b not in arvud:
                arvud.append(b)
            c = a*b
            f.write(str(c)+"\t")
        f.write("\n")
    f.write("\n")
    arvud.clear()

f.close()