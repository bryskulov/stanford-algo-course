from pathlib import Path


NUM_COMPARISONS = 0

def quick_sort(A, method):
    """
    Input:
        A: Array with n distinct elements in any order
    Output"
        A: Array in sorted order
    """
    global NUM_COMPARISONS
    if len(A) <= 1:
        return A, 0
    A = choose_pivot(A, method=method)
    A, pivot_pos = partition(A)
    A[:pivot_pos], _ = quick_sort(A[:pivot_pos], method)
    A[pivot_pos+1:], _ = quick_sort(A[pivot_pos+1:], method)

    NUM_COMPARISONS += len(A[:pivot_pos]) + len(A[pivot_pos+1:])

    return A, NUM_COMPARISONS


def choose_pivot(A, method):
    """
    Input:
        A: Array of size n
        method: which pivot to pick
    Output"
        A: Array A with pivot element p, put at first position of A
    """  
    if method == 'first':
        A = A
    elif method == 'last':
        A[0], A[-1] = A[-1], A[0]
    elif method == 'median':
        n = len(A)
        middle = A[(n-1)//2]
        cand = [A[0], middle, A[-1]]

        if cand[0] > cand[1]:
            if cand[0] < cand[2]:
                A = A
            elif cand[1] > cand[2]:
                A[0], A[(n-1)//2] = A[(n-1)//2], A[0]
            else:
                A[0], A[-1] = A[-1], A[0]
        else:
            if cand[0] > cand[2]:
                A = A
            elif cand[1] < cand[2]:
                A[0], A[(n-1)//2] = A[(n-1)//2], A[0]
            else:
                A[0], A[-1] = A[-1], A[0]

    return A
    

def partition(A):
    """
    Input"
        A: Array A with n(n > 1) distinct elements in any order
        and with pivot element p, put at first position of A
    Output:
        A: Array A partitioned around p
        pivot_pos: Pivot position after sorting
    """
    n = len(A)
    p = A[0]
    i = 1
    for j in range(1,n):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[0], A[i-1] = A[i-1], A[0]
    pivot_pos = i-1
    return A, pivot_pos


def open_test_file(file_path):
    test_directory = Path(__file__).parent
    with open(test_directory / file_path, "r") as f_in:
        test_A = [int(i) for i in f_in.read().splitlines()]
    return test_A


def count_comparisons(file_name, n_digits):
    global NUM_COMPARISONS
    NUM_COMPARISONS = 0
    array = open_test_file(file_name)
    _, count1 = quick_sort(array[:n_digits], method='first')
    _, count2 = quick_sort(array[:n_digits], method='last')
    _, count3 = quick_sort(array[:n_digits], method='median')
    counts = [count1, count2, count3]
    return counts