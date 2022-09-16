class Plataforma():
    def __init__(self, nombre:str, portatil:bool):
        self.nombre = nombre
        self.portatil = portatil

    def __str__(self):
        return " Plataforma: %s Portatil: %s" %(self.nombre, self.portatil)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Plataforma):
            return (self.nombre == o.nombre)
        
        return False