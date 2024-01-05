def Alik():
    i = input("coje: ")
    if int(i)>4:
        i = input("coje: ")
    else:
        Alik()
        i = input("coje: ")
        Alik()
    print(int(i)-1)
    
Alik()