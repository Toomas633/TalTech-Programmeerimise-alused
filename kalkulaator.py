a =int(input("Palun sisesta esimene arv: "))
b = int(input("Sisesta teine arv: "))

sum = a + b
vah = a - b
kor = a * b
jag1 = a / b
jag2 = b / a
prots25 = a * 0.25
prots75 = b * 0.75

print("Arvude summa: " , sum)
print("Arvude vahe: " , vah)
print("Arvude korrutis: ", kor)
print("Esimese ja teise jagatis: ", jag1)
print("Teise ja esimese jagatis: ", jag2)
print("25% esimeset arvust: ", prots25)
print("75% teisest arvust: ", prots75)
print()
input("Sulgemiseks vajuta Enter")