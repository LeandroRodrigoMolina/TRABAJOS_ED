"""Escriba un programa Python realice su cometido invocando a las siguientes
funciones:
a) Solicita al usuario dos números enteros para usar como límite inferior y otro
superior y genera un número aleatorio entre esos dos números.

b) Imprime por pantalla el mensaje: “Estoy pensando en el número…” y pide al
usuario adivinar ese número.

c) Controla que el número aleatorio es el mismo que el ingresado por el usuario y
si es así, muestra por pantalla el mensaje: “Correcto, has ganado!!”, en caso
contrario se ejecuta iterativamente indicando al usuario que el número
ingresado es mayor o menor y vuelve a solicitar el ingreso hasta que el número
es adivinado."""
from random import randint

def ingresoLimites(lim_inferior, lim_superior):
    if(lim_inferior < lim_superior):
        aleatorio = randint(lim_inferior, lim_superior)
        return aleatorio
    else:
        print("Los numeros recibidos no son validos.")
        
def pensandoNumero(numero_adivinar):
    print("Estoy pensando en el numero...\n¡Intenta adivinarlo!")
    adivinanza(numero_adivinar)

def adivinanza(numero):
    punto = True
    num_usuario = int(input("Ingrese un numero: "))
    while(punto):
        if(num_usuario == numero):
            print("¡¡Correcto, has ganado!!\n El numero era: ", numero)
            punto = False
        elif(numero > num_usuario):
            print("¡El numero es mayor! intentalo otra vez.")
            num_usuario = int(input("Ingrese nuevamente otro numero: "))
        else:
            print("¡El numero es menor! intentalo otra vez.")
            num_usuario = int(input("Ingrese nuevamente otro numero: "))

num_1 = int(input("Ingresa el limite inferior: "))
num_2 = int(input("Ingresa el limite superior: "))
adivinar = ingresoLimites(num_1, num_2)
pensandoNumero(adivinar)

