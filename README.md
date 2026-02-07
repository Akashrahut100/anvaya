<p align="center">
  <img src="https://raw.githubusercontent.com/Akashrahut100/anvaya/master/docs/assets/anvaya.png" alt="Anvaya Logo" width="300">
</p>

<h1 align="center">Anvaya (अन्वय)</h1>
<h3 align="center">A Comprehensive Python Mathematics Library</h3>

<p align="center">
  <a href="https://badge.fury.io/py/anvaya"><img src="https://badge.fury.io/py/anvaya.svg" alt="PyPI version"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+"></a>
  <a href="https://github.com/Akashrahut100/anvaya/graphs/commit-activity"><img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintenance"></a>
</p>

---

[![PyPI version](https://badge.fury.io/py/anvaya.svg)](https://badge.fury.io/py/anvaya)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Akashrahut100/anvaya/graphs/commit-activity)

> **Anvaya** (Sanskrit: अन्वय) means "logical connection" or "coherent reasoning." It represents the systematic thread that links mathematical premises to universal truths.

Anvaya is a production-ready, high-performance mathematics library for Python. It bridges the gap between symbolic reasoning and numerical computation, providing a unified interface for 14 different mathematical domains.

---

## 📑 Table of Contents
- [📚 Detailed Documentation](#-detailed-documentation)
- [📦 Installation](#-installation)
- [🚀 Quick Start](#-quick-start)
- [🧮 Domain Guides](#-domain-guides)
  - [1. Algebra](#1-algebra)
  - [2. Linear Algebra](#2-linear-algebra)
  - [3. Calculus](#3-calculus)
  - [4. Probability](#4-probability)
  - [5. Statistics](#5-statistics)
  - [6. Number Theory](#6-number-theory)
  - [7. Numerical Methods](#7-numerical-methods)
  - [8. Complex Analysis](https://github.com/Akashrahut100/anvaya/blob/master/docs/complex_analysis.md)
  - [9. Differential Equations](https://github.com/Akashrahut100/anvaya/blob/master/docs/differential_equations.md)
  - [10. Graph Theory](https://github.com/Akashrahut100/anvaya/blob/master/docs/graph_theory.md)
  - [11. Optimization](https://github.com/Akashrahut100/anvaya/blob/master/docs/optimization.md)
  - [12. Discrete Math](https://github.com/Akashrahut100/anvaya/blob/master/docs/discrete.md)
  - [13. Vector Calculus](https://github.com/Akashrahut100/anvaya/blob/master/docs/vector_calculus.md)
  - [14. Symbolic Engine](#-symbolic-engine)
- [🛠 Advanced Features](#-advanced-features)
- [🧬 Symbolic Engine](#-symbolic-engine)
- [🤝 Contributing](#-contributing)

---

## � Detailed Documentation

Since Anvaya covers 14+ mathematical domains, we have detailed guides for each. You can access them directly on GitHub by clicking the links below:

| Category | Detailed Guide | API Reference |
| :--- | :--- | :--- |
| **Getting Started** | [Installation](https://github.com/Akashrahut100/anvaya/blob/master/docs/installation.md) \| [Quick Start](https://github.com/Akashrahut100/anvaya/blob/master/docs/quickstart.md) | - |
| **Core domains** | [Algebra](https://github.com/Akashrahut100/anvaya/blob/master/docs/algebra.md) \| [Linear Algebra](https://github.com/Akashrahut100/anvaya/blob/master/docs/linear_algebra.md) \| [Calculus](https://github.com/Akashrahut100/anvaya/blob/master/docs/calculus.md) | [API](https://github.com/Akashrahut100/anvaya/blob/master/docs/api_reference/index.md) |
| **Probability & Stats** | [Probability](https://github.com/Akashrahut100/anvaya/blob/master/docs/probability.md) \| [Statistics](https://github.com/Akashrahut100/anvaya/blob/master/docs/statistics.md) | [API](https://github.com/Akashrahut100/anvaya/blob/master/docs/api_reference/statistics.md) |
| **Advanced Math**| [Complex Analysis](https://github.com/Akashrahut100/anvaya/blob/master/docs/complex_analysis.md) \| [Number Theory](https://github.com/Akashrahut100/anvaya/blob/master/docs/number_theory.md) \| [Differential Eqs](https://github.com/Akashrahut100/anvaya/blob/master/docs/differential_equations.md) | [API](https://github.com/Akashrahut100/anvaya/blob/master/docs/api_reference/number_theory.md) |
| **Applied Math** | [Graph Theory](https://github.com/Akashrahut100/anvaya/blob/master/docs/graph_theory.md) \| [Numerical Methods](https://github.com/Akashrahut100/anvaya/blob/master/docs/numerical.md) \| [Optimization](https://github.com/Akashrahut100/anvaya/blob/master/docs/optimization.md) | [API](https://github.com/Akashrahut100/anvaya/blob/master/docs/api_reference/numerical.md) |
| **Discrete & Others**| [Discrete Math](https://github.com/Akashrahut100/anvaya/blob/master/docs/discrete.md) \| [Vector Calculus](https://github.com/Akashrahut100/anvaya/blob/master/docs/vector_calculus.md) \| [Symbolic Engine](https://github.com/Akashrahut100/anvaya/blob/master/docs/symbolic_engine.md) | [API](https://github.com/Akashrahut100/anvaya/blob/master/docs/api_reference/symbolic.md) |

---


## �📦 Installation

Anvaya requires Python 3.8 or higher. Use `pip` to install:

```bash
pip install anvaya
```

---

## 🚀 Quick Start

Solving a complex problem with Anvaya is intuitive. Here is a 30-second example of symbolic variables, algebra, and calculus working together:

```python
from anvaya import algebra, calculus
from anvaya.symbolic import var

# 1. Define variables
x = var('x')

# 2. Expand a polynomial
polynomial = (x + 3)**2
expanded = algebra.expand_poly(polynomial)
print(f"Expanded: {expanded}")  # x**2 + 6*x + 9

# 3. Find the derivative
derivative = calculus.diff(expanded, x)
print(f"Derivative: {derivative}")  # 2*x + 6

# 4. Solve for roots
roots = algebra.solve_linear(derivative, x)
print(f"Roots: {roots}")  # [-3]
```

---

## 🧮 Domain Guides

### 1. [Algebra](https://github.com/Akashrahut100/anvaya/blob/master/docs/algebra.md)
Handle equations, polynomials, and simplifications with ease.

```python
from anvaya import algebra
from anvaya.symbolic import var

x = var('x')

# Solve quadratic equation x^2 - 5x + 6 = 0
roots = algebra.solve_quadratic(x**2 - 5*x + 6, x)
print(roots)  # [2, 3]

# Factorize expression
expr = x**2 + 2*x + 1
print(algebra.factor_poly(expr))  # (x + 1)**2
```

### 2. [Linear Algebra](https://github.com/Akashrahut100/anvaya/blob/master/docs/linear_algebra.md)
Perform matrix operations with high precision and safe error handling.

```python
from anvaya import linear_algebra as la
import numpy as np

# Create a matrix
A = la.matrix([[1, 2], [3, 4]])

# Calculate Determinant
print(la.determinant(A))  # -2.0

# Compute Eigenvalues and Eigenvectors (Structured Result)
result = la.eigenvalues(A)
print(f"Values: {result.values}")
print(f"Vectors:\n{result.vectors}")

# Solve System Ax = b
b = [5, 11]
x = la.solve_linear_system(A, b)
print(f"Solution: {x}") # [1.0, 2.0]
```

### 3. [Calculus](https://github.com/Akashrahut100/anvaya/blob/master/docs/calculus.md)
Perform symbolic differentiation, integration, and limit calculations.

```python
from anvaya import calculus
from anvaya.symbolic import var

x = var('x')

# Differentiation
print(calculus.diff(x**3, x))  # 3*x**2

# Definite Integration (from 0 to 1)
integral = calculus.integrate(x**2, x, 0, 1)
print(integral)  # 1/3

# Limits
print(calculus.limit(1/x, x, 0, direction='+'))  # oo (Infinity)
```

### 4. [Probability](https://github.com/Akashrahut100/anvaya/blob/master/docs/probability.md)
Modern API for probability distributions and Bayesian inference.

```python
from anvaya import probability as prob

# Probability Distributions
normal = prob.Normal(mean=0, std=1)
print(normal.pdf(0))  # 0.3989 (Bell curve peak)
print(normal.cdf(0))  # 0.5 (Area to the left)

# Bayes Theorem
# P(A|B) = P(B|A)*P(A) / P(B)
prob_a_given_b = prob.bayes_theorem(p_b_given_a=0.9, p_a=0.01, p_b=0.05)
print(f"Probability: {prob_a_given_b}") # 0.18
```

### 5. [Statistics](https://github.com/Akashrahut100/anvaya/blob/master/docs/statistics.md)
Descriptive statistics and data analysis tools.

```python
from anvaya import statistics as stats

# Descriptive Statistics
data = [10, 20, 20, 30, 40, 50]
print(stats.mean(data))    # 28.33
print(stats.median(data))  # 25.0
print(stats.mode(data))    # 20
print(stats.std(data))     # Standard deviation
```

### 6. [Number Theory](https://github.com/Akashrahut100/anvaya/blob/master/docs/number_theory.md)
Prime numbers, modular arithmetic, and ancient algorithms.

```python
from anvaya import number_theory as nt

# Prime factorization
print(nt.prime_factors(360))  # {2: 3, 3: 2, 5: 1}

# Euler's Totient
print(nt.totient(10))  # 4 (Numbers 1, 3, 7, 9 are coprime to 10)

# Modular Inverse
print(nt.mod_inverse(3, 11))  # 4 (3*4 = 12 ≡ 1 mod 11)

# Greatest Common Divisor
print(nt.gcd(48, 18))  # 6
```

### 7. [Numerical Methods](https://github.com/Akashrahut100/anvaya/blob/master/docs/numerical.md)
Root finding and numerical integration when symbolic math isn't enough.

```python
from anvaya import numerical

# Find root of f(x) = x^2 - 2 near x=1.5
def f(x): return x**2 - 2
root = numerical.root_find(f, 1.5)
print(f"Square root of 2 is approx: {root:.6f}") # 1.414214
```

---

## 🛠 Advanced Features

### Safe Error Handling
Anvaya doesn't just crash; it tells you *why* a calculation failed using custom exceptions.

```python
from anvaya import linear_algebra as la
from anvaya import SingularMatrixError

A = [[1, 1], [1, 1]] # Singular matrix (no inverse)

try:
    inv = la.inverse(A)
except SingularMatrixError as e:
    print(f"Math Error: {e}") # Matrix is singular or nearly singular
```

### Type Safety
Full support for Python type hints and PEP 561 compliance, making it perfect for large-scale applications with VS Code or PyCharm.

---

## 🧬 Symbolic Engine
The core of Anvaya is its `SymbolicEngine`. You can use it to parse strings into math or manipulate variables.

```python
from anvaya.symbolic import engine

# Parse from string
my_math = engine.expr("x**2 + 2*x + 1")
print(engine.factor(my_math)) # (x + 1)**2
```

---

## 🤝 Contributing
We welcome contributions to Anvaya! Whether it's adding new modules (like Tensor Calculus or Financial Math) or improving performance.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author
**Akash Rahut**
- GitHub: [@Akashrahut100](https://github.com/Akashrahut100)
- AI & Data Science Engineer
- Building intelligent, scalable, and data-driven systems at the intersection of mathematics, software architecture, and artificial intelligence.

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---

“स्थानात् स्थानं दशगुणं स्यात्”
— Āryabhaṭīya (499 CE)

(The logic of numbers shapes the universe)
