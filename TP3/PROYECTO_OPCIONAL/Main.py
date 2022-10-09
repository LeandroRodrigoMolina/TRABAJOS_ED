from RegistroAlturaRio import RegistroAlturaRio
import beatifulsoup1
from registroAdmin import registroAdmin

puertos = beatifulsoup1.get_puertos()
rios = beatifulsoup1.get_rios()
ultimo_registro = beatifulsoup1.get_ultimo_registro()
fecha_hora = beatifulsoup1.get_fecha_hora()
estado = beatifulsoup1.get_estado()


i = 0
lista_registro_altura_rio = registroAdmin()
while(i < len(puertos)):
    lista_registro_altura_rio.agregar(RegistroAlturaRio(puertos[i], rios[i], ultimo_registro[i], fecha_hora[i], estado[i]))
    i = i + 1

lista_1 = lista_registro_altura_rio.filtrar_por_puerto("BUENOS AIRES")
lista_2 = lista_registro_altura_rio.filtrar_por_rio("PARANA")
lista_3 = lista_registro_altura_rio.filtrar_por_estado("ESTAC.")

print("LISTADO POR PUERTO BUENOS AIRES:")
for i in lista_1:
    print(i)

print("*"*80)
print("LISTADO POR RIO PARANA:")
for i in lista_2:
    print(i)

print("*"*80)
print("LISTADO POR ESTADO ESTAC.")
for i in lista_3:
    print(i)