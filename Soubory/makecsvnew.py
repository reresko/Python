#!/usr/bin/env python3

import os
from datetime import datetime, timedelta

soubor = "uzivatele.csv"

cwd = os.getcwd()
cesta = os.path.join(cwd, soubor)

def spocitejDatum(vek):

    dnesniRok = datetime.now().year
    dnesniMesic = datetime.now().month
    dnesniDen = datetime.now().day

    narozeniRok = dnesniRok - vek
    narozeniMesic = dnesniMesic
    narozeniDen = dnesniDen

    while vek > dnesniRok or (vek == dnesniRok and (dnesniMesic > 1 or dnesniDen > 1)):
        narozeniRok -= 1
        narozeniMesic -= 1
    if narozeniMesic == 0:
        narozeniMesic = 12
        narozeniRok -= 1
    if narozeniMesic in [1, 3, 5, 7, 8, 10, 12]:
        narozeniDen += 31
    elif narozeniMesic in [4, 6, 9, 11]:
        narozeniDen += 30
    else:
        # Přestupný rok
        if narozeniRok % 4 == 0 and (narozeniRok % 100 != 0 or narozeniRok % 400 == 0):
            narozeniDen += 29
        else:
            narozeniDen += 28
    while narozeniDen > 31:
        narozeniMesic += 1
        narozeniDen -= 31
    if narozeniMesic > 12:
        narozeniMesic = 1
        narozeniRok += 1

    datum = datetime(narozeniRok, narozeniMesic, narozeniDen)

    return datum.strftime("%d.%m.%Y")

class Aplikace:

    def pridejUzivatele():

        with open(cesta, 'w') as f:
            while True:
                jmeno = input("Zadejte jmeno: ")
                vek = int(input("Zadejte vek: "))
                narozeni = spocitejDatum(vek)

                f.write(f"{jmeno},{vek},{narozeni}\n")

                pridejRadek = input("Chcete pridat dalsi radek? (y/n)? ")

                if pridejRadek.lower() != 'y':
                    break
        print("Uspesne zapsano do CSV souboru!")

a = Aplikace
a.pridejUzivatele()







