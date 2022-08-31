# Solicite al usuario el ingreso de dos números e indique cuál es el mayor.
# Alumno Leandro Molina.
print("Ingrese dos numeros")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if(num1 > num2):
    num_Mayor = num1
    print("El numero mayor es", num_Mayor)
elif(num2 > num1):
    num_Mayor = num2
    print("El numero mayor es", num_Mayor)
else:
    print("Los numeros son iguales ", num1, " = ", num2)
