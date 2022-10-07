class Genero():
    def __init__(self, genero:str):
        self.genero = genero

    def __str__(self):
        return "\nGenero: %s" % (self.genero)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        if isinstance(o, Genero):
            return (self.genero == o.genero)
        
        return False