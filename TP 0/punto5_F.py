# Pregunte al usuario por un número de días y calcule la cantidad de horas, minutos y segundos que transcurren en ese número de días.
# Alumno Leandro Molina.
dias = int(input("Ingrese numero de dias: "))

horas = dias * 24
minutos = horas * 60
segundos = minutos * 60

print("Dias: ", dias, "\nHoras:", horas, "\nMinutos:", minutos, "\nSegundos:", segundos)