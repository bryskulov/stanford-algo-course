import karatsuba

def test_karatsuba1():
    actual_result = karatsuba.karatsuba(5678, 1234)
    expected_result = 7006652
    assert actual_result == expected_result

def test_karatsuba2():
    actual_result = karatsuba.karatsuba(567, 123)
    expected_result = 69741
    assert actual_result == expected_result

def test_karatsuba3():
    actual_result = karatsuba.karatsuba(10000, 10000)
    expected_result = 100000000
    assert actual_result == expected_result

def test_karatsuba4():
    actual_result = karatsuba.karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 
        2718281828459045235360287471352662497757247093699959574966967627)
    expected_result = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
    assert actual_result == expected_result