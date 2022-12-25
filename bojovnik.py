#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Kostka:
    """
    Trida reprezentujci kostku
    """

    def __init__(self, pocetSten=6):
        self.__pocetSten = pocetSten
    
    def getpocetSten (self):
        """
        vrati pocet sten kostky.
        """
        return self.__pocetSten

    def hod(self):
        """
        vykona hod kostkou a vrati cislo od 1 do poctu sten.
        """
        import random as _random
        return _random.randint(1, self.__pocetSten)

    def __str__(self):
        """
        vraci textovou reprezentaci kostky.
        """
        return str("Kostka s {0} stenami.".format(self.__pocetSten))


class Bojovnik:
    """
    trida reprezentujici bojovnika do areny.
    """

    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        """
        jmeno - jmeno bojovnika
        zivot - maximalni zivot bojovnika
        utok - utok bojovnika
        obrana - obrana bojovnika
        kostka - instance kostky
        """

        self.__jmeno = jmeno
        self.__zivot = zivot
        self.__maxZivot = zivot
        self.__utok = utok
        self.__obrana = obrana
        self:__kostka = kostka

    def __str__(self):
        return str(self.__jmeno)

    @property
    def nazivu(self):
        if self.__zivot > 0:
            return True
        else:
            return False

    def grafickyZivot(self):
        celkem = 20
        pocet = int(self.__zivot / self.__maxZivot * celkem)
        if pocet == 0 and self.nazivu:
            pocet = 1
        return "[{0}{1}]".format("■"*pocet," "*(celkem-pocet))

kostka = Kostka()
bojovnik = Bojovnik ("Rikis",100,20,10,Kostka)

print("Bojovnik: {0}".format(bojovnik))
print("Je nazivu: {0}".format(bojovnik.nazivu))
print("zivot {0}".format(bojovnik.grafickyZivot()))
    