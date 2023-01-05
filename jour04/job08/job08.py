L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
Even = []
for i in L:
    if (i % 2 == 0):
        Even.append(i)
print("la somme des paires est:", sum(Even))