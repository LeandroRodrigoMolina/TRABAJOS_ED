from apython_ed_fcad_uner.data_structures.priority_queues.array_heap import ArrayHeap
class HeapQueue():
    def __init__(self):
        self.heap = ArrayHeap()

    def __len__(self):
        return len(self.heap._data)

    def __str__(self):
        if(len(self.heap) == 0):
            return "HeapQueue()"
        
        return f"HeapQueue({', '.join(list(str(x) for x in self.heap._data))})"

    def __iter__(self):
        i = len(self.heap)
        j = 0
        while j < i:
            yield self.heap[j]
            j += 1

    def is_empty(self):
        return (self.heap.is_empty())

    def first(self):
        return (self.heap.min())

    def dequeue(self):
        return (self.heap.remove_min())

    def enqueue(self, k, v):
        self.heap.add(k, v)