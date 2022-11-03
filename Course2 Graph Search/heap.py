class MinHeap:
    def __init__(self, array):
        self.size = len(array)
        self.heap = [None] + array
        self.min_heap()

    def parent(self, idx):
        return idx // 2

    def left_node(self, idx):
        return idx * 2

    def right_node(self, idx):
        return idx * 2 + 1
    
    def is_leaf(self, idx):
        return idx * 2 > self.size

    def swap(self, fidx, sidx):
        self.heap[fidx], self.heap[sidx] = \
            self.heap[sidx], self.heap[fidx]

    def heapify(self, idx):
        if not self.is_leaf(idx):
            if self.heap[idx] > self.heap[self.left_node(idx)] or \
                self.heap[idx] > self.heap[self.right_node(idx)]:
                if self.heap[self.left_node(idx)] < self.heap[self.right_node(idx)]:
                    self.swap(idx, self.left_node(idx))
                    self.heapify(self.left_node(idx))

                else:
                    self.swap(idx, self.right_node(idx))
                    self.heapify(self.right_node(idx))

    def min_heap(self):
        for idx in range(self.size//2, 0, -1):
            self.heapify(idx)

    def insert(self, object):
        self.heap.append(object)
        self.size += 1
        current = self.size
        
        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def get_min(self):
        return self.heap[1]

    def extract_min(self):
        min = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1
        self.heapify(self.heap[1])
        return min

arr = [13, 9, 11, 9, 4, 12, 4, 8, 4]
heap = MinHeap(arr)
heap.insert(7)
heap.insert(10)
heap.insert(5)
print(heap.heap)
print(heap.extract_min())