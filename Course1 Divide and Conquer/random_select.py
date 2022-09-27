def random_select(A, i):
    """
    Input:
        A: Array with n distinct elements in any order
        i: Integer i, i-th order  statistic indexed from 0 to n-1
    Output:
        ith order statistic of A
    """
    print(A)
    if len(A) == 1:
        return A[0]

    p = A[0]
    A, pivot_pos = partition(A)
    if pivot_pos == i:
        return p
    elif pivot_pos > i:
        return random_select(A[:pivot_pos], i)
    else:
        return random_select(A[pivot_pos+1:], i - (pivot_pos+1))


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