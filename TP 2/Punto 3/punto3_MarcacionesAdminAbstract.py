from abc import ABC, abstractmethod
from empleado import Empleado
from marcacion import Marcacion

class MarcacionesAdminAbstract(ABC):

    def __init__(self) -> None:
        self.marcaciones = list()

    def __len__(self) -> int:
        return len(self.marcaciones)
    
    def __getitem__(self, key: int) -> Marcacion:
        return self.marcaciones[key]

    def __delitem__(self, key: int) -> None:
        del self.marcaciones[key]
        
    def __str__(self) -> str:
        res = ""
        for elem in self.marcaciones:
            res += "{elem}\n".format(elem=str(elem))

        return res

    @abstractmethod
    def agregar(self, marcacion : Marcacion) -> None:
        pass

    @abstractmethod
    def empleados(self) -> list:
        pass

    @abstractmethod
    def filtrar_por_empleado(self, empleado: Empleado) -> list:
        pass

    @abstractmethod
    def filtrar_por_tipo(self, tipo: Marcacion) -> list:
        pass

    @abstractmethod
    def llegadas_tarde(self) -> list:
        pass

    @abstractmethod
    def ordenar_legajo(self) -> None:
        pass

    @abstractmethod
    def ordenar_apellido_nombre(self) -> None:
        pass
