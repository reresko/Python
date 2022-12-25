#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Clovek:

	def __init__(self, jmeno, prijmeni, vek):
		self.__jmeno = jmeno
		self.__prijmeni = prijmeni
		self.__vek = vek
	
	def getJmeno(self):
		return self.__jmeno
	
	def getPrijmeni(self):
		return self.__prijmeni
	
	def setJmeno(self, jmeno):
		self.__jmeno = jmeno
	
	def setPrijmeni(self, prijmeni):
		if(self.__vek > 17):
			self.__prijmeni = prijmeni
		else:
			print("Nelze zmenit pred 18. rokem.")


objekt = Clovek("Martina", "Novakova", 17)
objekt.setPrijmeni("Prochazkova")
objekt.vek=20
objekt.setPrijmeni("Prochazkova")

print(objekt.getJmeno(), objekt.getPrijmeni())



