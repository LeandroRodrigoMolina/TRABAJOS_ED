from punto2_Raza import Raza
from punto2_Persona import Persona
from punto2_Mascota import Mascota
from punto2_Especie import Especie

import operator

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

def filtrar_por_especie(mascotas : list, especie) -> list:
    lista_especie = []
    for mascota in mascotas:
        if(mascota.especie == especie):
            lista_especie.append(mascota)

    return lista_especie

def max_mascotero(mascotas : list) -> Persona:
    pass

persona1 = Persona("Lopeciño", "Juancito", "48524321")
especie1 = Especie("JIJIJUA")
raza1 = Raza("Xaxa", especie1)
mascota1 = Mascota(78, "COSO", raza1, 1892, persona1)

especie2 = Especie("JEJEJE")
raza2 = Raza("XEXE", especie2)
mascota2 = Mascota(78, "COSO", raza2, 1892, persona1)

persona3 = Persona("Block", "Walter", "02345847")
mascota3= Mascota(200, "MASH", raza2, 2001, persona3)

print("Edad del bicho:", mascota1.edad)

lista_mascotas = [mascota1, mascota2, mascota3]

el_AMO = max_mascotero(lista_mascotas)
print("EL QUE TIENE MUCHAS MASCOTAS: ", el_AMO)