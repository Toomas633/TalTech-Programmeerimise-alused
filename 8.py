from tkinter import *
from tkinter import ttk
from tkinter import font
import re

uusklient = {}
poolik_taotlus = {}

aken = Tk('Ülesanne8')
aken.title("Ülesanne8")
raam = ttk.Frame(aken,
                padding=10,
                borderwidth=5,
                relief="sunken")
sisu= ttk.Frame(raam,
                padding=(15,15,20,20),
                borderwidth=5,
                relief="groove",
                width=300,
                height=400)

tingimused= ttk.Frame(raam,
                padding=(15,15,20,20),
                borderwidth=10,
                relief="groove",
                width=300,
                height=400)

pealkirja_font = font.Font(family='Consolas', name='pealkiri', size=12, weight='bold')
pealkiri_silt = ttk.Label(raam,
                         text="Registreerimisvorm",font=pealkirja_font)
eesnimi_silt = ttk.Label(sisu,
                         text="Eesnimi")
perenimi_silt = ttk.Label(sisu,
                          text="Perenimi")
vanus_silt = ttk.Label(sisu,
                       text="Vanus")
ting_silt = ttk.Label(tingimused,
                       text="Tingimused",font=pealkirja_font)
sugu_silt = ttk.Label(sisu,
                       text="Sugu")
email_silt = ttk.Label(sisu,
                       text="E-post")
eraldaja = ttk.Separator(tingimused, orient=HORIZONTAL)
eesnimi = ttk.Entry(sisu)
perenimi = ttk.Entry(sisu)
vanus = ttk.Entry(sisu)
email  = ttk.Entry(sisu)

valikeel_1 = BooleanVar(value=False)
valikeel_2 = BooleanVar(value=False)
valikeel_3 = BooleanVar(value=True)

yld = ttk.Checkbutton(tingimused, text="Üldtingimused", variable=valikeel_1, onvalue=True)
andmed = ttk.Checkbutton(tingimused, text="Kliendiandmete töötlemise kord", variable=valikeel_2, onvalue=True)
kypsis = ttk.Checkbutton(tingimused, text="Veebilehe küpsiste kasutamise eeskiri", variable=valikeel_3, onvalue=True)


sugu = StringVar()
mees = ttk.Radiobutton(sisu, text='Mees', variable=sugu, value='mees')
naine = ttk.Radiobutton(sisu, text='Naine', variable=sugu, value='naine')

def saada_taotlus():
    global uusklient
    nimi_regex = '[A-Za-z-]{2,25}( [A-Za-z-]{2,25})?'
    eesnimi_status = re.fullmatch(nimi_regex, eesnimi.get())
    perenimi_status = re.fullmatch(nimi_regex, perenimi.get())
    try:
        vanus_number = vanus.get()
        vanus_number = int(vanus_number)
        vanus_staatus = 1
    except ValueError:
        vanus_staatus = 0
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_status = re.fullmatch(email_regex, email.get())
    if len(eesnimi.get()) == 0:
        valideerimine = ttk.Label(justify="center", text="Eesnimi lahter pole täidetud")
        valideerimine.place(x=200, y=510, width=250, height=25, anchor="center")
    elif eesnimi_status == None:
        valideerimine = ttk.Label(justify="center", text="Eesnimi lahter valesti täidetud")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    elif len(perenimi.get()) == 0:
        valideerimine = ttk.Label(justify="center", text="Perenimi lahter pole täidetud")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    elif perenimi_status == None:
        valideerimine = ttk.Label(justify="center", text="Perenimi lahter valesti täidetud")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    elif len(email.get()) == 0:
        valideerimine = ttk.Label(justify="center", text="Email lahter pole täidetud")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    elif email_status == None:
        valideerimine = ttk.Label(justify="center", text="E-posti adress pole õigel kujul")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")            
    elif len(vanus.get()) == 0:
        valideerimine = ttk.Label(justify="center", text="Vanus lahter pole täidetud")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    elif vanus_staatus == 0:
        valideerimine = ttk.Label(justify="center", text="Sisesta vanuse lahtrisse numbrid")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    elif vanus_number < 0:
        valideerimine = ttk.Label(justify="center", text="Vanus ei saa olla negatiivne")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    elif vanus_number > 120:
        valideerimine = ttk.Label(justify="center", text="Vanus liiga suur")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    elif len(sugu.get()) == 0:
        valideerimine = ttk.Label(justify="center", text="Vali oma sugu")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    elif valikeel_1.get() != True:
        valideerimine = ttk.Label(justify="center", text="Nõustu kõikide tingimustega")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    elif valikeel_2.get() != True:
        valideerimine = ttk.Label(justify="center", text="Nõustu kõikide tingimustega")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    elif valikeel_3.get() != True:
        valideerimine = ttk.Label(justify="center", text="Nõustu kõikide tingimustega")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center")
    else:
        valideerimine = ttk.Label(justify="center", text="Lugupeetud "+eesnimi.get().capitalize()+" "+perenimi.get().capitalize()+"!"+"\n"+"Teie taotlus on vastu võetud")
        valideerimine.place(x=200, y=510,width=250, height=25, anchor="center") 
        uusklient["eesnimi"] = eesnimi.get().capitalize()
        uusklient["perenimi"] = perenimi.get().capitalize()
        uusklient["email"] = email.get()
        uusklient["vanus"] = vanus.get()
        uusklient["sugu"] = sugu.get()
        uusklient["tingimus_1"] = valikeel_1.get()
        uusklient["tingimus_2"] = valikeel_2.get()
        uusklient["tingimus_3"] = valikeel_3.get()
        print(uusklient)
    valideerimine.grid(column=0, row=1, columnspan=2)
    
