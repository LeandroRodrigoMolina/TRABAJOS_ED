#Solicite al usuario el ingreso de un número entero entre 1 y 12 y muestre por pantalla las tablas de multiplicación del 1 al 10.

print("Ingrese un numero entero entre 1 y 12")
i = 0
punto = True
numero = int(input());
print()

while(punto == True):
    if(numero >= 1 and numero <= 12):
        while(i <= 10):
            print(numero,"x", i,":",numero * i)
            i += 1;
        punto = False
    else:
        print("Ingrese un numero valido entre 1 y 12.")
        numero = int(input());
        