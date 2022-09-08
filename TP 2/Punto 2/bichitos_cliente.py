from punto2_Raza import Raza
from punto2_Persona import Persona
from punto2_Mascota import Mascota

def imprimir(mascotas : list) -> None:
    for mascota in mascotas:
        print(mascota)
        print()

def filtrar_gerontes(mascotas : list) -> list:
    lista_gerontes = []
    for mascota in mascotas:
        if mascota.edad >= 13:
            lista_gerontes.append(mascota)

    return lista_gerontes

def filtrar_por_especie(mascotas : list, especie : Especie) -> list:
    lista_especie = []
    for mascota in mascotas:
        if(mascota.especie == especie):
            lista_especie.append(mascota)

    return lista_especie

def max_mascotero(mascotas : list) -> Persona:
    pass