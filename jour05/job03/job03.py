def draw_carpet(n):
    corner="+"
    large="|"
    long="-"
    size=n+1
    center=" "

    for i in range(n): center+="#"
    print (corner+long * size+corner)

    for i in range(size):
        center=center[1:] + center[0]
        print (large + center + large)
    print (corner+long * size+corner)

draw_carpet(10)