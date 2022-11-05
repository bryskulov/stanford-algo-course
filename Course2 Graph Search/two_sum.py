# Brute force hash implementation using Python set

def read_file(filename):
    file = open(filename, 'r')
    data = file.readlines()
    hash = set()
    for line in data:
        items = line.split()
        hash.add(int(items[0]))
    return hash


def main(filename):
    hash = read_file(filename)
    total = 0
    for t in range(-10000, 10000):
        print('Runnung t: ', t)
        for key in hash:
            y = t - key
            if y in hash and y != key:
                total += 1
                break
    return total

if __name__ == '__main__':
    print(main('2sum.txt'))
