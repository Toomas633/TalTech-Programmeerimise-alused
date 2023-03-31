aastatulu = float(input("Sisesta aasta tulu: "))

if aastatulu > 0:
    if aastatulu <= 6000:
        print("Maksuvaba tulu on: ", aastatulu, "€")
    elif 6000 < aastatulu < 14400:
        print("Maksuvaba tulu on: 6000€")
    elif aastatulu >= 25200:
        print("Maksuvaba tulu on: 0€")
    elif 14400 < aastatulu < 25200:
        maksuvaba = 6000-6000/10800*(aastatulu-14400)
        print("Maksuvaba tulu on: ", maksuvaba.__round__(2), "€")
else:
    print("Arv pole positiivne")