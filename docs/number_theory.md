# Number Theory Module

The `number_theory` module provides functions for primes, factorization, and modular arithmetic.

---

## Import

```python
from anvaya import number_theory as nt
```

---

## Functions

### `is_prime(n)` / `isprime(n)`
Tests if n is prime.

```python
nt.is_prime(17)  # True
nt.is_prime(18)  # False
```

---

### `prime_factors(n)` / `factorint(n)`
Prime factorization.

```python
nt.prime_factors(360)  # {2: 3, 3: 2, 5: 1}
```

---

### `primerange(a, b)`
All primes in [a, b).

```python
nt.primerange(10, 30)  # [11, 13, 17, 19, 23, 29]
```

---

### `gcd(a, b)`
Greatest Common Divisor.

```python
nt.gcd(48, 18)  # 6
```

---

### `lcm(a, b)`
Least Common Multiple.

```python
nt.lcm(12, 18)  # 36
```

---

### `totient(n)`
Euler's totient φ(n).

```python
nt.totient(10)  # 4 ({1, 3, 7, 9} coprime to 10)
```

---

### `extended_gcd(a, b)`
Returns (gcd, x, y) where ax + by = gcd.

```python
nt.extended_gcd(35, 15)  # (5, 1, -2)
```

---

### `mod_inverse(a, m)`
Modular inverse: (a × x) % m = 1

```python
nt.mod_inverse(3, 11)  # 4
```

---

### `is_coprime(a, b)`
Check if gcd(a, b) = 1.

```python
nt.is_coprime(15, 28)  # True
```

---

### `discrete_log(n, a, b)`
Finds x where b^x ≡ a (mod n).

```python
nt.discrete_log(17, 3, 2)
```

---

### `crt(remainders, moduli)`
Chinese Remainder Theorem.

```python
nt.crt([2, 3, 2], [3, 5, 7])  # (23, 105)
```

---

### `to_hex(n)` / `to_bin(n)` / `to_oct(n)`
Base conversions.

```python
nt.to_hex(255)  # '0xff'
nt.to_bin(10)   # '0b1010'
nt.to_oct(64)   # '0o100'
```

---

## See Also

- [Algebra](algebra.md)
