def skipnumb():
    i = 0
    for i in range(0, 100):
        if (i == 26 or i == 37 or i== 88):
            continue
        print(i)
        i += 1
skipnumb()