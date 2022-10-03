from Deque import Deque

deque1 = Deque()

#SE USAN METODOS add_first y add_last
deque1.add_first(1)
deque1.add_first(3)
deque1.add_last(23)
deque1.add_first(5)
deque1.add_last(13)
deque1.add_first(6)
deque1.add_last(9)

print("METODO LEN:", deque1.__len__())
print("METODO STR:",deque1.__str__())
print("METODOO EMPTY:", deque1.is_empty())
print("METODO FIRST:", deque1.first())
print("METODO LAST:", deque1.last())

print()
print("ANTES DEL METODO DELETE_FIRST:\n", deque1)
deque1.delete_first()
print()
print("DESPUES DEL METODO DELETE_FIRST:\n",deque1)
print()
print("*"*80)
print("ANTES DEL METODO DELETE_LAST:\n", deque1)
deque1.delete_last()
print()
print("DESPUES DEL METODO DELETE_LAST:\n", deque1)
