from apython_ed_fcad_uner.data_structures.linear.stacks.linked_stack import LinkedStack
from Punto2LinkedStackExt import LinkedStackExt
pila_basica = LinkedStackExt()
pila_basica.push(1)
pila_basica.push(2)
pila_basica.push(5)
pila_basica.push(23)
pila_basica.push(21)
pila_basica.push(4)
pila_basica.push(8)
pila_basica.push(5.5)
pila_basica.push(2)
pila_basica.push(9)
pila_basica.push(298)
pila_basica.push(2112)
print("LA PILA ANTES DE USAR LOS METODOS", pila_basica)

indice = pila_basica.__len__()
print("INDICE: ", indice)
lista_popo = pila_basica.multi_pop(2)
print("DESPUES DEL MULTIPOP CON INDICE",indice,":", pila_basica)
print("LISTA_POPO:",lista_popo)

pila_basica.replace_all(2, 69)
print("PILA DESPUES DE REPLACE_ALL: ", pila_basica)

pila_basica.exchange()
print("PILA DESPUES DE EXCHANGE: ", pila_basica)