from PriorityQueueStack import PriorityQueueStack

cola_stack = PriorityQueueStack()

cola_stack.add(10, 8)
cola_stack.add(0, 3)
cola_stack.add(-2, 3)
cola_stack.add(2, 4)

a = cola_stack.min()

print("MIN", a)

print("LEN",len(cola_stack))

b = cola_stack.remove_min()
print("REMOVE MIN",b)

c = cola_stack.remove_min()
print("REMOVE MIN 2:", c)
