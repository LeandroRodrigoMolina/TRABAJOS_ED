from Punto7HeapQueue import HeapQueue
cola_heap = HeapQueue()

print("METODO IS_EMTPY ANTES DE LOS ENQUEUE:",cola_heap.is_empty())
cola_heap.enqueue(4, 20)
cola_heap.enqueue(1, 10)
cola_heap.enqueue(1, 0)
cola_heap.enqueue(2, 9)
cola_heap.enqueue(10, 3)

print("METODO LEN:",len(cola_heap))
print(cola_heap)
print("METODO IS_EMTPY:",cola_heap.is_empty())
print("METODO FIRST:",cola_heap.first())

print("*"*80)
print("METODO DEQUEUE:", cola_heap.dequeue())
print("COLA DESPUES DE DEQUEUE:\n",cola_heap)

print("METODO DEQUEUE2:", cola_heap.dequeue())

print("METODO DEQUEUE3:", cola_heap.dequeue())
print("COLA DESPUES DE DEQUEUE 2 y 3:\n",cola_heap)