import timeit
not_sorted_heap = [1, 43, 23 ,65 ,8 , 653, 345, 324, 8, 8]
sort_it = range(10000000)

class Heap:
    # didn't want to close access to this var from outside,
    # because it would make the code more difficult to understand
    heap = []
    
    def __init__ (self, arr):
        self.heap = arr
        self.build_max_heap()
        
    def build_max_heap (self):
        heap_size = len(self.heap)
        for x in range(heap_size//2, -1, -1):
            self.heap = self.max_heapify(x)
        
    def swap (self, a, b):
        tmp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = tmp
        return self.heap

    def max_heapify(self, i):

        left_dif = 0
        right_dif = 0

        #first check if these numbers exist
        if 2 * (i + 1) < len(self.heap):
            right_dif = self.heap[2 * (i + 1)] - self.heap[i]
        if 2 * (i + 1) - 1 < len(self.heap):
            left_dif = self.heap[2 * (i + 1) - 1] - self.heap[i]

        #then which child we have to swap, if not, return self.heap
        if right_dif > 0 and right_dif >= left_dif:
            self.swap (i, 2 * (i + 1))
            return self.max_heapify (2 * (i + 1))
        elif left_dif > 0 and left_dif > right_dif:
            self.swap (i, 2 * (i + 1) - 1)
            return self.max_heapify (2 * (i + 1) - 1)
        else:
            return self.heap

    def extract_max (self):
        m = self.heap[0]
        self.swap (0, len(self.heap) - 1)
        self.heap = self.heap [:len(self.heap) - 1]
        self.max_heapify(0)
        return m

    def insert (self, val):
        self.heap.append(val)
        self.build_max_heap()

    def increase_key (self, i, value):
        self.heap[i] = value
        self.build_max_heap()

    def get_max (self):
        return self.heap[0]
    
    def get_sorted (self):
        arr = []
        for x in range(len(self.heap)):
            arr.append(self.extract_max())
        return arr
    
smth = range(10000)
arr = Heap(smth)
#arr = Heap(sort_it)
print timeit.timeit(arr.get_sorted, number=1)
# range of 10 million numbers it sorts in 30.8309111595
