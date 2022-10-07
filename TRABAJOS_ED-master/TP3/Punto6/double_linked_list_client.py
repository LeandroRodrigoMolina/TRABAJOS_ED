from DoubleLinkedList import DoubleLinkedList

lista = DoubleLinkedList()
lista.append(1)
lista.append(2)
lista.append(8)
print("METODO STR:",lista.__str__())
print("METODO LEN:", lista.__len__())
print("METODO GETITEM CON EL ELEMENTO 1:", lista.__getitem__(1))

print("*"*80)
lista.__setitem__(1, 69)
print("\nDESPUES DE SETITEM:", lista)

print("*"*80)
lista.__delitem__(1) #Borrar elemento 69
print("DESPUES DE USAR METODO DELITEM EN KEY 1",lista)
print("METODO STR:",lista.__str__())
print("METODO LEN:", lista.__len__())
print("METODO GETITEM CON EL ELEMENTO 1:", lista.__getitem__(1))

print("METODO ITER")
a = [i for i in range(lista.__len__())]
iterator = iter(lista)

while True:
    try:
        out = next(iterator)
        print(f"Iterator loaded {out}")
    except StopIteration:
        print("End of iterator loading!")
        break