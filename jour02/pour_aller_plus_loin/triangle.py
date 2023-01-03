def triangle(a, b, c):
    if a+b > c and a+c > b and b+c > a:
        print("il est possible de construire un triangle")
    else:
        print("il n'est pas possible de contruire un triangle")
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + c*c:
        print("rectangle")
    elif a == b or b == c or a == c:
        print("isocele")
    elif a == b == c:
        print("equilateral")
    elif a+b > c and a+c > b and b+c > a:
        print("quelconque")
    


triangle(6,7,8)