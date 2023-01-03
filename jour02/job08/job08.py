def food(type, saison):
    if type == "fruit" and saison == "hiver":
        sum="orange, mandarine et kiwi"
        return(print(sum))
    elif type == "fruit" and saison == "ete":
        sum="Poire, fraise, cassis"
        return(print(sum))
    elif type == "legume" and saison == "hiver":
        sum="carotte, topinambour, endive"
        return(print(sum))
    elif type == "legume" and saison == "ete":
        sum="artichaut, aubergine,navet"
        return(print(sum))
    else:
        sum="entrez une catégorie (fruit ou legume) et une saison (ete ou hiver)"
        return(print(sum))

food("fruit", "hiver")
food("fruit", "ete")
food("legume", "hiver")
food("legume", "ete")
food("fruit", "winter")
