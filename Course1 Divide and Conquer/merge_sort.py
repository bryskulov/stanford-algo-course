def merge_sort(array):
    """
    Input: Unsorted array of length n
    Output: Sorted array of length n

    A = 1st sorted sub-array, of length bn=2c
    B = 2nd sorted sub-array, of length dn=2e
    C = Sorted array of length n
    """
    n = len(array)
    if n <= 1:
        return array
    
    n_half = n // 2
    A = array[:n_half]
    B = array[n_half:]

    A = merge_sort(A)
    B = merge_sort(B)

    C = [None]*n
    i = 0
    j = 0
    for k in range(n):
        if i == len(A):
            C[k] = B[j]
            j += 1
        elif j == len(B):
            C[k] = A[i]
            i += 1
        elif A[i] <= B[j]:
            C[k] = A[i]
            i += 1
        elif A[i] > B[j]:
            C[k] = B[j]
            j += 1
    return C