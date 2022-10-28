"""Implemente a través de una clase con nombre PriorityQueueStack una estructura de
datos Pila (Ed. LIFO) utilizando solamente una cola de prioridad y una variable de instancia
adicional de tipo int."""

class PriorityQueueStack():
    def __init__(self):
        self.prioridad_stack = []

    def __len__(self):
        return len(self.prioridad_stack)

    def is_empty(self):
        return len(self.prioridad_stack) == 0

    def add(self, k, v):
        if(self.is_empty()):
            self.prioridad_stack.append((k,v))
        else:
            self.prioridad_stack.sort(key=lambda a: a[0])
            self.prioridad_stack.reverse()
            self.prioridad_stack.append((k,v))

    def min(self):
        if(self.is_empty()):
            raise "PriortyQueueStack esta vacio."
        aux = sorted(self.prioridad_stack)
        return aux[0]

    def remove_min(self):
        if(self.is_empty()):
            raise "PriortyQueueStack esta vacio."
        self.prioridad_stack.sort(key=lambda a: a[0])
        self.prioridad_stack.reverse()
        aux = self.prioridad_stack.pop()
        return aux