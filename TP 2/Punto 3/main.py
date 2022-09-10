from punto3_Marcacion import Marcacion
from punto3_Empleado import Empleado
from punto3_Oficina import Oficina
from punto3_MarcacionTipo import MarcacionTipo
from datetime import datetime
from datetime import time

horaMarcacion_DateTime = datetime(2020,10,19)

hora_Entrada_Oficina_Time = time(10,25)
hora_Salida_Oficina_Time = time(21,25)

oficina1 = Oficina("La area de poo", hora_Entrada_Oficina_Time, hora_Salida_Oficina_Time)

empleado1 = Empleado(350, "44704088", "Lopecito", "Ricardito", oficina1)

marcacion1 = Marcacion(8000, empleado1, horaMarcacion_DateTime, 1)
print(marcacion1)