from ntpy import factorize , prime_factorize , divisors , num_divisors , sum_divisors

def test_factorize():
    assert factorize(2) == {2: 1}
    assert factorize(12) == {2: 2, 3: 1}
    assert factorize(360) == {2: 3, 3: 2, 5: 1}

def test_prime_factorize():
    assert prime_factorize(2) == [2]
    assert prime_factorize(12) == [2, 3]
    assert prime_factorize(360) == [2, 3, 5]

def test_divisors():
    assert divisors(1) == [1]
    assert divisors(6) == [1, 2, 3, 6]
    assert divisors(12) == [1, 2, 3, 4, 6, 12]

def test_num_divisors():
    assert num_divisors(1) == 1
    assert num_divisors(6) == 4
    assert num_divisors(12) == 6
    assert num_divisors(36) == 9

def test_sum_divisors():
    assert sum_divisors(1) == 1
    assert sum_divisors(6) == 12
    assert sum_divisors(12) == 28
    assert sum_divisors(36) == 91
