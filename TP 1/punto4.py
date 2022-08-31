"""Solicite al usuario el ingreso de un número entre 10 y 20. Si ingresa un número 
menor que 10 muestre el mensaje “Valor inferior” y solicite que intente
nuevamente. Si el valor ingresado es superior a 20 muestre el mensaje “Valor 
superior” y solicite que intente nuevamente. Repita esta situación hasta que el 
valor ingresado sea válido, en dicho caso, muestre el mensaje: “Gracias!!!”."""

def mayorMenor(numero):
    punto = True
    while(punto == True):
        if(numero < 10):
            print("Valor inferior. Ingrese un valor nuevamente.")
            numero = int(input())
        elif(numero > 20):
            print("Valor superior. Ingrese un valor nuevamente.")
            numero = int(input())
        else:
            print("Gracias!!!")
            punto = False

print("Ingrese un valor entre 10 y 20 (incluidos): ")
numero = int(input())
mayorMenor(numero)