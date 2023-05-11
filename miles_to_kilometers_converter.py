#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def converter(miles):
    km = miles * 1.6
    print(str(km) + "km")


converter(int(input("Zadej délku v mílích: ")))