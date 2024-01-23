def Alik():
    i=input("coje: ")
    if int(i)==0:
        i=input("coje: ")
    else:
        Alik()
        Alik()
        Alik()
    print(int(i)+1)
    
Alik()