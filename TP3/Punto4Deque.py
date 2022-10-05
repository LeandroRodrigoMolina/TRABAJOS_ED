from typing import Any
from Punto4.DequeAbstract import DequeAbstract
from apython_ed_fcad_uner.data_structures.linear.list_node import ListNode

class Deque(DequeAbstract):
    def __init__(self):
        self.front = None
        self.prev = None
        self.deque_size = 0

    def __len__(self):
        return self.deque_size

    def __str__(self):
        if(self.is_empty()):
            return "Deque()"

        resultado = ""
        actual = self.front

        while(actual != None):
            resultado += str(actual.element) + ","
            actual = actual.next

        resultado = resultado[:len(resultado) - 1]

        return f"Deque({resultado})"
        
    def is_empty(self):
        if self.deque_size == 0:
            return True
        
        return False

    def first(self):
        if(self.deque_size == 0):
            raise Exception("Deque esta vacio. Operacion no valida.")

        return self.front.element

    def last(self):
        if(self.deque_size == 0):
            raise Exception("Deque esta vacio. Operacion no valida.")

        aux = self.front
        while(aux.next != None):
            aux = aux.next
        
        return aux.element

    def add_first(self, element):
        aux = ListNode(element, self.front)
        if(self.is_empty()):
            self.front = aux
            self.prev = aux
        else:
            self.front = aux
        self.deque_size += 1

    def add_last(self, element):
        aux = ListNode(element)
        if(self.is_empty()):
            self.front = aux
            self.prev = aux
        else:
            self.prev.next = aux
            self.prev = self.prev.next

        self.deque_size += 1
        
    def delete_first(self):
        if(self.deque_size == 0):
            raise Exception("Deque esta vacio. Operacion no valida.")
        else:
            aux = self.front
            self.front = self.front.next
            self.deque_size -= 1
            del aux

    def delete_last(self):
        if(self.deque_size == 0):
            raise Exception("Deque esta vacio. Operacion no valida.")
        else:
            aux = self.front
            anterior = None
            while (aux.next != None):
                anterior = aux
                aux = aux.next
            anterior.next = aux.next
            self.deque_size -= 1
            del aux