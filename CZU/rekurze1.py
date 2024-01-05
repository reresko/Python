




def Funkce(x):
    if x<36:
        return Funkce(x+5)+x
    else:
        return x
    

print(Funkce(12))