

def calculadora(numero1 , numero2, basica=False):

    suma = numero1+numero2
    resta = numero1-numero2
    muliplicacion = numero1*numero2
    divicion = numero1/numero2

 
    cadena = ""
    if basica != False:
        cadena +="La suma es: " + str(suma)
        cadena += '\n'
        cadena +="La resta es: " + str(resta)
        cadena += '\n'
    else:
        cadena +="La multiplicacion es: "+ str(muliplicacion)
        cadena += '\n'
        cadena +="La division es: " + str(divicion)
        cadena += '\n'

    return  cadena

print(calculadora(1,2, basica=True))

