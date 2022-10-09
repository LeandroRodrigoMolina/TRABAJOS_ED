from RegistroAlturaRio import RegistroAlturaRio
import beatifulsoup1

puertos = beatifulsoup1.get_puertos()
rios = beatifulsoup1.get_rios()
ultimo_registro = beatifulsoup1.get_ultimo_registro()
fecha_hora = beatifulsoup1.get_fecha_hora()
estado = beatifulsoup1.get_estado()


i = 0
lista_registro_altura_rio = []

while(i < len(puertos)):
    lista_registro_altura_rio.append(RegistroAlturaRio(puertos[i], rios[i], ultimo_registro[i], fecha_hora[i], estado[i]))
    i = i + 1

for registro in lista_registro_altura_rio:
    print(registro)