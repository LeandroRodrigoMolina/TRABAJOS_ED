"""Escriba un programa que pregunte al usuario en qué dirección quiere iniciar un conteo (ascedente ó descendente | asc ó desc). 
Si selecciona ascendente, luego solicite el límite superior y luego cuente desde 1 a ese número. 
Si selecciona descendente, solicite el límite inferior (deberá ser un número menor que 20 y la cuenta descendente 
será desde 20 a ese número. Si ingresa otra cosa que no sea “ascendente” o “descendente” muestre 
por pantalla el mensaje: “Incorrecto. No se puede continuar”."""

def impresionLimSuperior(limite):
    for i in range(1, limite, 1):
        print(i)
    print(limite)

def impresionLimInferior(limite):
    for i in range(20, limite, -1):
        print(i)
    print(limite)  

print("Ingrese 1 para un conteo ascendente, 2 para un conteo descendente")
numero = int(input())

if(numero != 1 and numero != 2):
    print("Incorrecto. No se puede continuar.")
else:
    if(numero == 1): #ascendente cuenta desde 1 a ese numero
        limite = int(input("Ingrese limite superior: "))
        impresionLimSuperior(limite)

    elif(numero == 2): #descendente tiene que ser un numero menor que 20 y la cuenta sera de 20 a ese numero
        limite = int(input("Ingrese limite inferior: "))
        
        if(limite < 20):
            impresionLimInferior(limite)
        else:
            print("Ingrese numero menor que 20.")