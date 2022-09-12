from datetime import datetime
from punto3_Empleado import Empleado
from punto3_MarcacionTipo import MarcacionTipo

class Marcacion():
    ultimo_num_registro = 0;
    contador_instancias = 0;
    def __init__(self, numRegistro : int, empleado : Empleado, fecha_Hora : datetime, tipo: MarcacionTipo):
        self.__numRegistro = numRegistro
        self.empleado = empleado
        self.fecha_Hora = fecha_Hora
        self.tipo = tipo

        self.ultimo_num_registro = numRegistro
        self.contador_instancias = self.contador_instancias  + 1;

    @property
    def numRegistro(self):
        return self.__numRegistro

    @numRegistro.setter
    def numRegistro(self, a):
        raise ValueError("NO SE PUEDE.")
    def __str__(self):
        return "Numero registro: %d\n\nEmpleado:\n%s\nFecha y hora: %s\nTipo: %s" % (self.__numRegistro, self.empleado, self.fecha_Hora, self.tipo)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Marcacion):
            return (self.__numRegistro == o.__numRegistro)

        return False

    