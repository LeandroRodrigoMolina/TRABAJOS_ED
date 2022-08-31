# Solicite al usuario el ingreso de tres números e indique cuál es el mayor.
# Alumno Leandro Molina.
print("Ingrese tres numeros")
numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))
numero_3 = int(input("Ingrese el tercer numero: "))

mayor = numero_1

if(numero_2 > mayor):
    mayor = numero_2
    
if(numero_3 > mayor):
    mayor = numero_3


print("El mayor numero es: ", mayor)
