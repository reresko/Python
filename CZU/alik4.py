def Alik():
    i = input("coje: ")
    if int(i)==0:
        i = input("coje: ")
    else:
        Alik()
        Alik()
        print(i)
        i = input("coje: ")
    print(i)
    
Alik()