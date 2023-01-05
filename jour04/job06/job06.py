L = list(range(5))
print(L)
i = L[0]
j = L[-1]
L[0] = j
L[-1] = i
print(L)