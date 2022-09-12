from punto3_Marcacion import Marcacion
from punto3_Empleado import Empleado
from punto3_Oficina import Oficina
from punto3_MarcacionTipo import MarcacionTipo
from punto3_MarcacionesAdmin import MarcacionesAdmin
from datetime import datetime
from datetime import time

horaMarcacion_DateTime = datetime(2020,10,19, 15,29)
horaMarcacion2_DateTime = datetime(2020,5,6, 8,32)
horaMarcacion3_DateTime = datetime(2019,10,19, 15,29)

hora_Entrada_Oficina_Time = time(10,25)
hora_Salida_Oficina_Time = time(21,25)

oficina1 = Oficina("La area de poo", hora_Entrada_Oficina_Time, hora_Salida_Oficina_Time)

empleado1 = Empleado(350, "44704088", "Lopecito", "Ricardito", oficina1)
empleado1_Copia = Empleado(350, "44704088", "Lopecito", "Ricardito", oficina1)
empleado2 = Empleado(69696969, "44704088", "AGUIRRE", "JOSE", oficina1)

marcacion_Tipo1 = MarcacionTipo(13, 20)
marcacion_Tipo2 = MarcacionTipo(10, 22)

marcacion1 = Marcacion(8000, empleado1, horaMarcacion_DateTime, marcacion_Tipo1)
marcacion2 = Marcacion(8000, empleado1_Copia, horaMarcacion2_DateTime, marcacion_Tipo2)

marcacion3 = Marcacion(8690, empleado2, horaMarcacion3_DateTime, marcacion_Tipo1)
#print(marcacion1)
#print(marcacion1.numRegistro) #Llamando al get
# marcacion1.numRegistro = 23 probando el set si da error

marcacion_admin1 = MarcacionesAdmin()
marcacion_admin1.agregar(marcacion1)
marcacion_admin1.agregar(marcacion3)
marcacion_admin1.agregar(marcacion2)

# print(marcacion1 == marcacion2)
# print("CON REPETIDOS: \n", marcacion_admin1)
# print("*"*60)
# print("SIN EMPLEADOS REPETIDOS:\n",marcacion_admin1.empleados())
# print("*"*60)
# print("FILTRADO POR EMPLEADO SE BUSCA POR AGUIRRE: \n", marcacion_admin1.filtrar_por_empleado(empleado2))
# print("*"*60)
# print("FILTRADO POR TIPO SE BUSCA POR marcacion1:", marcacion_admin1.filtrar_por_tipo(marcacion3))

# print("DATETIME: ",marcacion1.fecha_Hora.hour, "WA", marcacion1.fecha_Hora.minute)
# print("*"*60)
# print("TIME", marcacion1.empleado.oficina.hora_entrada.hour, "WA",marcacion1.empleado.oficina.hora_entrada.minute)

#print(marcacion_admin1.llegadas_tarde())

print(marcacion_admin1)
marcacion_admin1.ordenar_legajo()
print("'ORDENADO POR LEGAJO Y POR FECHA/HORA': ", marcacion_admin1)