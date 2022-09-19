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