#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import random
import tkinter

root = tkinter.Tk()
root.title("Kalkulačka")

expression = ""

import random
rng = random.randint(1, 10)


def add(value):
    global expression
    expression += value
    print(expression)
    label_vysledek.config(text=expression)

def clear():
    global expression
    expression = ""
    label_vysledek.config(text=expression)

def vypocitej():
    global expression
    vysledek = ""
    if expression != "":
        try:
            vysledek = eval(expression)
        except:
            vysledek = "ses kokot"
            expression = ""
    label_vysledek.config(text=vysledek)
    expression = str(vysledek)


label_vysledek = tkinter.Label(root, text="")
label_vysledek.grid(row=0, column=0, columnspan=4)

button_7 = tkinter.Button(root, text="7", command=lambda: add("7"))
button_7.grid(row=1, column=0)

button_8 = tkinter.Button(root, text="8", command=lambda: add("8"))
button_8.grid(row=1, column=1)

button_9 = tkinter.Button(root, text="9", command=lambda: add("9"))
button_9.grid(row=1, column=2)

button_deleno = tkinter.Button(root, text="/", command=lambda: add("/"))
button_deleno.grid(row=1, column=3)

button_4 = tkinter.Button(root, text="4", command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(root, text="5", command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, text="6", command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_krat = tkinter.Button(root, text="*", command=lambda: add("*"))
button_krat.grid(row=2, column=3)

button_1 = tkinter.Button(root, text="1", command=lambda: add("1"))
button_1.grid(row=3, column=0)

button_2 = tkinter.Button(root, text="2", command=lambda: add("2"))
button_2.grid(row=3, column=1)

button_3 = tkinter.Button(root, text="3", command=lambda: add("3"))
button_3.grid(row=3, column=2)

button_minus = tkinter.Button(root, text="-", command=lambda: add("-"))
button_minus.grid(row=3, column=3)

button_0 = tkinter.Button(root, text="0", width=6, command=lambda: add("0"))
button_0.grid(row=4, column=0, columnspan=2)

button_desetinne = tkinter.Button(root, text=".", command=lambda: add("."))
button_desetinne.grid(row=4, column=2)

button_plus = tkinter.Button(root, text="+", command=lambda: add("+"))
button_plus.grid(row=4, column=3)

button_rovnitko = tkinter.Button(root, text="=", width=10, command=lambda: vypocitej())
button_rovnitko.grid(row=5, column=0, columnspan=3)

button_clear = tkinter.Button(root, text="C", command=lambda: clear())
button_clear.grid(row=5, column=3)

root.mainloop()