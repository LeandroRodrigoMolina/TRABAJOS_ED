class RegistroAlturaRio:
    def __init__(self, puerto, rio, ultimo_registro, fecha_hora, estado):
        self.puerto = puerto
        self.rio = rio
        self.ultimo_registro = ultimo_registro
        self.fecha_hora = fecha_hora
        self.estado = estado

    def filtrar_por_puerto(self) -> list: 
        pass

    def filtrar_por_rio(self) -> list:
        pass

    def filtrar_por_estado(self) -> list:
        pass

    def __str__(self):
        return "Puerto: %s\nRio: %s\nUltimo registro: %s\nFecha hora: %s\nEstado: %s\n" % (self.puerto, self.rio, self.ultimo_registro, self.fecha_hora, self.estado)