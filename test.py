#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Zasilka:
    def __init__(self, nazev, hmotnost, delka, vyska, hloubka, jednotkyDelky, jednotkyHmotnosti):
        self._nazev = nazev
        self._hmotnost = hmotnost
        self._delka = delka
        self._vyska = vyska
        self._hloubka = hloubka
        self._jednotkyDelky = jednotkyDelky
        self._jednotkyHmotnosti = jednotkyHmotnosti

    def __str__(self):
        return str(self._jednotkyDelky)
        
    def __str__(self):
        return str(self._jednotkyHmotnosti)

    def _jednotkyDelky(self):
        return (self._jednotkyDelky)

    def _jednotkyHmotnosti(self):
        return (self._jednotkyHmotnosti)

    def __str__(self):
        return str(self._nazev)

    def _nazev(self):
        print (self._nazev)
            
    def _hmotnost(self):
        return (self._hmotnost)

    def _delka(self):
        print(self._delka)

    def _vyska(self):
        print(self._vyska)

    def _hloubka(self):
        print(self._hloubka)
        


zasilka = Zasilka("Stativ", 2300, 35, 42, 134, "cm", "g")
if zasilka._hmotnost < 5000:
    pass
else:
    print("Zásilka překračuje hmotnostní limity skladu.")
print(zasilka._nazev, zasilka._hmotnost, zasilka._jednotkyHmotnosti, zasilka._delka, zasilka._jednotkyDelky, zasilka._vyska, zasilka._jednotkyDelky, zasilka._hloubka, zasilka._jednotkyDelky)