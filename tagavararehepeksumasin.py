sõne = str("tagavararehepeksumasin")

print("a tähti on", sõne.count("a"))
print("h indeks on",sõne.index("h"))

asendus = sõne.replace("e","a").replace("u","a").replace("i","a").split("a")

print(asendus)

viimased5 = sõne[-5:]
print("viimased 5 tähte on ", viimased5)