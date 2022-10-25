from pathlib import Path
from collections import Counter

from dfs import graph


def test_compute_scc1():
    G, expected_result = read_file('test_files/scc1.txt')
    G = graph(G)
    leaders = G.compute_scc().values()
    sizes = Counter(leaders).most_common(5)
    actual_result = [i[1] for i in sizes] + [0] * (5 - len(sizes))
    assert actual_result == expected_result


def test_compute_scc2():
    G, expected_result = read_file('test_files/scc2.txt')
    G = graph(G)
    leaders = G.compute_scc().values()
    sizes = Counter(leaders).most_common(5)
    actual_result = [i[1] for i in sizes] + [0] * (5 - len(sizes))
    assert actual_result == expected_result


def test_compute_scc3():
    G, expected_result = read_file('test_files/scc3.txt')
    G = graph(G)
    leaders = G.compute_scc().values()
    sizes = Counter(leaders).most_common(5)
    actual_result = [i[1] for i in sizes] + [0] * (5 - len(sizes))
    assert actual_result == expected_result


def test_compute_scc4():
    G, expected_result = read_file('test_files/scc4.txt')
    G = graph(G)
    leaders = G.compute_scc().values()
    sizes = Counter(leaders).most_common(5)
    actual_result = [i[1] for i in sizes] + [0] * (5 - len(sizes))
    assert actual_result == expected_result


def test_compute_scc5():
    G, expected_result = read_file('test_files/scc5.txt')
    G = graph(G)
    leaders = G.compute_scc().values()
    sizes = Counter(leaders).most_common(5)
    actual_result = [i[1] for i in sizes] + [0] * (5 - len(sizes))
    assert actual_result == expected_result


def read_file(filename):
    test_directory = Path(__file__).parent
    file = open(test_directory / filename, "r")
    data = file.readlines()
    
    counter = 0
    for line in data:
        if counter == 0:
            num_nodes = int(line)
            G = [[] for i in range(num_nodes)]
            counter += 1
        elif counter == 1:
            true_sizes = [int(i) for i in line.split()]
            counter += 1
        else:
            items = line.split()
            G[int(items[0])-1] += [str(items[1])]
    G = dict(zip([str(i) for i in range(1, num_nodes+1, 1)], G))
        
    return G, true_sizes