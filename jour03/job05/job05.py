def primenumbr():
  for i in range(0, 1001 +1):
    if i > 1:
      for j in range(2, i):
        if (i % j) == 0:
          break
      else:
        print(i)
                    
primenumbr()