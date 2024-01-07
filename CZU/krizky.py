rows = 7
cols = 10

for a in range(rows):
    for b in range(cols):
        if b == 2 or (a >= 0 and b >= 6 + a):
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()  # Move to the next line after completing a row