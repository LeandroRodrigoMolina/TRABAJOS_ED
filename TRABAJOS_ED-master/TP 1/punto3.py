"""Pida al usuario que ingrese una palabra por consola de comandos y muestre en 
orden inverso los caracteres que la forman, uno por línea."""

def ordenInverso(palabra):
    i = palabra.__len__() - 1
    while i >= 0:
        print(palabra[i])
        i -= 1

print("Ingrese una palabra: ")
palabra = input()
ordenInverso(palabra)