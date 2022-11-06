from Punto1yPunto2.LinkedBinaryTreeExtAbstract import LinkedBinaryTreeExtAbstract
from apython_ed_fcad_uner.data_structures.trees.linked_binary_tree import LinkedBinaryTree

class LinkedBinaryTreeExt(LinkedBinaryTree, LinkedBinaryTreeExtAbstract):
    def __init__(self):
        super(LinkedBinaryTreeExt, self).__init__()

    def hermanos(self, nodo1, nodo2):
        """ Indica si node1 y node2 son hermanos.
        Args:
        nodo1 (BinaryTreeNode): nodo que debe pertenecer al árbol.
        nodo2 (BinaryTreeNode): nodo que debe pertenecer al árbol.
        Returns:
        bool: True si los nodos tienen el mismo padre, False en caso contrario.
        """
        nodo1Padre = self._search_parent(nodo1)
        nodo2Padre = self._search_parent(nodo2)
        return nodo1Padre == nodo2Padre
        pass

    def hojas(self):
        """ Devuelve los elementos de los nodos que no tienen ningún hijo.
        Returns:
        List[Any]: lista formada por los elementos de los nodos hoja.
        """
        lista_hojas = []
        for nodo in self:
            if(nodo.element != None):
                if(nodo.children_count() == 0):
                    lista_hojas.append(nodo.element)
        return lista_hojas

    def internos(self):
        """ Devuelve los elementos de los nodos que tienen padre y algún hijo.
        Returns:
        List[Any]: lista formada por los elementos de los nodos internos.
        """
        lista_internos = []
        for nodo in self:
            nodoPadre = self._search_parent(nodo)
            if(nodoPadre != None):
                if(nodo.children_count() > 0):
                    lista_internos.append(nodo.element)

        return lista_internos

    def profundidad(self, nodo):
        """ Devuelve la longitud del camino entre la raíz y un nodo.
        Args:
        nodo (BinaryTreeNode): nodo del que se quiere conocer la profundidad.
        Returns:
        int: devuelve el número de arcos entre la raíz y nodo. 0 si nodo es la raíz.
        """
        aux = self._search_parent(nodo)
        profundidad = 1

        if (aux == None):
            return 0

        while aux:
            aux = self._search_parent(aux)

            if (aux == None):
                return profundidad
            else:
                profundidad += 1

    def altura(self, nodo):
        """ Retorna la longitud del camino entre nodo y la hoja más lejana.
        Args:
        nodo (BinaryTreeNode): nodo del que se quiere conocer la altura.
        Returns:
        int: Devuelve 0 en caso que nodo sea hoja, caso contrario, la cantidad de arcos
        entre nodo y la hoja más lejana. """
        
        if (nodo.children_count == 0):
            return 0

        hojas = self.hojas()
        cont = 0
        altura = 0

        while len(hojas) != 0:
            pop_hoja = hojas.pop()

            while pop_hoja:
                pop_hoja = self._search_parent(pop_hoja)

                if(pop_hoja == nodo):
                    if(altura < cont):
                        altura = cont
                else:
                    cont += 1

                if (pop_hoja == None):
                    pass
                
                cont = 1

        return altura