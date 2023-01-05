L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
inter = []

multi = 1
for i in L:
    if (i>=25) and (i<=90):
        inter.append(i)
        multi = multi * i 
print("le produit des valeurs comprises dans l'intervalle [25, 90] est:", multi)