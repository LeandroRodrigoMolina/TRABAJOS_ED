# Pregunte cuanto costó la cena y la cantidad de invitados y luego calcule qué importe debería pagar cada uno.
# Alumno Leandro Molina.
print("¿Cuanto costo la cena?")
costo_Cena = float(input())

print("¿Cuantos invitados son?")
cant_Invitados = int(input())

importe_Individual = costo_Cena * cant_Invitados
print("El importe que deberia pagar cada uno de los invitados es de: $", importe_Individual.__round__(2))