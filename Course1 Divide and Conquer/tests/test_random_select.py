import random_select


def test_random_select1():
    """Basic case: select median"""
    A = [2, 4, 6, 1, 3, 7, 5, 9, 8]
    actual_result = random_select.random_select(A, 3)
    expected_result = 4
    assert actual_result == expected_result


def test_random_select2():
    """Select median in list where length is even"""
    A = [2, 4, 6, 1, 3, 7, 5, 9]
    actual_result = random_select.random_select(A, 3)
    expected_result = 4
    assert actual_result == expected_result


def test_random_select3():
    """Select first and last elements"""
    A = [2, 4, 6, 1, 3, 7, 5, 9]
    actual_result = [None] * 2
    actual_result[0] = random_select.random_select(A, 0)
    actual_result[1] = random_select.random_select(A, len(A)-1)
    expected_result = [1, 9]
    assert actual_result == expected_result


def test_random_select4():
    """Longer list"""
    A = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
    median_pos = len(A) // 2
    actual_result = random_select.random_select(A, median_pos-1)
    expected_result = 10
    assert actual_result == expected_result