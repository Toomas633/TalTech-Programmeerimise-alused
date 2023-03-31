palgaraport = open("palgaraport_toomas_kirsing.txt",mode = "w", encoding = "utf8")
bruto = float(input("Sisesta brutopalk: "))

aastatulu = bruto * 12

if aastatulu <= 6000:
    maksuvaba = aastatulu / 12
elif 6000 < aastatulu < 14400:
    maksuvaba = 6000 / 12
elif aastatulu >= 25200:
    maksuvaba = 0
elif 14400 < aastatulu < 25200:
    maksuvaba = (6000-6000/10800*(aastatulu-14400))/12
    maksuvaba = maksuvaba.__round__(2)
  
töötuskindlustus = bruto * 0.016
kogumispension = bruto * 0.02
tulumaks = (bruto - töötuskindlustus - maksuvaba - kogumispension) * 0.2
tulumaks = tulumaks.__round__(2)
if tulumaks <= 0:
    tulumaks = 0
else:
    tulumaks == tulumaks

netopalk = bruto - tulumaks - kogumispension - töötuskindlustus
sotsiaalmaks = bruto * 0.33
töötuskindlustus_tööandja = bruto * 0.008
tööandja_kulu = bruto + sotsiaalmaks + töötuskindlustus_tööandja

palgaraport.write("Töötaja palk ja maksud" + "\n")
palgaraport.write("\n")
palgaraport.write("Brutopalk            " + str(bruto) + "\n")  
palgaraport.write("Töötuskindlustus     " + str(töötuskindlustus) + "\n")
palgaraport.write("Kogumispension       " + str(kogumispension) + "\n")
palgaraport.write("Tulumaks             " + str(tulumaks) + "\n")
palgaraport.write("Netopalk             " + str(netopalk) + "\n")
palgaraport.write("\n")
palgaraport.write("Arvestatud tulumaksuvaba miinimumi   " + str(maksuvaba) + "\n")
palgaraport.write("\n")
palgaraport.write("Tööandja kulud ja maksud" + "\n")
palgaraport.write("\n")
palgaraport.write("Kogukulu tööandjale  " + str(tööandja_kulu) + "\n")
palgaraport.write("Brutopalk            " + str(bruto) + "\n")
palgaraport.write("Sotsiaalmaks         " + str(sotsiaalmaks) + "\n")
palgaraport.write("Töötuskindlustus     " + str(töötuskindlustus_tööandja) + "\n")

palgaraport.close()