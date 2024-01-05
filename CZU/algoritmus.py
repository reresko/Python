
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
                print(a)
            b=b+1
            print(b)
        print(c)
        if int(a)==5:
            a=a+1
        else:
            pass

Prog()