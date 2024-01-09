
def Prog():
    a=5
    b=1
    while int(a)<8:
        while int(b)<4:
            c=a
            while int(c)<int(a)+3:
                if int(c)==6:
                    a=a+2
                else:
                    pass
                c=c+1
                print("A", end=" ")
            b=b+1
            print("B", end=" ")
        print("C", end=" ")
        if int(a)==5:
            a=a-1
        else:
            a=a+1

Prog()