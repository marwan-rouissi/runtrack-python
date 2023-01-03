def calcule(num1, operator, num2):
    if operator == "+":
        sum=num1+num2
        return(print(sum))
    elif operator == "-":
        sum=num1-num2
        return(print(sum))
    elif operator == "/":
        sum=num1/num2
        return(print(sum))
    elif operator == "%":
        sum=num1%num2
        return(print(sum))
    else:
        print("essayez avec les paramètres suivants: 'nombre, '+,-,/ ou %', nombre'")

calcule(5,"+",2)
calcule(5,"-",2)
calcule(5,"/",2)
calcule(5,"%",2)
calcule(5,"=", 2)