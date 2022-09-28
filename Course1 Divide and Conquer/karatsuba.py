def karatsuba(x, y):
    """
    Input:
        x: integer
        y: integer
    Output
        result: x*y (multiplication of two integers)
    """
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y

    n = max(len(str(x)), len(str(y)))
    n_half = n // 2

    a = x // (10**n_half)
    b = x % (10**n_half)
    c = y // (10**n_half)
    d = y % (10**n_half)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ab_cd = karatsuba(a+b, c+d)
    ad_bc = ab_cd - ac - bd
    result = ac*(10**(n_half*2)) + ad_bc*(10**n_half) + bd

    return result