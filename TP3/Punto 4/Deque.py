from typing import Any
from DequeAbstract import DequeAbstract
from Node import Node

class Deque(DequeAbstract):
    def __init__(self):
        self.front = None
        self.deque_size = 0

    def __len__(self):
        return self.deque_size

    def __str__(self):
        if(self.is_empty()):
            return "Deque()"

        resultado = ""
        actual = self.front

        while(actual != None):
            resultado += str(actual.data) + ","
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

        return self.front.data

    def last(self):
        if(self.deque_size == 0):
            raise Exception("Deque esta vacio. Operacion no valida.")

        aux = self.front
        while(aux.next != None):
            aux = aux.next

        return aux.data

    def add_first(self, element):
        tempo = Node(element)
        if(self.front == None):
            self.front = tempo
            self.deque_size += 1
        else:
            tempo.next = self.front
            self.front = tempo
            self.deque_size = self.deque_size + 1

    def add_last(self, element):
        tempo = Node(element)
        if (self.front == None):
            self.front = tempo
            self.deque_size += 1
        else:
            aux = self.front
            while (aux.next != None):
                aux = aux.next

            aux.next = tempo
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