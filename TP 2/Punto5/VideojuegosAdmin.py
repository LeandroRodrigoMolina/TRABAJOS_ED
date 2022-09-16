from VideojuegoAdminAbstract import VideojuegosAdminAbstract

class VideojuegosAdmin(VideojuegosAdminAbstract):
    def __init__(self):
        super().__init__()

# SE LO TUVE AL __STR__ QUE CAMBIAR PORQUE NO ME ANDABAN 
# LOS ORDENAMIENTOS POR TITULO NI POR MEJORES PRIMERO, NO ME ANDABAN LOS LAMBDAS O NI IDEA LA VERDAD
    def __str__(self) -> str: 
        res = ""
        for elem in self.videojuegos:
            res += "{elem}\n".format(elem=str(elem))

        return res
        
    def agregar(self, videojuego) -> None:
        self.videojuegos.append(videojuego)

    def filtrar_por_desarrolladora(self, desarrolladora) -> list:
        lista_desarrollados = []
        for videojuego in self.videojuegos:
            if videojuego.empresa_Dev == desarrolladora:
                lista_desarrollados.append(videojuego)

        return lista_desarrollados

    def filtrar_por_distribuidora(self, distribuidora) -> list:
        lista_distribuidora = []
        for videojuego in self.videojuegos:
            if videojuego.empresa_Distri == distribuidora:
                lista_distribuidora.append(videojuego)

        return lista_distribuidora

    def filtrar_por_genero(self, genero) -> list:
        lista_genero = []
        for videojuego in self.videojuegos:
            if videojuego.genero == genero:
                lista_genero.append(videojuego)

        return lista_genero

    def cantidad_por_plataforma(self) -> list:
        """Indica la cantidad de videojuegos por plataforma. """
        play2 = 0
        xbox = 0
        psp = 0
        wii = 0
        lista = []
        for videojuego in self.videojuegos:
            for plataforma in videojuego.plataformas:
                if(plataforma.nombre == "Play 2"):
                    play2 += 1
                elif(plataforma.nombre == "Xbox"):
                    xbox += 1
                elif(plataforma.nombre == "PSP"):
                    psp += 1
                elif(plataforma.nombre == "Wii"):
                    wii += 0

        lista.append(play2)
        lista.append(xbox)
        lista.append(psp)
        lista.append(wii)
        return lista

    def ordenar_titulo(self) -> None:
        lista_AUX = self.videojuegos
        lista_AUX.sort(key=lambda x: (x.titulo))
        self.videojuegos = lista_AUX

    def ordenar_mejores_primero(self) -> None:
        lista_AUX = self.videojuegos
        lista_AUX.sort(key=lambda x: (x.rankingMetacritic))
        lista_AUX.reverse()
        self.videojuegos = lista_AUX
