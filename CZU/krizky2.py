rows = 8
cols = 7

for a in range(rows):
    for b in range(cols):
        if a<2 or a==7 or b==a-1:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()  # Move to the next line after completing a row