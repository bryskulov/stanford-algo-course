# Sorted array implementation with bisection

from bisect import bisect_left, bisect_right

def read_file(filename):
    file = open(filename, 'r')
    data = file.readlines()
    array = []
    for line in data:
        items = line.split()
        array.append(int(items[0]))
    array = sorted(array)
    return array

def main(filename):
    arr = read_file(filename)

    t_values = set()
    for x in arr:
        left = bisect_left(arr, -10000 - x)
        right = bisect_right(arr, 10000 - x)
        for y in arr[left:right]:
            if x != y:
                t_values.add(x + y)
    return len(t_values)


if __name__ == '__main__':
    print(main('2sum.txt'))