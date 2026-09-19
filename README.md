# ntpy

**ntpy** is a Python library for number theory and mathematical computations.

## Features

* Prime number generation
* Primality testing
* Integer factorization
* Prime factorization
* Divisor calculations
* Euler's totient function
* Möbius function
* Chinese Remainder Theorem

## Installation

```bash
pip install git+https://github.com/Mustafa200215/ntpy.git
```

## Usage

```python
import ntpy
```

### Prime numbers

```python
ntpy.is_prime(17)
# True

ntpy.generate_primes(20)
# [2, 3, 5, 7, 11, 13, 17, 19]
```

### Factorization

```python
ntpy.factorize(360)
# {2: 3, 3: 2, 5: 1}
ntpy.prime_factorize(360)
# [2,3,5]
```

### Divisors

```python
ntpy.divisors(12)
# [1, 2, 3, 4, 6, 12]

ntpy.num_divisors(12)
# 6

ntpy.sum_divisors(12)
# 28
```

### Euler's totient function

```python
ntpy.euler_phi(10)
# 4
```

### Möbius function

```python
ntpy.mobius(30)
# -1
```

### Chinese Remainder Theorem

```python
ntpy.crt([3, 5], [2, 3])
# (15, 8)
```

This represents:

```text
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)
```

The result means:

```text
x ≡ 8 (mod 15)
```

## License

This project is licensed under the MIT License.

## Author

**Mustafa Hato**

Project identity: **MHD**
