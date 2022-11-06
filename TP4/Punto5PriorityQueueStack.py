"""Implemente a través de una clase con nombre PriorityQueueStack una estructura de
datos Pila (Ed. LIFO) utilizando solamente una cola de prioridad y una variable de instancia
adicional de tipo int."""

class PriorityQueueStack():
    def __init__(self):
        self.prioridad_stack = []
        self.prioridad_int = 0

    def __len__(self):
        return len(self.prioridad_stack)

    def is_empty(self):
        return len(self.prioridad_stack) == 0

    def push(self,v):
        self.prioridad_stack.append((self.prioridad_int, v))
        self.prioridad_int -= 1

    def top(self):
        if(self.is_empty()):
            raise "PriortyQueueStack esta vacio."
        aux = self.prioridad_stack.copy()
        res = aux.pop()
        return res

    def pop(self):
        if(self.is_empty()):
            raise "PriortyQueueStack esta vacio."

        self.prioridad_int += 1
        return self.prioridad_stack.pop()
        
    def __iter__(self):
        i = len(self.prioridad_stack)
        j = 0
        while j < i:
            yield self.prioridad_stack[j]
            j += 1

    def __str__(self):
        res = ""
        for elem in self.prioridad_stack:
            res += str(elem) + ","
        return "PriorityQueueStack(" + res[:-1] + ")"