hinded = open("hinded.csv", "w")
with open("arvud.csv", "r") as arvud:
    for rida in arvud:
        arv=int(rida)
        if 0 <= arv <= 50:
            hinded.write("0" + "\n")
        elif 50 < arv <= 60:
            hinded.write("1" + "\n")
        elif 60 < arv <= 70:
            hinded.write("2" + "\n")
        elif 70 < arv <= 80:
            hinded.write("3" + "\n")
        elif 80 < arv <= 90:
            hinded.write("4" + "\n")
        else:
            hinded.write("5" + "\n")

hinded.close()