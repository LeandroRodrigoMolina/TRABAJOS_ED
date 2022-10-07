from datetime import time
class Oficina:
    def __init__(self, nombre : str, hora_entrada:time, hora_salida:time):
        self.nombre = nombre
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida

    def __str__(self):
        return "\nNombre: %s\nEntrada: %s\nSalida: %s" % (self.nombre, self.hora_entrada, self.hora_salida)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Oficina):
            return (self.nombre == self.nombre)

        return False