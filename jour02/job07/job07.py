def spe(langage):
    if langage == str("javascript"):
        sum="tu es un developpeur web"
        return(print(sum))
    elif langage == "python":
        sum="tu es un developpeur IA"
        return(print(sum))
    elif langage == "java":
        sum="tu es un developpeur logiciel"
        return(print(sum))
    elif langage == "reactjs":
        sum="tu es un developpeur mobile"
        return(print(sum))
    else:
        sum="un jour, je serai le meilleur developpeur..."
        return(print(sum))

spe("javascript")
spe("python")
spe("java")
spe("reactjs")
spe("bootstrap")