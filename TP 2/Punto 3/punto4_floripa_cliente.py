from punto3_Marcacion import Marcacion
from punto3_Empleado import Empleado
from punto3_Oficina import Oficina
from punto3_MarcacionTipo import MarcacionTipo
from punto3_MarcacionesAdmin import MarcacionesAdmin
from datetime import datetime
from datetime import time

hora_Entrada_Oficina1_Time = time(10,25)
hora_Salida_Oficina1_Time = time(21,25)
hora_Entrada_Oficina2_Time = time()
hora_Salida_Oficina2_Time = time()
hora_Entrada_Oficina3_Time = time()
hora_Salida_Oficina3_Time = time()

horaMarcacion_DateTime = datetime(2020,10,19, 15,29)
horaMarcacion2_DateTime = datetime(2020,5,6, 8,32)
horaMarcacion3_DateTime = datetime(2019,10,19, 15,29)
horaMarcacion4_DateTime = datetime()
horaMarcacion5_DateTime = datetime()
horaMarcacion6_DateTime = datetime()
horaMarcacion7_DateTime = datetime()
horaMarcacion8_DateTime = datetime()
horaMarcacion9_DateTime = datetime()
horaMarcacion10_DateTime = datetime()
horaMarcacion11_DateTime = datetime()
horaMarcacion12_DateTime = datetime()
horaMarcacion13_DateTime = datetime()
horaMarcacion14_DateTime = datetime()
horaMarcacion15_DateTime = datetime()

oficina1 = Oficina(nombre, hora_entrada, hora_salida)
oficina2 = Oficina(nombre, hora_entrada, hora_salida)
oficina3 = Oficina(nombre, hora_entrada, hora_salida)

empleado1 = Empleado(legajo, documento, apellido, nombre, oficina)
empleado2 = Empleado(legajo, documento, apellido, nombre, oficina)
empleado3 = Empleado(legajo, documento, apellido, nombre, oficina)
empleado4 = Empleado(legajo, documento, apellido, nombre, oficina)
empleado5 = Empleado(legajo, documento, apellido, nombre, oficina)

marcacion_Tipo1 = MarcacionTipo(13, 20)
marcacion_Tipo2 = MarcacionTipo(10, 22)
marcacion_Tipo3 = MarcacionTipo(entrada, salida)

marcarcacion1 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion2 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion3 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion4 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion5 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion6 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion7 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion8 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion9 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion10 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion11 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion12 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion13 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion14 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)
marcarcacion15 = Marcacion(numRegistro, empleado, fecha_Hora, tipo)

