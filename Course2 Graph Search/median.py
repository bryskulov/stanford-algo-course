# Median Maintenance using Heaps
from argparse import ArgumentParser

from heap import MinHeap, MaxHeap

class MedianMaintener:
    def __init__(self):
        self.MaxHeap = MaxHeap([])
        self.MinHeap = MinHeap([])

    def insert(self, x):
        if self.MaxHeap.size < 2:
            self.MaxHeap.insert(x)
            self.median = x
        if x < self.MaxHeap.get_max():
            self.MaxHeap.insert(x)
        else:
            self.MinHeap.insert(x)

        if self.MinHeap.size - self.MaxHeap.size == 2:
            self.MaxHeap.insert(self.MinHeap.extract_min())
        elif self.MaxHeap.size - self.MinHeap.size == 2:
            self.MinHeap.insert(self.MaxHeap.extract_max())

        if self.MinHeap.size > self.MaxHeap.size:
            self.median = self.MinHeap.get_min()
        else:
            self.median = self.MaxHeap.get_max()

def read_file(filename):
    file = open(filename)
    data = file.readlines()
    array = []
    for line in data:
        items = line.split()
        array.append(int(items[0]))
    return array

def main(filename):
    mm = MedianMaintener()
    array = read_file(filename)
    sum = 0
    for x in array:
        mm.insert(x)
        sum += mm.median
    return sum % 10000


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-i", dest="filename", required=True,
                        help="input txt file", metavar="FILE")
    args = parser.parse_args()
    print(main(args.filename))