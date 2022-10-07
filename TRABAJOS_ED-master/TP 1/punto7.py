"""Cree una lista formada por cuatro elementos de tres dígitos y muestre esa lista al
usuario (un número por línea). Solicite al usuario el ingreso de otro número de tres
dígitos. Si el número ingresado forma parte de la lista, muestre la posición en la
lista que ocupa ese número. En caso contrario muestre el mensaje: “El valor
ingresado no es parte de la lista”."""

def forma_parte_lista(numero):
    punto = True
    
    if(numero >= 100 and numero < 1000):
        for i in lista:
            if(numero == i):
                punto = False
                print("El numero se encuentra en la lista en la posicion: ", lista.index(i))
                
        if(punto == True):
            print("El valor ingresado no es parte de la lista.")
    else:
        print("El numero tiene que ser de 3 digitos.")

lista = [132,254,389,445]
for i in lista:
    print(i)

ingresar = int(input("Ingrese un numero de tres digitos que forme parte de la lista: "))
forma_parte_lista(ingresar)