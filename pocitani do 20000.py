
file = open("pocitani_do_20000.txt", "w")

for i in range(20001):
        file.writelines(str(i)+"\n")

file.close()