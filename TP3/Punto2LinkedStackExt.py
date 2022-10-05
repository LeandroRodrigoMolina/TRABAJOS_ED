from apython_ed_fcad_uner.data_structures.linear.stacks.linked_stack import LinkedStack
from Punto2.LinkedStackExtAbstract import LinkedStackExtAbstract

class LinkedStackExt(LinkedStackExtAbstract, LinkedStack):
    def multi_pop(self, num):
        i = num
        lista_pop = []
        while(i > 0):
            if(self.is_empty() == True):
                raise Exception("Pila vacia. Operacion no soportada.")
            else:
                lista_pop.append(self.pop())
            i -= 1
        return lista_pop

    def replace_all(self, param1, param2):
        lista_AUX = []
        pila_AUX = self
        indice = pila_AUX.__len__()
        while(indice > 0):
            lista_AUX.append(pila_AUX.pop())
            indice -= 1

        j = 0
        while(j < len(lista_AUX)):
            if lista_AUX[j] == param1:
                lista_AUX[j] = param2
            j += 1

        j = pila_AUX.__len__()
        pila_AUX.multi_pop(j)

        i = len(lista_AUX)
        while(i > 0):
            i -= 1
            pila_AUX.push(lista_AUX[i])

    def exchange(self):
        if(self.is_empty() == True):
            raise Exception("Pila vacia. Operacion no soportada.")
        else:
            top = self.top()

            lista_AUX = []
            pila_AUX = self
            indice = pila_AUX.__len__()
            while(indice > 0):
                lista_AUX.append(pila_AUX.pop())
                indice -= 1

            indice = len(lista_AUX) - 1
            ultimo = lista_AUX[indice]
            index_top = lista_AUX.index(top)
            index_ultimo = lista_AUX.index(ultimo)
            
            lista_AUX[index_top] = ultimo
            lista_AUX[index_ultimo] = top

            i = len(lista_AUX)
            while(i > 0):
                i -= 1
                pila_AUX.push(lista_AUX[i])