from pathlib import Path
from  count_inversions import countSplitInv, count_inversions


def open_test_file():
    test_directory = Path(__file__).parent
    with open(test_directory / "integers.txt", "r") as f_in:
        test_array = [int(i) for i in f_in.read().splitlines()]
    return test_array

def test_countSplitInv():
    B = [1, 3, 5]
    C = [2, 4, 6]
    actual_result = countSplitInv(B, C)
    expected_result = ([1, 2, 3, 4, 5, 6], 3)
    assert actual_result == expected_result

def test_count_inversions1():
    A = [1, 3, 5, 2, 4, 6]
    _, actual_result = count_inversions(A)
    expected_result = 3
    assert actual_result == expected_result

def test_count_inversions2():
    A = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
    _, actual_result = count_inversions(A)
    expected_result = 56
    assert actual_result == expected_result

def test_count_inversions3():
    A = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
    _, actual_result = count_inversions(A)
    expected_result = 590
    assert actual_result == expected_result

def test_count_inversions4():
    A = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
    _, actual_result = count_inversions(A)
    expected_result = 2372
    assert actual_result == expected_result

def test_count_inversions5():
    A = open_test_file()
    _, actual_result = count_inversions(A)
    expected_result = 2407905288
    assert actual_result == expected_result