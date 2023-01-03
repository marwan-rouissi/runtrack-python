def pos_or_neg(nombre):
    if nombre > 0:
        sum="positif"
        return(print(sum))
    elif nombre < 0:
        sum="negatif"
        return(print(sum))
    else:
        print("entrer un nombre autre que 0")

pos_or_neg(5)
pos_or_neg(-5)
pos_or_neg(0)