"""Defina colores = ['Azul', 'Verde', 'Rojo', 'Amarillo', 'Violeta', 'Rosa',
'Negro', 'Celeste', 'Gris', 'Blanco']. Solicite al usuario el ingreso del número
entero inicio con valor entre 0 y 4 y del número entero fin entre 5 y 9. Muestre la
sublista formada por los colores entre los números inicio y fin."""

def ingreso_inicio_fin(inicio, fin):
    punto = True

    while(punto == True):
        if((inicio >= 0 and inicio <= 4) and (fin >= 5 and fin <= 9)):
            punto = False
            return sub_lista(inicio, fin)
        else:
            print("Ingrese inicio o fin invalidos.")
            inicio = int(input("Ingrese nuevamente un numero inicio entre 0 a 4: "))
            fin = int(input("Ingrese nuevamente un numero fin entre 5 y 9: "))   

def sub_lista(inicio, final):
    lista = colores[inicio:fin + 1]
    return lista

colores = ['Azul', 'Verde', 'Rojo', 'Amarillo', 'Violeta', 'Rosa',
            'Negro, Celeste','Gris', 'Blanco']

inicio = int(input("Ingrese un numero inicio entre 0 a 4: "))
fin = int(input("Ingrese un numero fin entre 5 y 9: "))
lista = ingreso_inicio_fin(inicio, fin)
print(lista)