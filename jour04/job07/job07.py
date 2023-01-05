L = [8, 24,48,2,16]
Mof3 = []
for i in L:
    if (i % 3 == 0):
        Mof3.append(i)
print("le nombre de multiples de 3 presents dans la liste est:", len(Mof3))