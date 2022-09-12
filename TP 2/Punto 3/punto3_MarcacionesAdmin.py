from punto3_MarcacionesAdminAbstract import MarcacionesAdminAbstract

class MarcacionesAdmin(MarcacionesAdminAbstract):
    def __init__(self):
        super().__init__()
        
    def agregar(self, marcacion) -> None:
        self.marcaciones.append(marcacion)

    def empleados(self) -> list:
        empleados_Repe = []
        empleados_sinRepe = []
        for marcacion in self.marcaciones:
            empleados_Repe.append(marcacion.empleado)

        for i in empleados_Repe:
            if i not in empleados_sinRepe:
                empleados_sinRepe.append(i)

        return empleados_sinRepe
        
    def filtrar_por_empleado(self, empleado) -> list:
        lista_empleados = []
        for marcacion in self.marcaciones:
            if marcacion.empleado == empleado:
                lista_empleados.append(marcacion.empleado)

        return lista_empleados

    def filtrar_por_tipo(self, tipo) -> list:
        lista_tipo = []
        for marcacion in self.marcaciones:
            if(marcacion == tipo):
                lista_tipo.append(marcacion)

        return lista_tipo

    def llegadas_tarde(self) -> list:
        llegados_tarde = []
        for marcacion in self.marcaciones:
            if(marcacion.fecha_Hora.hour > marcacion.empleado.oficina.hora_entrada.hour) & (marcacion.fecha_Hora.minute > marcacion.empleado.oficina.hora_entrada.minute):
                llegados_tarde.append(marcacion)

        return llegados_tarde

    def ordenar_legajo(self) -> None:
        lista_AUX = self.marcaciones
        lista_AUX.sort(key=lambda x: (x.empleado.legajo, x.fecha_Hora))
        self.marcaciones = lista_AUX

    def ordenar_apellido_nombre(self):
        lista_AUX = self.marcaciones
        lista_AUX.sort(key=lambda x: (x.empleado.apellido, x.empleado.nombre))
        self.marcaciones = lista_AUX