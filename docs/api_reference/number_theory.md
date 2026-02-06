# API Reference: Number Theory

## Module: `anvaya.number_theory`

---

## Functions

### `is_prime`

```python
is_prime(n: int) -> bool
```

Checks if a number is prime using Miller-Rabin primality test.

---

### `prime_factors`

```python
prime_factors(n: int) -> dict
```

Computes the prime factorization of a number.

**Returns:** `dict` — Primes as keys, exponents as values.

---

### `gcd` / `lcm`

```python
gcd(a: int, b: int) -> int
lcm(a: int, b: int) -> int
```

Computes the Greatest Common Divisor or Least Common Multiple.

---

### `totient`

```python
totient(n: int) -> int
```

Computes Euler's totient function $\phi(n)$.

---

### `mod_inverse`

```python
mod_inverse(a: int, m: int) -> int
```

Computes the modular multiplicative inverse of $a$ modulo $m$.

---

### `crt`

```python
crt(remainders: list, moduli: list) -> tuple
```

Chinese Remainder Theorem solver.

**Returns:** `(x, N)` — Solution $x$ mod $N$.

---

### Base Conversion

| Function | Description |
|----------|-------------|
| `to_bin(n)` | Int to Binary string |
| `to_oct(n)` | Int to Octal string |
| `to_hex(n)` | Int to Hex string |
| `from_base(s, base)` | String to Int |
| `convert_base(val, b1, b2)` | Change base of a string |
