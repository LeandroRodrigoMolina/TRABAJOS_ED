"""Escriba un programa que solicite al usuario el ingreso del nombre de tres ciudades
del mundo que desea conocer y las almacene en una lista. Luego de haber
ingresado los nombres, pregúntele si quiere añadir más ciudades. Si así lo de
desea, permita el ingreso de más nombres hasta que la respuesta sea “no”.
Cuando la respuesta sea “no” muestre por pantalla el número y listado de
ciudades cargadas."""

def ingresar_ciudad(respuesta):
    if(respuesta == "si"):
        ciudad = input("Ingrese  ciudad, para cancelar escriba 'no': ")
        while(ciudad != "no"):
            lista.append(ciudad)
            ciudad = input("Ingrese  ciudad, para cancelar escriba 'no': ")

        for i in lista:
            print(i)
    else:
        print("Respuesta invalida.")
        
print("Ingrese el nombre de tres ciudadades: ")
ciudad_1 = input("Ciudad uno: ")
ciudad_2 = input("Ciudad dos: ")
ciudad_3 = input("Ciudad tres: ")
lista = [ciudad_1, ciudad_2, ciudad_3]

print("¿Quieres ingresar mas ciudadades?,'si' para el ingresar mas ciudades, para cancelar escriba: 'no'.")
respuesta = input()
ingresar_ciudad(respuesta)