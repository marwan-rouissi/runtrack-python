def draw_rectangle(h, w):
    large="|"
    long="-"
    center=" "
    nt= 1*w-2
    i=2
    print (large+long * nt+large)
    while i < h :
        print (large+ center * nt+large)
        i+=1
    print (large+long * nt+large)

draw_rectangle(3, 10)