import math
print("Sisesta ruudu külje pikkus: ")
a = int(input())

r = a*(math.sqrt(2))/2
S = math.pi*r**2
P = 2*math.pi * r

print("Ringi pindala on: ", round(S,2))
print("Ringi ümbermõõt on: ", round(P,2))
