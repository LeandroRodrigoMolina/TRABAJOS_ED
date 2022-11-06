from Punto3yPunto4.UnsortedPriorityQueueAbstract import UnsortedPriorityQueueAbstract

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract):
    def __init__(self):
        self.prioridad_queue = []

    def __len__(self):
        """ Devuelve la cantidad de elementos en la estructura.
        Returns:
        int: Cantidad de elementos en la estructura. 0 en caso que esté vacía.
        """
        return len(self.prioridad_queue)

    def is_empty(self):
        """ Indica si la estructura está vacía o no.
        Returns:
        bool: True si está vacía. False en caso contrario.
        """
        return len(self.prioridad_queue) == 0

    def add(self, k, v):
        """ Inserta un nuevo ítem al final de la estructura.
        Args:
            k (Any): Clave que determina la prioridad del ítem.
            v (Any): Valor del ítem.
        """
        self.prioridad_queue.append((k, v))

    def min(self):
        """ Devuelve una tupla conformada por la clave y valor del ítem con menor valor de
        clave.
        Raises:
        Exception: Arroja excepción si se invoca cuando la estructura está vacía.
        Returns:
        Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem.
        """
        if(self.is_empty()):
            raise "TA VACIA LA QUEUE LOCO"

        aux = sorted(self.prioridad_queue)
        return aux[0]

    def remove_min(self):
        """ Quita de la estructura el ítem con menor valor de clave.
        Raises:
        Exception: Arroja excepción si se invoca cuando la estructura está vacía.
        Returns:
        Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem.
        """
        if(self.is_empty()):
            raise "TA VACIA LA QUEUE LOCO"
        
        aux = sorted(self.prioridad_queue)
        i = aux[0]
        self.prioridad_queue.remove(i)
        return i