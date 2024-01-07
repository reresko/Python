rows = 8
cols = 7

for a in range(rows):
    for b in range(cols):
        if (a>1 and a<7) and (b>0 and b<5):
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()  # Move to the next line after completing a row