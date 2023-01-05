L = [ 2, 5, 1, 6, 8, 9, 3, 4]

size = 0
for i in L:
    size +=1
for i in range(0, size):
    for j in range(i, size):
        if L[i]>L[j]:
            L[i], L[j] = L[j], L[i]
print(L)
