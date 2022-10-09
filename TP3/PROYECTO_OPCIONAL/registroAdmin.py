from RegistroAlturaRio import RegistroAlturaRio

class registroAdmin():
    def __init__(self) -> None:
        self.registro = []

    def __len__(self) -> int:
        return len(self.registro)

    def __getitem__(self, key: int):
        return self.registro[key]

    def __delitem__(self, key: int):
        return self.registro[key]

    def __delitem__(self, key: int):
        del self.registro[key]

    def __str__(self) -> str: 
        res = ""
        for elem in self.registro:
            res += "{elem}\n".format(elem=str(elem))

        return res
        
    def agregar(self, registro):
        self.registro.append(registro)
    
    def filtrar_por_puerto(self, nombrePuerto) -> list: 
        lista_puerto = []
        for i in self.registro:
            if(i.puerto == nombrePuerto):
                lista_puerto.append(i)

        return lista_puerto
    def filtrar_por_rio(self, rio) -> list:
        lista_rio = []
        for i in self.registro:
            if(i.rio == rio):
                lista_rio.append(i)

        return lista_rio
    def filtrar_por_estado(self, estado) -> list:
        lista_estado = []
        for i in self.registro:
            if(i.estado == estado):
                lista_estado.append(i)
        return lista_estado