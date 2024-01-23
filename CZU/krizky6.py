rows = 9
cols = 8

for a in range(rows):
    for b in range(cols):
        if a==8 or b==7 or (b==a and a>0):
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()