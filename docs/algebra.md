# Algebra Module

The `algebra` module provides symbolic tools for solving equations, manipulating polynomials, and working with rational expressions.

---

## Overview

This module wraps SymPy's algebraic capabilities, providing a clean interface for:

- Solving linear and quadratic equations
- Solving systems of equations (linear and non-linear)
- Polynomial expansion and factorization
- Rational expression simplification
- Partial fraction decomposition

---

## Import

```python
from anvaya import algebra
from anvaya.symbolic import var
```

---

## Functions

### `solve_linear(equations, variables)`

Solves a system of linear equations.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `equations` | `list` | List of equations (expressions equal to 0) |
| `variables` | `list` | List of variables to solve for |

**Returns**

- `dict` — Dictionary mapping variables to their solutions

**Example**

```python
from anvaya import algebra
from anvaya.symbolic import var

x, y = var('x y')

# Single equation
result = algebra.solve_linear([2*x + 4], [x])
print(result)  # {x: -2}

# System of equations
result = algebra.solve_linear([x + y - 10, x - y - 2], [x, y])
print(result)  # {x: 6, y: 4}
```

---

### `solve_quadratic(equation, variable)`

Solves a quadratic equation.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `equation` | `Expr` | Quadratic expression (set equal to 0) |
| `variable` | `Symbol` | Variable to solve for |

**Returns**

- `list` — List of solutions (may include complex numbers)

**Example**

```python
from anvaya import algebra
from anvaya.symbolic import var

x = var('x')

# Real roots
roots = algebra.solve_quadratic(x**2 - 5*x + 6, x)
print(roots)  # [2, 3]

# Complex roots
roots = algebra.solve_quadratic(x**2 + 1, x)
print(roots)  # [-I, I]

# Using the quadratic formula form: ax² + bx + c = 0
roots = algebra.solve_quadratic(2*x**2 - 4*x - 6, x)
print(roots)  # [-1, 3]
```

---

### `expand_poly(expression)`

Expands a polynomial expression.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `expression` | `Expr` | Polynomial expression to expand |

**Returns**

- `Expr` — Expanded polynomial

**Example**

```python
from anvaya import algebra
from anvaya.symbolic import var

x = var('x')

# Binomial expansion
result = algebra.expand_poly((x + 1)**2)
print(result)  # x**2 + 2*x + 1

# More complex expansion
result = algebra.expand_poly((x + 1)**3)
print(result)  # x**3 + 3*x**2 + 3*x + 1

# Multiple variables
y = var('y')
result = algebra.expand_poly((x + y)**2)
print(result)  # x**2 + 2*x*y + y**2
```

---

### `factor_poly(expression)`

Factors a polynomial expression.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `expression` | `Expr` | Polynomial expression to factor |

**Returns**

- `Expr` — Factored form of the polynomial

**Example**

```python
from anvaya import algebra
from anvaya.symbolic import var

x = var('x')

# Simple factoring
result = algebra.factor_poly(x**2 - 4)
print(result)  # (x - 2)*(x + 2)

# Quadratic factoring
result = algebra.factor_poly(x**2 + 5*x + 6)
print(result)  # (x + 2)*(x + 3)

# Higher degree
result = algebra.factor_poly(x**3 - x)
print(result)  # x*(x - 1)*(x + 1)
```

---

### `rational_simplify(expression)`

Simplifies a rational expression by canceling common factors.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `expression` | `Expr` | Rational expression to simplify |

**Returns**

- `Expr` — Simplified expression

**Example**

```python
from anvaya import algebra
from anvaya.symbolic import var

x = var('x')

# Cancel common factors
result = algebra.rational_simplify((x**2 - 1)/(x - 1))
print(result)  # x + 1

# More complex
result = algebra.rational_simplify((x**2 - 4)/(x**2 - 4*x + 4))
print(result)  # (x + 2)/(x - 2)
```

---

### `partial_fraction(expression, variable)`

Computes partial fraction decomposition of a rational expression.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `expression` | `Expr` | Rational expression |
| `variable` | `Symbol` | Variable for decomposition |

**Returns**

- `Expr` — Partial fraction form

**Example**

```python
from anvaya import algebra
from anvaya.symbolic import var

x = var('x')

# Simple decomposition
result = algebra.partial_fraction(1/(x**2 - 1), x)
print(result)  # -1/(2*(x + 1)) + 1/(2*(x - 1))

# More complex
result = algebra.partial_fraction((x + 1)/(x**2 - 5*x + 6), x)
print(result)  # 4/(x - 3) - 3/(x - 2)
```

---

### `solve_system(equations, variables)`

Solves a system of equations (works for both linear and non-linear systems).

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `equations` | `list` | List of equations (expressions equal to 0) |
| `variables` | `list` | List of variables to solve for |

**Returns**

- `dict` or `list` — Solutions (format depends on the system)

**Example**

```python
from anvaya import algebra
from anvaya.symbolic import var

x, y = var('x y')

# Linear system
result = algebra.solve_system([x + y - 5, 2*x - y - 1], [x, y])
print(result)  # {x: 2, y: 3}

# Non-linear system (circle and line)
result = algebra.solve_system([x**2 + y**2 - 25, y - x], [x, y])
print(result)  # Multiple solutions

# Quadratic system
result = algebra.solve_system([x*y - 6, x + y - 5], [x, y])
print(result)  # [{x: 2, y: 3}, {x: 3, y: 2}]
```

---

## Common Use Cases

### Solving Word Problems

```python
from anvaya import algebra
from anvaya.symbolic import var

# "Two numbers sum to 100 and differ by 30. Find them."
x, y = var('x y')
solutions = algebra.solve_system([x + y - 100, x - y - 30], [x, y])
print(f"Numbers: {solutions[x]} and {solutions[y]}")  # 65 and 35
```

### Polynomial Long Division

```python
from anvaya import algebra
from anvaya.symbolic import var
import sympy as sp

x = var('x')

# Divide x³ - 1 by x - 1
quotient, remainder = sp.div(x**3 - 1, x - 1, x)
print(f"Quotient: {quotient}")    # x² + x + 1
print(f"Remainder: {remainder}")  # 0
```

### Finding Polynomial Roots

```python
from anvaya import algebra
from anvaya.symbolic import var

x = var('x')

# All roots of a cubic
roots = algebra.solve_system([x**3 - 6*x**2 + 11*x - 6], [x])
print(roots)  # [1, 2, 3]
```

---

## See Also

- [Symbolic Engine](symbolic_engine.md) — Creating variables and expressions
- [Calculus](calculus.md) — Differentiation and integration
- [API Reference: Algebra](api_reference/algebra.md)
