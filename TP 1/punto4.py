"""Solicite al usuario el ingreso de un número entre 10 y 20. Si ingresa un número 
menor que 10 muestre el mensaje “Valor inferior” y solicite que intente
nuevamente. Si el valor ingresado es superior a 20 muestre el mensaje “Valor 
superior” y solicite que intente nuevamente. Repita esta situación hasta que el 
valor ingresado sea válido, en dicho caso, muestre el mensaje: “Gracias!!!”."""
punto = False
print("Ingrese un valor entre 10 y 20: ")

while(punto == False):
    numero = int(input())
    if(numero < 10):
        print("Valor inferior. Ingrese un valor nuevamente.")
    elif(numero > 20):
        print("Valor superior. Ingrese un valor nuevamente.")
    else:
        print("Gracias!!!")
        punto = True