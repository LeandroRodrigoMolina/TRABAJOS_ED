from VideojuegoAdminAbstract import VideojuegosAdminAbstract

class VideojuegosAdmin(VideojuegosAdminAbstract):
    def __init__(self):
        super().__init__()

    def __str__(self) -> str:
        string = ','.join(str(videojuego) for videjuego in self.videojuegos)
        return string
        
    def agregar(self, videojuego) -> None:
        self.videojuegos.append(videojuego)

    def filtrar_por_desarrolladora(self, desarrolladora) -> list:
        #TA MAL NO SIRVE
        desarrolladora_Repe = []
        desarrolladora_SinRepe = []
        for videojuego in self.videojuegos:
            desarrolladora_Repe.append(videojuego.empresa_Dev)

        for i in desarrolladora_Repe:
            if i not in desarrolladora_SinRepe:
                desarrolladora_SinRepe.append(i)

        return desarrolladora_SinRepe

    def filtrar_por_distribuidora(self, distribuidora) -> list:
        distribuidora_Repe = []
        distribuidora_SinRepe = []

        for videojuego in self.videojuegos:
            distribuidora_Repe.append(videojuego.empresa_Distri)

        for i in distribuidora_Repe:
            if i not in distribuidora_SinRepe:
                distribuidora_SinRepe.append(i)

        return distribuidora_SinRepe

    def filtrar_por_genero(self, genero) -> list:
        lista_genero = []
        for videojuego in self.videojuegos:
            if videojuego.genero == genero:
                lista_genero.append(videojuego.genero)

        return lista_genero

    def cantidad_por_plataforma(self) -> list:
        """Indica la cantidad de videojuegos por plataforma. """
        listado_plataformas = []
        for videojuego in self.videojuegos:
            if videojuego.plataforma not in listado_plataformas:
                listado_plataformas.append(videojuego.plataforma)

    def ordenar_titulo(self) -> None:
        lista_AUX = self.videojuegos
        lista_AUX.sort(key=lambda x: (x.titulo))
        self.videojuegos = lista_AUX

    def ordenar_mejores_primero(self) -> None:
        lista_AUX = self.videojuegos
        lista_AUX.sort(key=lambda x: (x.ranking_metacritic))
        lista_AUX.sort(reverse=True)
        self.videojuegos = lista_AUX