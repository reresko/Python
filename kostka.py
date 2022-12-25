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




kostka = Kostka()
print(Kostka.hod)