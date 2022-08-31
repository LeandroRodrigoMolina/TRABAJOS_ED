# Solicite al usuario que ingrese por consola de comandos sus cuatro platos favoritos
# y almacénelos en un diccionario de manera que sean indexados con números a
# partir del 1. Muestre por pantalla el diccionario completo (claves y valores). A
# continuación el programa deberá preguntar al usuario qué elemento quiere quitar
# del diccionario y hacerlo. Muestre por pantalla el resultado final.
def ingresar_plato(plato_numero):
    print("Ingrese plato el", plato_numero, "favorito: ")
    plato = input()
    return plato

def eliminar_platos():
    print("¿Que elemento quiere eliminar del diccionario?, ingrese el indice (numero).")
    plato_eliminar = int(input())
    platos_favoritos.pop(plato_eliminar)

i = 1
platos_favoritos = {}
while(i<=4):
    platos_favoritos[i] = ingresar_plato(i)
    i += 1

print(platos_favoritos)
eliminar_platos()
print(platos_favoritos)