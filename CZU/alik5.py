def Alik():
    i=input("coje: ")
    if int(i)==0:
        i=input("coje: ")
    else:
        Alik()
        print(i)
        Alik()
    print(i)
    
Alik()