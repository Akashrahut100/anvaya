"""
Number Theory Module for Anvaya.

Provides functions for prime numbers, factorization, modular arithmetic,
and other number-theoretic operations.
"""
from typing import Dict, List, Optional, Tuple
from functools import lru_cache
from sympy import gcd as sp_gcd, lcm as sp_lcm
import sympy.ntheory as nt
# Use new location for totient (fixes SymPy 1.13+ deprecation warning)
from sympy.functions.combinatorial.numbers import totient as sympy_totient


def prime_factors(n: int) -> Dict[int, int]:
    """
    Compute prime factorization of n.
    
    Parameters
    ----------
    n : int
        Positive integer to factorize.
    
    Returns
    -------
    dict
        Dictionary mapping prime factors to their exponents.
        Example: 360 -> {2: 3, 3: 2, 5: 1}
    
    Examples
    --------
    >>> prime_factors(360)
    {2: 3, 3: 2, 5: 1}
    """
    if n < 1:
        raise ValueError(f"n must be a positive integer, got {n}")
    return nt.factorint(n)


# Alias for backward compatibility
factorint = prime_factors


@lru_cache(maxsize=10000)
def is_prime(n: int) -> bool:
    """
    Check if n is a prime number.
    
    Uses Miller-Rabin primality test for large numbers.
    Results are cached for repeated calls.
    
    Parameters
    ----------
    n : int
        Integer to test.
    
    Returns
    -------
    bool
        True if n is prime, False otherwise.
    """
    return nt.isprime(n)


# Alias for backward compatibility
isprime = is_prime


def primerange(a: int, b: int) -> List[int]:
    """
    Generate all primes in the range [a, b).
    
    Parameters
    ----------
    a : int
        Start of range (inclusive).
    b : int
        End of range (exclusive).
    
    Returns
    -------
    list of int
        List of prime numbers in the range.
    
    Examples
    --------
    >>> primerange(10, 30)
    [11, 13, 17, 19, 23, 29]
    """
    return list(nt.primerange(a, b))


def gcd(a: int, b: int) -> int:
    """
    Compute Greatest Common Divisor of a and b.
    
    Parameters
    ----------
    a, b : int
        Integers (can be negative).
    
    Returns
    -------
    int
        The greatest common divisor, always non-negative.
    
    Examples
    --------
    >>> gcd(48, 18)
    6
    """
    return int(sp_gcd(a, b))


def lcm(a: int, b: int) -> int:
    """
    Compute Least Common Multiple of a and b.
    
    Parameters
    ----------
    a, b : int
        Integers (can be negative).
    
    Returns
    -------
    int
        The least common multiple, always non-negative.
    
    Examples
    --------
    >>> lcm(12, 18)
    36
    """
    return int(sp_lcm(a, b))


