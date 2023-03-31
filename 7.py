import requests
import csv

geo=[]
maa=[]
pind=[]
lõpp=[]
list_1=[]
list_2=[]

def file():
    global geo
    a = open("katastritunnused.txt","r")
    for i in a:
        i = i.strip()
        geo.append(i)
        geo.sort()
    a.close()
    req()
    
def req():
    global geo
    global maa
    for i in geo:
        a = str(i)
        b = requests.get("https://geoportaal.maaamet.ee/url/xgis-ky.php?ky="+a+"&out=json")
        maa.append(b.text)        
    pindala()
        
def pindala():
    global lõpp
    global list_1
    global list_2
    global pind
    global maa
    b = []
    d = []
    for i in maa:
        start_index = i.find("Pindala")
        start_index = start_index
        end_index = i.find("m²")
        loend = start_index + 11
        start_index_2 = i.find("Pindala")
        end_index_2 = i.find("ha")        
        loend_2 = start_index_2 + 11       
        while loend <= end_index:
            a = i[loend]
            b.append(a) 
            loend = loend + 1
            c = ''.join(map(str,b))
            c = str(c).replace("m", ",")
            c = c.split(",")
            while("" in c):
                c.remove("")
            c= [int(v2) for v2 in c]
            list_1 = c
        while loend_2 <= end_index_2: 
            f = i[loend_2]
            d.append(f)
            loend_2 = loend_2 + 1
            e = ''.join(map(str,d))
            e = str(e).replace("h",",")
            g = e.split(",")
            while("" in g):
                g.remove("")
            g = [float(l) for l in g]
            g = [v*10000 for v in g]
            g = [int(v1) for v1 in g]
            list_2 = g
    global pind
    nm = 0
    nha = 0
    p = []
    for i in maa:
        ha_index = i.find("ha")
        m2_index = i.find("m²")
        if m2_index > ha_index:
            pind.append(list_1[nm])
            nm = nm + 1
        else:
            pind.append(list_2[nha])
            nha = nha + 1
    for j in pind:
        str(j).replace(" ","")
        p.append(j)
    pind = p
    np = 0
    nl = 0
    s = []
    for k in geo:
        s.append(k)
        s.append(pind[np])
        np = np + 1
        lõpp.append(list(s))
        nl = nl + 1
        s.clear()
    sorteerija()
    
def sorteerija():
    global lõpp
    lõpp = sorted(lõpp, key = lambda x:x[1], reverse = True)
    kirjutaja()

def kirjutaja():
    global lõpp
    with open("7.csv", "w",newline="") as seitse:
        write = csv.writer(seitse, delimiter=";")
        write.writerows(lõpp)

file()