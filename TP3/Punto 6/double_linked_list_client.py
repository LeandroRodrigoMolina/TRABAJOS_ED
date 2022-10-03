from DoubleLinkedList import DoubleLinkedList

lista = DoubleLinkedList()
lista.append(1)
lista.append(2)
lista.append(8)
print("METODO STR:",lista.__str__())
print("METODO LEN:", lista.__len__())
print("METODO GETITEM:", lista.__getitem__(1))

lista.__setitem__(1, 69)
print("DESPUES DE SETITEM:", lista)
