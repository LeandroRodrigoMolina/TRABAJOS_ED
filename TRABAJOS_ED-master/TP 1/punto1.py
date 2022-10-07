#Solicite al usuario el ingreso de un número entero entre 1 y 12 y muestre por pantalla las tablas de multiplicación del 1 al 10.


def multiplicacionHasta10(numero):
    i = 0
    while(i <= 10):
        print(numero,"x", i,":",numero * i)
        i += 1;

print("Ingrese un numero entero entre 1 y 12")
punto = True
numero = int(input());
while(punto):
    if(numero >= 1 and numero <= 12):
        multiplicacionHasta10(numero)
        punto = False
    else:
        print("Ingrese un numero valido entre 1 y 12.")
        numero = int(input())