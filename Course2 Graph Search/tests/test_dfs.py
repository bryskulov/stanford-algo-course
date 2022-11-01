from pathlib import Path
from collections import Counter

from dfs import graph


def test_compute_scc1():
    G = read_file(10, 'test_files/scc1.txt')
    expected_result = [3, 3, 3, 0, 0]
    G = graph(G)
    leaders = G.compute_scc().values()
    sizes = Counter(leaders).most_common(5)
    actual_result = [i[1] for i in sizes] + [0] * (5 - len(sizes))
    assert actual_result == expected_result


def test_compute_scc2():
    G = read_file(9, 'test_files/scc2.txt')
    expected_result = [3, 3, 2, 0, 0]
    G = graph(G)
    leaders = G.compute_scc().values()
    sizes = Counter(leaders).most_common(5)
    actual_result = [i[1] for i in sizes] + [0] * (5 - len(sizes))
    assert actual_result == expected_result


def test_compute_scc3():
    G = read_file(9, 'test_files/scc3.txt')
    expected_result = [3, 3, 1, 1, 0]
    G = graph(G)
    leaders = G.compute_scc().values()
    sizes = Counter(leaders).most_common(5)
    actual_result = [i[1] for i in sizes] + [0] * (5 - len(sizes))
    assert actual_result == expected_result


def test_compute_scc4():
    G = read_file(9, 'test_files/scc4.txt')
    expected_result = [7, 1, 0, 0, 0]
    G = graph(G)
    leaders = G.compute_scc().values()
    sizes = Counter(leaders).most_common(5)
    actual_result = [i[1] for i in sizes] + [0] * (5 - len(sizes))
    assert actual_result == expected_result


def test_compute_scc5():
    G = read_file(13, 'test_files/scc5.txt')
    expected_result = [6, 3, 2, 1, 0]
    G = graph(G)
    leaders = G.compute_scc().values()
    sizes = Counter(leaders).most_common(5)
    actual_result = [i[1] for i in sizes] + [0] * (5 - len(sizes))
    assert actual_result == expected_result


def read_file(num_nodes, filename):
    test_directory = Path(__file__).parent
    file = open(test_directory / filename, "r")
    data = file.readlines()
    G = [[] for i in range(num_nodes)]
    
    for line in data:
            items = line.split()
            G[int(items[0])-1] += [str(items[1])]
    G = dict(zip([str(i) for i in range(1, num_nodes, 1)], G))
        
    return G