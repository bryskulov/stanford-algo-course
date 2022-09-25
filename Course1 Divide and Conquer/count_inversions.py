def count_inversions(array):
    """
    Input:
        array = Array of length n
    Output
        Number of inversions of the input array A
    """
    if len(array) == 1:
        return array, 0
    
    n = len(array)
    n_half = n // 2

    B = array[:n_half]
    C = array[n_half:]
    B, x = count_inversions(B)
    C, y = count_inversions(C)
    D, z = countSplitInv(B, C)
    return D, x + y + z

def countSplitInv(B, C):
    """
    Input:
        B = 1st sorted sub-array, of length n/2
        C = 2nd sorted sub-array, of length n/2
    Output:
        D = sorted array of length n
        numSplitInv = number of split inversions
    """
    n = len(B) + len(C)
    D = [None]*n
    i = 0
    j = 0
    numSplitInv = 0
    for k in range(n):
        if i == len(B):
            D[k] = C[j]
            j += 1
        elif j == len(C):
            D[k] = B[i]
            i += 1
        elif B[i] <= C[j]:
            D[k] = B[i]
            i += 1
        else:
            D[k] = C[j]
            j += 1
            numSplitInv += len(B[i:])
    
    return D, numSplitInv