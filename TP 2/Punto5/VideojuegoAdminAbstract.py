from abc import ABC, abstractmethod
from plataforma import Plataforma
from genero import Genero
from empresa import Empresa
from videojuego import Videojuego

class VideojuegosAdminAbstract(ABC):
    def __init__(self) -> None:
        self.videojuegos = []

    def __len__(self) -> int:
        return len(self.videojuegos)

    def __getitem__(self, key: int) -> Videojuego:
        return self.videojuegos[key]

    def __delitem__(self, key: int) -> None:
        return self.videojuegos[key]

    def __delitem__(self, key: int) -> None:
        del self.videojuegos[key]

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def agregar(self, videojuego : Videojuego) -> None:
        pass

    @abstractmethod
    def filtrar_por_desarrolladora(self, desarrolladora: Empresa) -> list:
        pass

    @abstractmethod
    def filtrar_por_distribuidora(self, distribuidora: Empresa) -> list:
        pass

    @abstractmethod
    def filtrar_por_genero(self, genero: Genero) -> list:
        pass

    @abstractmethod
    def cantidad_por_plataforma(self) -> list:
        pass

    def ordenar_titulo(self) -> None:
        pass

    @abstractmethod
    def ordenar_mejores_primero(self) -> None:
        pass