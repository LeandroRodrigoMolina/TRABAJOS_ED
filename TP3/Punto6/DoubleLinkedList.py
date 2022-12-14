from typing import Any
from DoubleLinkedListAbstract import DoubleLinkedListAbstract
from NodeLinked import Node

class DoubleLinkedList(DoubleLinkedListAbstract):
    def __init__(self):
        self.head = None

    def __len__(self):
        p = self.head
        count = 0
        while (p != None): 
            count += 1
            p = p.next
        return count

    def __getitem__(self, key):
        if(key > self.__len__()):
            raise Exception("Indice fuera de rango.")
        else:
            tempo = self.head
            contador = 0
            while(contador < key):
                tempo = tempo.next
                contador += 1
            return tempo.data

    def __setitem__(self, key, value): 
        if(key > self.__len__()):
            raise Exception("Indice fuera de rango.")
        else:
            tempo = self.head
            contador = 0
            while(contador < key):
                tempo = tempo.next
                contador += 1
            tempo.data = value
    def __delitem__(self, key): 
        if(key > self.__len__()):
            raise Exception("Indice fuera de rango.")
        else:
            tempo = self.head
            contador = 0
            while(contador < key):
                tempo = tempo.next
                contador += 1

            # print("\ntempo.previous", tempo.previous.data)
            # print("tempo.data", tempo.data)
            # print("tempo.next", tempo.next.data)

            tempo.previous.next = tempo.next
            tempo.next.previous = tempo.previous

            # print("\nDESPUES DEL CAMBIO\n")
            # print("tempo.previous", tempo.previous.data)
            # print("tempo.previous.next",tempo.previous.next.data)
            # print("tempo.data", tempo.data)
            # print("tempo.next.previous.data", tempo.next.previous.data)
            del tempo
    def __iter__(self):
        actual = self.head

        while(actual != None):
            yield actual.data
            actual = actual.next

    def __str__(self):
        if(self.is_empty()):
            return "DoubleLinkedList()"

        resultado = ""
        actual = self.head

        while(actual != None):
            resultado += str(actual.data) + ","
            actual = actual.next

        resultado = resultado[:len(resultado) - 1]

        return f"DoubleLinkedList({resultado})"

    def is_empty(self):
        return self.head == None

    def append(self, elem):
        node = Node(elem)
        if self.is_empty():
            self.head = node
        else:
            tempo = self.head
            while(tempo.next!=None):
                tempo = tempo.next
                
            tempo.next = node
            node.previous = tempo