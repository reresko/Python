rows = 8
cols = 8

for a in range(rows):
    for b in range(cols):
        if a==0 or a==7 or (b>3-a and b<6-a):
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()  # Move to the next line after completing a row

