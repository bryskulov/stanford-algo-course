import quick_sort


def test_partition():
    A = [3, 4, 7, 1, 5, 2, 8, 6]
    actual_result = quick_sort.partition(A)
    expected_result = ([2, 1, 3, 4, 5, 7, 8, 6], 2)
    assert actual_result == expected_result


def test_quick_sort1():
    A = [3, 4, 7, 1, 5, 2, 8, 6]
    actual_result, _ = quick_sort.quick_sort(A, method="first")
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8]
    assert actual_result == expected_result


def test_quick_sort2():
    """
    Tests the algorithm based on test cases provided by the course with first 10 integers.
    The elements in the expected_result come in cumulative way.
    """
    actual_result = quick_sort.count_comparisons("tests/quick_sort_integers.txt", n_digits=10)
    expected_result = [25, 56, 77]
    assert actual_result == expected_result


def test_quick_sort3():
    """
    Tests the algorithm based on test cases provided by the course with first 100 integers.
    The elements in the expected_result come in cumulative way.
    """
    actual_result = quick_sort.count_comparisons("tests/quick_sort_integers.txt", n_digits=100)
    expected_result = [620, 1193, 1695]
    assert actual_result == expected_result


def test_quick_sort4():
    """
    Tests the algorithm based on test cases provided by the course with first 1000 integers.
    The elements in the expected_result come in cumulative way.
    """
    actual_result = quick_sort.count_comparisons("tests/quick_sort_integers.txt", n_digits=1000)
    expected_result = [11175, 22132, 31867]
    assert actual_result == expected_result