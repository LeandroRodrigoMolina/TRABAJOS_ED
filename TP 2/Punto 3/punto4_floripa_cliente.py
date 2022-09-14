from punto3_Marcacion import Marcacion
from punto3_Empleado import Empleado
from punto3_Oficina import Oficina
from punto3_MarcacionTipo import MarcacionTipo
from punto3_MarcacionesAdmin import MarcacionesAdmin
from datetime import datetime
from datetime import time

hora_Entrada_Oficina1_Time = time(10,25)
hora_Salida_Oficina1_Time = time(21,25)
hora_Entrada_Oficina2_Time = time(4,00)
hora_Salida_Oficina2_Time = time(22,45)
hora_Entrada_Oficina3_Time = time(12,00)
hora_Salida_Oficina3_Time = time(21,00)

horaMarcacion_DateTime = datetime(2020,10,19, 15,29)
horaMarcacion2_DateTime = datetime(2020,5,6, 8,32)
horaMarcacion3_DateTime = datetime(2019,10,19, 15,29)
horaMarcacion4_DateTime = datetime(2021,9,4,10,16)
horaMarcacion5_DateTime = datetime(1970,1,20,9,20)
horaMarcacion6_DateTime = datetime(1850,2,27,5,22)
horaMarcacion7_DateTime = datetime(2023,4,11,14,20)
horaMarcacion8_DateTime = datetime(2022,9,13,11,22)

oficina1 = Oficina("El area de POO", hora_Entrada_Oficina1_Time, hora_Salida_Oficina1_Time)
oficina2 = Oficina("EL AREA", hora_Entrada_Oficina2_Time, hora_Salida_Oficina2_Time)
oficina3 = Oficina("RECURSOS HUMANOIDES", hora_Entrada_Oficina3_Time, hora_Salida_Oficina3_Time)

empleado1 = Empleado(10, "44704088", "Lopecito", "Ricardito", oficina1)
empleado2 = Empleado(12, "21254785", "Rothbard", "Murray", oficina1)
empleado3 = Empleado(20, "69694524", "Friedman", "David", oficina2)
empleado4 = Empleado(25, "44444444", "Ravier", "Adrian", oficina2)
empleado5 = Empleado(66, "01247824", "De Soto", "Jesus Huerta", oficina3)

marcacion_Tipo1 = MarcacionTipo(13, 20)
marcacion_Tipo2 = MarcacionTipo(10, 22)
marcacion_Tipo3 = MarcacionTipo(4, 22)

marcarcacion1 = Marcacion(empleado1, horaMarcacion_DateTime, marcacion_Tipo1)
marcarcacion2 = Marcacion(empleado2, horaMarcacion2_DateTime, marcacion_Tipo2)
marcarcacion3 = Marcacion(empleado3, horaMarcacion3_DateTime, marcacion_Tipo3)
marcarcacion4 = Marcacion(empleado4, horaMarcacion4_DateTime, marcacion_Tipo1)
marcarcacion5 = Marcacion(empleado4, horaMarcacion5_DateTime, marcacion_Tipo2)
marcarcacion6 = Marcacion(empleado3, horaMarcacion6_DateTime, marcacion_Tipo1)
marcarcacion7 = Marcacion(empleado2, horaMarcacion7_DateTime, marcacion_Tipo2)
marcarcacion8 = Marcacion(empleado1, horaMarcacion8_DateTime, marcacion_Tipo1)
marcarcacion9 = Marcacion(empleado3, horaMarcacion4_DateTime, marcacion_Tipo3)
marcarcacion10 = Marcacion(empleado2, horaMarcacion5_DateTime, marcacion_Tipo2)
marcarcacion11 = Marcacion(empleado4, horaMarcacion3_DateTime, marcacion_Tipo1)
marcarcacion12 = Marcacion(empleado1, horaMarcacion7_DateTime, marcacion_Tipo3)
marcarcacion13 = Marcacion(empleado4, horaMarcacion_DateTime, marcacion_Tipo2)
marcarcacion14 = Marcacion(empleado2, horaMarcacion6_DateTime, marcacion_Tipo1)
marcarcacion15 = Marcacion(empleado5, horaMarcacion5_DateTime, marcacion_Tipo3)

marcacionAdmin1 = MarcacionesAdmin()
marcacionAdmin1.agregar(marcarcacion1)
marcacionAdmin1.agregar(marcarcacion2)
marcacionAdmin1.agregar(marcarcacion3)
marcacionAdmin1.agregar(marcarcacion4)
marcacionAdmin1.agregar(marcarcacion5)
marcacionAdmin1.agregar(marcarcacion6)
marcacionAdmin1.agregar(marcarcacion7)
marcacionAdmin1.agregar(marcarcacion8)
marcacionAdmin1.agregar(marcarcacion9)
marcacionAdmin1.agregar(marcarcacion10)
marcacionAdmin1.agregar(marcarcacion11)
marcacionAdmin1.agregar(marcarcacion12)
marcacionAdmin1.agregar(marcarcacion13)
marcacionAdmin1.agregar(marcarcacion14)
marcacionAdmin1.agregar(marcarcacion15)

lista_empleados = marcacionAdmin1.empleados()
lista_filtrado_empleado = marcacionAdmin1.filtrar_por_empleado(empleado2)
lista_filtrado_tipo = marcacionAdmin1.filtrar_por_tipo(marcarcacion15)
lista_llegadas_tarde = marcacionAdmin1.llegadas_tarde()
print("EMPLEADOS: \n", lista_empleados)

print("*"*80)
print("FILTRADO EMPLEADO2: \n", lista_filtrado_empleado)

print("*"*80)
print("FILTRADO POR TIPO: \n", lista_filtrado_tipo)

print("*"*80)
print("LLEGADAS TARDE: \n", lista_llegadas_tarde)

print("*"*80)
marcacionAdmin1.ordenar_legajo()
print("ORDENADO POR LEGAJO Y LUEGO FECHA/HORA: \n", marcacionAdmin1)

print("*"*80)
marcacionAdmin1.ordenar_apellido_nombre()
print("ORDENADO POR APELLIDO Y NOMBRE: \n", marcacionAdmin1)