def tyhistataotlus():
    valideerimine = ttk.Label(justify="center", text="Tühistatud")
    valideerimine.place(x=200, y=510,width=250, height=25, anchor="center") 
    global poolik_taotlus
    poolik_taotlus["eesnimi"] = eesnimi.get().capitalize()
    poolik_taotlus["perenimi"] = perenimi.get().capitalize()
    poolik_taotlus["email"] = email.get()
    poolik_taotlus["vanus"] = vanus.get()
    poolik_taotlus["sugu"] = sugu.get()
    poolik_taotlus["tingimus_1"] = valikeel_1.get()
    poolik_taotlus["tingimus_2"] = valikeel_2.get()
    poolik_taotlus["tingimus_3"] = valikeel_3.get()
    print(poolik_taotlus)

ok = ttk.Button(raam, text="Saada", command=saada_taotlus)
tyhista = ttk.Button(raam, text="Tühista",command=tyhistataotlus)

raam.grid(column=0, row=0)
pealkiri_silt.grid(column=0, row=0, columnspan = 2,padx=20, pady=20)
sisu.grid(column=0, row=1, columnspan = 2)

eesnimi_silt.grid(column=0, row=0, sticky=E)
eesnimi.grid(column=1, row=0, pady=5, padx=5)
perenimi_silt.grid(column=0, row=1, sticky=E)
perenimi.grid(column=1, row=1, pady=5, padx=5)
email_silt.grid(column=0, row=2, sticky=E)
email.grid(column=1, row=2, pady=5, padx=5)
vanus_silt.grid(column=0, row=3, sticky=E)
vanus.grid(column=1, row=3, pady=5, padx=5)


sugu_silt.grid(column = 0, row = 4, rowspan=2, sticky=E)
mees.grid(column=1, row=4, pady=5, padx=5, sticky=W)
naine.grid(column=1, row=5, pady=5, padx=5, sticky=W)

#Tingimused
tingimused.grid(column=0, row=3,columnspan = 2)
ting_silt.grid(column = 0, row = 0, columnspan = 2)
eraldaja.grid(column = 0, row = 1, columnspan = 2)
yld.grid(column=0, row=2, columnspan = 2, sticky=W)
andmed.grid(column=0, row=3, columnspan = 2, sticky=W)
kypsis.grid(column=0, row=4, columnspan = 2, sticky=W)

ok.grid(column=0, row=4,padx=20, pady=20)
tyhista.grid(column=1, row=4)

aken.mainloop()