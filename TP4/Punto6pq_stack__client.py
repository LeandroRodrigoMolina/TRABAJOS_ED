from Punto5PriorityQueueStack import PriorityQueueStack

cola_stack = PriorityQueueStack()

cola_stack.push(3)
cola_stack.push(10)
cola_stack.push(1)
cola_stack.push(4)

print(cola_stack)

a = cola_stack.top()

print("TOP", a)

print("LEN",len(cola_stack))

b = cola_stack.pop()
print("POP (REMOVE MIN)",b)

c = cola_stack.pop()
print("POP (REMOVE MIN) 2:", c)

cola_stack.push(69)
print(cola_stack)

print("ITER:")
for elemento in cola_stack:
    print(elemento)