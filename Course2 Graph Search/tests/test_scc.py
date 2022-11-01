from pathlib import Path

from scc import Graph


def test_compute_scc1():
    expected_result = [3, 3, 3, 0, 0]
    G = Graph(10, 'tests/test_files/scc1.txt')
    actual_result = G.run()
    assert actual_result == expected_result


def test_compute_scc2():
    expected_result = [3, 3, 2, 0, 0]
    G = Graph(9, 'tests/test_files/scc2.txt')
    actual_result = G.run()
    assert actual_result == expected_result


def test_compute_scc3():
    expected_result = [3, 3, 1, 1, 0]
    G = Graph(9, 'tests/test_files/scc3.txt')
    actual_result = G.run()
    assert actual_result == expected_result


def test_compute_scc4():
    expected_result = [7, 1, 0, 0, 0]
    G = Graph(9, 'tests/test_files/scc4.txt')
    actual_result = G.run()
    assert actual_result == expected_result


def test_compute_scc5():
    expected_result = [6, 3, 2, 1, 0]
    G = Graph(13, 'tests/test_files/scc5.txt')
    actual_result = G.run()
    assert actual_result == expected_result


def test_compute_SCC():
    expected_result = [434821, 968, 459, 313, 211]
    G = Graph(875715, 'tests/test_files/SCC.txt')
    actual_result = G.run()
    assert actual_result == expected_result