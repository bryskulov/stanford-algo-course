import merge_sort


def test_merge_sort1():
    """Basic case"""
    array = [1, 5, 6, 7, 3, 10, 2, 8]
    actual_result = merge_sort.merge_sort(array)
    predicted_result = [1, 2, 3, 5, 6, 7, 8, 10]
    assert actual_result == predicted_result

def test_merge_sort2():
    """Empty list"""
    array = []
    actual_result = merge_sort.merge_sort(array)
    predicted_result = []
    assert actual_result == predicted_result

def test_merge_sort3():
    """Already sorted list"""
    array = [1, 2, 3, 5, 6, 7, 8, 10]
    actual_result = merge_sort.merge_sort(array)
    predicted_result = [1, 2, 3, 5, 6, 7, 8, 10]
    assert actual_result == predicted_result

def test_merge_sort4():
    """Reverse sorted list"""
    array = [10, 8, 7, 6, 5, 3, 2, 1]
    actual_result = merge_sort.merge_sort(array)
    predicted_result = [1, 2, 3, 5, 6, 7, 8, 10]
    assert actual_result == predicted_result

def test_merge_sort5():
    """Duplicate elements list"""
    array = [1, 1, 1, 2, 3, 4, 4, 5]
    actual_result = merge_sort.merge_sort(array)
    predicted_result = [1, 1, 1, 2, 3, 4, 4, 5]
    assert actual_result == predicted_result