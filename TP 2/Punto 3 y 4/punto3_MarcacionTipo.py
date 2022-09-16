#Podria ser una enumeracion o asi como esta xd
class MarcacionTipo():
    def __init__(self, entrada:int, salida:int):
        self.entrada = entrada
        self.salida = salida

    def __str__(self) -> str:
        return "Entrada:%d\nSalida:%d\n" % (self.entrada, self.salida)

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, o) -> str:
        if isinstance(o, MarcacionTipo):
            return (self.entrada == o.entrada) and (self.salida == o.salida)

        return False