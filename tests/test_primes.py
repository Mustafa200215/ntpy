from ntpy import generate_primes , is_prime
def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(100) is False

def test_generate_primes():
    assert generate_primes(1) == []
    assert generate_primes(2) == [2]
    assert generate_primes(10) == [2, 3, 5, 7]
    assert generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
