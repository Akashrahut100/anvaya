# Quickstart Guide

Get up and running with Anvaya in 5 minutes! This guide covers the essential concepts and common use cases.

---

## 🎯 Basic Concepts

### Symbolic Variables

Most Anvaya operations work with **symbolic variables**. Create them using the `var` function:

```python
from anvaya.symbolic import var

# Single variable
x = var('x')

# Multiple variables
x, y, z = var('x y z')
```

### Expression Building

Build mathematical expressions naturally:

```python
from anvaya.symbolic import var

x = var('x')

# Expressions
expr1 = x**2 + 2*x + 1
expr2 = (x + 1)**2
expr3 = x**3 - x
```

---

## 📐 Algebra

### Solving Equations

```python
from anvaya import algebra
from anvaya.symbolic import var

x = var('x')

# Linear equation
algebra.solve_linear([2*x + 4], [x])  # {x: -2}

# Quadratic equation
algebra.solve_quadratic(x**2 - 5*x + 6, x)  # [2, 3]

# System of equations
y = var('y')
algebra.solve_system([x + y - 5, x - y - 1], [x, y])  # {x: 3, y: 2}
```

### Polynomial Operations

```python
from anvaya import algebra
from anvaya.symbolic import var

x = var('x')

# Expand
algebra.expand_poly((x + 1)**3)  # x**3 + 3*x**2 + 3*x + 1

# Factor
algebra.factor_poly(x**2 - 4)  # (x - 2)*(x + 2)

# Partial fractions
algebra.partial_fraction(1/(x**2 - 1), x)  # -1/(2*(x + 1)) + 1/(2*(x - 1))
```

---

## 📊 Calculus

### Differentiation

```python
from anvaya import calculus
from anvaya.symbolic import var

x = var('x')

# First derivative
calculus.diff(x**3, x)  # 3*x**2

# Higher order derivative
calculus.diff(x**4, x, order=2)  # 12*x**2
```

### Integration

```python
from anvaya import calculus
from anvaya.symbolic import var

x = var('x')

# Indefinite integral
calculus.integrate(x**2, x)  # x**3/3

# Definite integral
calculus.integrate(x**2, x, lower=0, upper=1)  # 1/3
```

### Limits

```python
from anvaya import calculus
from anvaya.symbolic import var
import sympy as sp

x = var('x')

# Limit at a point
calculus.limit(sp.sin(x)/x, x, 0)  # 1

# Limit at infinity
calculus.limit(1/x, x, sp.oo)  # 0
```

### Series Expansion

```python
from anvaya import calculus
from anvaya.symbolic import var
import sympy as sp

x = var('x')

# Taylor series around x=0
calculus.taylor_series(sp.exp(x), x, 0, 5)  # 1 + x + x**2/2 + x**3/6 + x**4/24
```

---

## 🔢 Linear Algebra

### Matrix Operations

```python
from anvaya import linear_algebra as la

# Create matrices
A = la.matrix([[1, 2], [3, 4]])
B = la.matrix([[5, 6], [7, 8]])

# Multiplication
C = la.multiply(A, B)

# Determinant
det = la.determinant(A)  # -2.0

# Inverse
A_inv = la.inverse(A)

# Trace
tr = la.trace(A)  # 5.0
```

### Eigenvalues

```python
from anvaya import linear_algebra as la

A = la.matrix([[4, 2], [1, 3]])
result = la.eigenvalues(A)

print(result.values)   # Eigenvalues
print(result.vectors)  # Eigenvectors
```

### Solving Linear Systems

```python
from anvaya import linear_algebra as la

# Solve Ax = b
A = la.matrix([[2, 1], [1, 3]])
b = [1, 2]

x = la.solve_linear_system(A, b)  # [0.2, 0.6]
```

---

## 🎲 Probability & Statistics

### Probability Distributions

```python
from anvaya import probability as prob

# Normal distribution
normal = prob.Normal(mean=0, std=1)
normal.pdf(0)      # 0.3989...
normal.cdf(1.96)   # 0.975...
normal.sample(5)   # Array of 5 random samples

# Binomial distribution
binom = prob.Binomial(n=10, p=0.5)
binom.pmf(5)       # P(X = 5)

# Poisson distribution
poisson = prob.Poisson(mu=3)
poisson.pmf(2)     # P(X = 2)
```

### Bayes' Theorem

```python
from anvaya import probability as prob

# P(A|B) = P(B|A) * P(A) / P(B)
prob.bayes_theorem(
    p_b_given_a=0.99,  # Sensitivity
    p_a=0.01,          # Prevalence
    p_b=0.05           # Positive rate
)  # 0.198
```

### Descriptive Statistics

```python
from anvaya import statistics as stats

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

stats.mean(data)       # 5.5
stats.median(data)     # 5.5
stats.variance(data)   # 8.25
stats.stdev(data)      # 2.87...
stats.percentile(data, 75)  # 7.75
```

---

## 🔐 Number Theory

```python
from anvaya import number_theory as nt

# Primality
nt.is_prime(17)           # True
nt.primerange(10, 30)     # [11, 13, 17, 19, 23, 29]

# Factorization
nt.prime_factors(360)     # {2: 3, 3: 2, 5: 1}

# GCD and LCM
nt.gcd(48, 18)            # 6
nt.lcm(12, 18)            # 36

# Modular arithmetic
nt.mod_inverse(3, 11)     # 4 (because 3*4 ≡ 1 mod 11)

# Chinese Remainder Theorem
nt.crt([2, 3, 2], [3, 5, 7])  # (23, 105)
```

---

## 📈 Optimization

```python
from anvaya import optimization as opt
import numpy as np

# Minimize a function
def f(x):
    return x[0]**2 + x[1]**2

result = opt.minimize(f, x0=[1, 1])
print(result.x)  # [0, 0]

# Gradient descent
def grad(x):
    return [2*x[0], 2*x[1]]

x_opt = opt.gradient_descent(f, grad, x0=[5, 5])
```

---

## 🕸️ Graph Theory

```python
from anvaya import graph_theory as gt

# Create a graph
G = gt.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 4)])

# Shortest path
path = gt.shortest_path(G, 1, 3)  # [1, 2, 3]

# BFS and DFS
bfs = gt.bfs_tree(G, 1)
dfs = gt.dfs_tree(G, 1)
```

---

## ⚠️ Error Handling

Anvaya provides custom exceptions for clear error messages:

```python
from anvaya import linear_algebra as la
from anvaya.core.exceptions import SingularMatrixError, DimensionMismatchError

try:
    # Singular matrix (determinant = 0)
    A = la.matrix([[1, 2], [2, 4]])
    la.inverse(A)
except SingularMatrixError as e:
    print(f"Cannot invert: {e}")

try:
    # Dimension mismatch
    A = la.matrix([[1, 2, 3]])
    B = la.matrix([[1], [2]])
    la.multiply(A, B)
except DimensionMismatchError as e:
    print(f"Dimension error: {e}")
```

---

## 📝 Next Steps

Now that you know the basics, explore the detailed module documentation:

- [Algebra](algebra.md)
- [Calculus](calculus.md)
- [Linear Algebra](linear_algebra.md)
- [Probability](probability.md)
- [Statistics](statistics.md)
- [Number Theory](number_theory.md)

Or see the complete [API Reference](api_reference/index.md).
