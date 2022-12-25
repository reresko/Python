#!/usr/bin/env python3

import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET


class Uzivatel:
    """
    Tato třída bude plodit objekty načtené ze souboru .csv
    """

    def __init__(self, jmeno, vek, narozeni):
        self._jmeno = jmeno
        self._vek = vek
        self._narozeni = narozeni      # na objekt datetime kašleme (odstraněn i z importů)

    def __str__(self):                       # textová reprezentace je tu navíc, nikde se neprojevuje
        return str(self._jmeno)

class Prevod:
    def __init__(self, vstup, vystup=None):  # instance třídy Prevod očekává zadání vstupního souboru, výstupní soubor
        if vystup == None:                   # můžeme vynechat; pokud tak učiníme, bude 'None' a vygeneruje se ze vstupu
            vystup = vstup[:-4] + ".xml"
        self._vstup = vstup
        self._vystup = vystup
        self._zaznamy = []                   # zde vytvoříme seznam, kde budou objekty třídy Uzivatel

    def nacti(self):                         # metoda s minimálními změnami oproti té z hodiny (prevod.py)
        with open(self._vstup, "r", encoding="utf-8") as f:
            for s in f.readlines():
                jmeno, vek, narozeni = s.strip().split(",")
                u = Uzivatel(jmeno, vek, narozeni)
                self._zaznamy.append(u)

    def uloz(self):                             # metoda zůstala prakticky beze změn, jen názvy proměnných se vrátily
        uzivatele = ET.Element("uzivatele")

        for u in self._zaznamy:
            uzivatel = ET.SubElement(uzivatele, "uzivatel")
            uzivatel.set("vek", u._vek)
            jmeno = ET.SubElement(uzivatel, "jmeno")
            jmeno.text = str(u._jmeno)
            reg = ET.SubElement(uzivatel, "narozeni")
            reg.text = str(u._narozeni)
        xml = ET.tostring(uzivatele, xml_declaration=True, encoding="utf-8")

        f = open(self._vystup, "wb")
        f.write(xml)
        f.close()

if __name__=="__main__":                        # pokud spouštíme program z konzole (vestavná podmínka)
    p = Prevod("uzivatele.csv")
    p.nacti()                                   # metody nacti() a uloz() by mohly být spojené do jedné, např. preved()
    p.uloz()                                    # zde jsou odděleny jen pro názornost