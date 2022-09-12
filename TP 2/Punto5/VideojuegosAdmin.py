from VideojuegoAdminAbstract import VideojuegosAdminAbstract

class VideojuegosAdmin(VideojuegosAdminAbstract):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        string = ','.join(str(videojuego) for videjuego in self.videojuegos)
        return string
        
    def agregar(self, videojuego : Videojuego) -> None:
        pass

    def filtrar_por_desarrolladora(self, desarrolladora: Empresa) -> list:
        pass

    def filtrar_por_distribuidora(self, distribuidora: Empresa) -> list:
        pass

    def filtrar_por_genero(self, genero: Genero) -> list:
        pass

    def cantidad_por_plataforma(self) -> list:
        pass

    def ordenar_titulo(self) -> None:
        pass

    def ordenar_mejores_primero(self) -> None:
        pass