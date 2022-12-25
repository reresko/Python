#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class a:
    zblept = input("Co/koho máš na srdci?: ")
    if zblept == "Máju":
        for row in range(6):
            for col in range(7):
                if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
                    print("*",end="")
                else:
                    print(end=" ")
            print()
    else:
        print("špatná odpověď.")