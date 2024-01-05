
#fuck yeeah ono to fungujeeeeee

def Alik():
    a = input("piš1: ")
    if int(a)==0:
        a = input("piš2: ")
    else:
        if int(a)>5:
            a = input("piš3: ")
            a = input("piš4: ")
            Alik()
        else:
            Alik()
            a = input("piš5: ")
            a = input("piš6: ")
    print(a)
    
Alik()