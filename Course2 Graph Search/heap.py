class Heap:
    def __init__(self, array):
        self.heap = [None] + array

    def insert(self, object):
        self.heap.append(object)
        idx = len(self.heap) - 1
        par_idx = idx // 2

        while idx > 1:
            if self.heap[idx] < self.heap[par_idx]:
                self.heap[idx], self.heap[par_idx] = \
                    self.heap[par_idx], self.heap[idx]
                idx = par_idx
                par_idx = idx // 2
            else:
                break

        return self.heap

    def extract_min(self):
        min = self.heap[1]
        self.heap[1] = self.heap.pop()
        length = len(self.heap) - 1
        idx = 1
        child_idx = 2 * idx

        while True:
            if child_idx > length:
                break
            elif child_idx == length:
                if self.heap[idx] > self.heap[child_idx]:
                    self.heap[idx], self.heap[child_idx] = \
                        self.heap[child_idx], self.heap[idx]
                    idx = child_idx
                    child_idx = 2 * idx
                else:
                    break
            else:
                if self.heap[idx] < self.heap[child_idx] & \
                    self.heap[idx] < self.heap[child_idx + 1]:
                    break
                elif self.heap[child_idx + 1] > self.heap[child_idx]:
                    self.heap[idx], self.heap[child_idx] = \
                        self.heap[child_idx], self.heap[idx]
                    idx = child_idx
                    child_idx = 2 * idx
                else:
                    self.heap[idx], self.heap[child_idx + 1] = \
                        self.heap[child_idx + 1], self.heap[idx]
                    idx = child_idx + 1
                    child_idx = 2 * idx
        return self.heap

arr = [4, 4, 8, 9, 4, 12, 9, 11, 13]
heap = Heap(arr)
print(heap.insert(7))
print(heap.insert(10))
print(heap.insert(5))
print(heap.extract_min())