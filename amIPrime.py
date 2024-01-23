
def Cyklus(n, p):
    if n >= p**2:
        if n%p == 0:
            print("neni prvocislo")
        else:
            p = p+1
            Cyklus(n, p)
    else:
        print("je prvocislo")
        
Cyklus(int(input("zadej cislo: ")), int(2))