def totient(n: int) -> int:
    """
    Compute Euler's totient function φ(n).
    
    φ(n) counts the positive integers up to n that are relatively prime to n.
    
    Parameters
    ----------
    n : int
        Positive integer.
    
    Returns
    -------
    int
        Number of integers in [1, n] coprime to n.
    
    Examples
    --------
    >>> totient(10)  # {1, 3, 7, 9} are coprime to 10
    4
    """
    if n < 1:
        raise ValueError(f"n must be a positive integer, got {n}")
    return int(sympy_totient(n))


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    
    Finds (gcd, x, y) such that a*x + b*y = gcd(a, b).
    
    Parameters
    ----------
    a, b : int
        Input integers.
    
    Returns
    -------
    tuple of (int, int, int)
        (gcd, x, y) where a*x + b*y = gcd.
    
    Examples
    --------
    >>> extended_gcd(35, 15)
    (5, 1, -2)  # 35*1 + 15*(-2) = 5
    """
    from sympy import gcdex
    x, y, g = gcdex(a, b)
    return int(g), int(x), int(y)


def mod_inverse(a: int, m: int) -> int:
    """
    Compute modular multiplicative inverse of a modulo m.
    
    Finds x such that (a * x) % m == 1.
    
    Parameters
    ----------
    a : int
        Integer to find inverse of.
    m : int
        Modulus (must be positive).
    
    Returns
    -------
    int
        The modular inverse x, where 0 <= x < m.
    
    Raises
    ------
    ValueError
        If a and m are not coprime (inverse doesn't exist).
    
    Examples
    --------
    >>> mod_inverse(3, 11)
    4  # because 3 * 4 = 12 ≡ 1 (mod 11)
    """
    from sympy import mod_inverse as sp_mod_inverse
    try:
        return int(sp_mod_inverse(a, m))
    except ValueError:
        raise ValueError(f"Modular inverse of {a} mod {m} does not exist (not coprime)")


def is_coprime(a: int, b: int) -> bool:
    """
    Check if two integers are coprime (relatively prime).
    
    Parameters
    ----------
    a, b : int
        Integers to check.
    
    Returns
    -------
    bool
        True if gcd(a, b) == 1.
    """
    return gcd(a, b) == 1


def discrete_log(n: int, a: int, b: int) -> int:
    """
    Compute discrete logarithm.
    
    Finds x such that b^x ≡ a (mod n).
    
    Parameters
    ----------
    n : int
        Modulus.
    a : int
        Target value.
    b : int
        Base.
    
    Returns
    -------
    int
        The discrete logarithm x.
    """
    return nt.discrete_log(n, a, b)


def crt(remainders: List[int], moduli: List[int]) -> Tuple[int, int]:
    """
    Chinese Remainder Theorem.
    
    Finds x such that x ≡ remainders[i] (mod moduli[i]) for all i.
    
    Parameters
    ----------
    remainders : list of int
        List of remainders [a1, a2, ...].
    moduli : list of int
        List of pairwise coprime moduli [n1, n2, ...].
    
    Returns
    -------
    tuple of (int, int)
        (x, N) where x is the unique solution mod N, and N = product of moduli.
    
    Examples
    --------
    >>> crt([2, 3, 2], [3, 5, 7])
    (23, 105)  # 23 ≡ 2 (mod 3), 23 ≡ 3 (mod 5), 23 ≡ 2 (mod 7)
    """
    from sympy.ntheory.modular import crt as sympy_crt
    result = sympy_crt(moduli, remainders)
    if result is None:
        raise ValueError("No solution exists (moduli may not be pairwise coprime)")
    return result


def to_hex(n: int) -> str:
    """
    Convert an integer to its hexadecimal representation.
    """
    return hex(n)


def to_bin(n: int) -> str:
    """
    Convert an integer to its binary representation.
    
    Examples
    --------
    >>> to_bin(10)
    '0b1010'
    """
    return bin(n)


def to_oct(n: int) -> str:
    """
    Convert an integer to its octal representation.
    
    Examples
    --------
    >>> to_oct(8)
    '0o10'
    """
    return oct(n)


def from_base(s: str, base: int) -> int:
    """
    Convert a string representation in a given base back to a decimal integer.
    
    Parameters
    ----------
    s : str
        The string to convert (e.g., '0xff', '1010').
    base : int
        The base of the input string (e.g., 2, 8, 16).
        Use 0 to automatically detect base from prefixes like '0b', '0o', '0x'.
        
    Returns
    -------
    int
        The decimal integer value.
        
    Examples
    --------
    >>> from_base('0xff', 16)
    255
    >>> from_base('1010', 2)
    10
    """
    return int(s, base)


def convert_base(val: str, from_base: int, to_base: int) -> str:
    """
    Convert a number string from one base to another.
    
    Parameters
    ----------
    val : str
        The value to convert as a string.
    from_base : int
        The base of the input value.
    to_base : int
        The target base to convert to (2, 8, 10, or 16).
        Currently supports targets 2, 8, 10, 16.
        
    Returns
    -------
    str
        The value in the target base as a string.
        
    Examples
    --------
    >>> convert_base('1010', 2, 16)
    '0xa'
    >>> convert_base('ff', 16, 2)
    '0b11111111'
    """
    decimal_val = int(val, from_base)
    
    if to_base == 10:
        return str(decimal_val)
    elif to_base == 2:
        return bin(decimal_val)
    elif to_base == 8:
        return oct(decimal_val)
    elif to_base == 16:
        return hex(decimal_val)
    else:
        # Generic conversion for other bases if needed, 
        # but for now we'll stick to common ones.
        raise ValueError(f"Target base {to_base} not directly supported in this simple helper.")



