from Punto3UnsortedPriorityQueue import UnsortedPriorityQueue

a = UnsortedPriorityQueue()

print("LEN:",len(a))
print("IS EMPTY:",a.is_empty())
a.add(10, 3)
a.add(0, 4)
a.add(0, 1)
a.add(2, 3)
a.add(4, 87)
b = a.min()
print("LEN DESPUES DE ADD:",len(a))
print("MIN: ",b)

j = a.remove_min()
print("REMOVE MIN:", j)

b = a.min()
print("MIN 2: ",b)

j = a.remove_min()
print("REMOVE MIN 2:", j)
