# Calculus Module

The `calculus` module provides symbolic tools for limits, differentiation, integration, and series expansion.

---

## Overview

This module wraps SymPy's calculus capabilities, providing a clean interface for:

- Computing limits (including directional limits)
- Symbolic differentiation (any order)
- Indefinite and definite integration
- Taylor and Maclaurin series expansions

---

## Import

```python
from anvaya import calculus
from anvaya.symbolic import var
import sympy as sp  # For special constants like oo (infinity)
```

---

## Functions

### `limit(expr, variable, point, direction='+')`

Computes the limit of an expression as a variable approaches a point.

**Parameters**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `expr` | `Expr` | — | Mathematical expression |
| `variable` | `Symbol` | — | Variable approaching the limit |
| `point` | `number` | — | Point being approached (can use `sp.oo` for infinity) |
| `direction` | `str` | `'+'` | Direction: `'+'` (right), `'-'` (left), or `'+-'` (both) |

**Returns**

- Limit value or symbolic expression

**Example**

```python
from anvaya import calculus
from anvaya.symbolic import var
import sympy as sp

x = var('x')

# Basic limit
result = calculus.limit(sp.sin(x)/x, x, 0)
print(result)  # 1

# Limit at infinity
result = calculus.limit(1/x, x, sp.oo)
print(result)  # 0

# One-sided limits
result = calculus.limit(1/x, x, 0, direction='+')
print(result)  # oo

result = calculus.limit(1/x, x, 0, direction='-')
print(result)  # -oo

# Indeterminate forms (L'Hôpital's Rule applied automatically)
result = calculus.limit((sp.exp(x) - 1)/x, x, 0)
print(result)  # 1
```

---

### `diff(expr, variable, order=1)`

Computes the derivative of an expression.

**Parameters**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `expr` | `Expr` | — | Expression to differentiate |
| `variable` | `Symbol` | — | Variable to differentiate with respect to |
| `order` | `int` | `1` | Order of differentiation |

**Returns**

- `Expr` — The derivative

**Example**

```python
from anvaya import calculus
from anvaya.symbolic import var
import sympy as sp

x = var('x')

# First derivative
result = calculus.diff(x**3, x)
print(result)  # 3*x**2

# Second derivative
result = calculus.diff(x**4, x, order=2)
print(result)  # 12*x**2

# Transcendental functions
result = calculus.diff(sp.sin(x), x)
print(result)  # cos(x)

result = calculus.diff(sp.exp(x), x)
print(result)  # exp(x)

result = calculus.diff(sp.ln(x), x)
print(result)  # 1/x

# Chain rule (automatic)
result = calculus.diff(sp.sin(x**2), x)
print(result)  # 2*x*cos(x**2)

# Product rule (automatic)
result = calculus.diff(x * sp.exp(x), x)
print(result)  # exp(x) + x*exp(x)
```

---

### `integrate(expr, variable, lower=None, upper=None)`

Computes the integral of an expression.

**Parameters**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `expr` | `Expr` | — | Expression to integrate |
| `variable` | `Symbol` | — | Variable of integration |
| `lower` | `number` | `None` | Lower bound for definite integral |
| `upper` | `number` | `None` | Upper bound for definite integral |

**Returns**

- `Expr` — The integral (+ C for indefinite, value for definite)

**Example**

```python
from anvaya import calculus
from anvaya.symbolic import var
import sympy as sp

x = var('x')

# Indefinite integrals
result = calculus.integrate(x**2, x)
print(result)  # x**3/3

result = calculus.integrate(sp.cos(x), x)
print(result)  # sin(x)

result = calculus.integrate(1/x, x)
print(result)  # log(x)

# Definite integrals
result = calculus.integrate(x**2, x, lower=0, upper=1)
print(result)  # 1/3

result = calculus.integrate(sp.sin(x), x, lower=0, upper=sp.pi)
print(result)  # 2

# Improper integrals
result = calculus.integrate(sp.exp(-x), x, lower=0, upper=sp.oo)
print(result)  # 1

# Integration by parts (automatic)
result = calculus.integrate(x * sp.exp(x), x)
print(result)  # (x - 1)*exp(x)
```

---

### `taylor_series(expr, variable, point, n)`

Expands an expression into a Taylor series around a point.

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `expr` | `Expr` | Expression to expand |
| `variable` | `Symbol` | Variable for expansion |
| `point` | `number` | Center point of expansion |
| `n` | `int` | Number of terms |

**Returns**

- `Expr` — Taylor polynomial (Big-O term removed)

**Example**

```python
from anvaya import calculus
from anvaya.symbolic import var
import sympy as sp

x = var('x')

# Exponential function at x=0
result = calculus.taylor_series(sp.exp(x), x, 0, 5)
print(result)  # 1 + x + x**2/2 + x**3/6 + x**4/24

# Sine function at x=0
result = calculus.taylor_series(sp.sin(x), x, 0, 6)
print(result)  # x - x**3/6 + x**5/120

# Cosine function at x=0
result = calculus.taylor_series(sp.cos(x), x, 0, 6)
print(result)  # 1 - x**2/2 + x**4/24

# Taylor series around x=1
result = calculus.taylor_series(sp.ln(x), x, 1, 4)
print(result)  # (x-1) - (x-1)**2/2 + (x-1)**3/3

# Using for approximation
f = calculus.taylor_series(sp.exp(x), x, 0, 10)
approx_e = f.subs(x, 1)
print(float(approx_e))  # ≈ 2.7182818...
```

---

### `maclaurin_series(expr, variable, n)`

Expands an expression into a Maclaurin series (Taylor series centered at 0).

**Parameters**

| Name | Type | Description |
|------|------|-------------|
| `expr` | `Expr` | Expression to expand |
| `variable` | `Symbol` | Variable for expansion |
| `n` | `int` | Number of terms |

**Returns**

- `Expr` — Maclaurin polynomial

**Example**

```python
from anvaya import calculus
from anvaya.symbolic import var
import sympy as sp

x = var('x')

# Common Maclaurin series
result = calculus.maclaurin_series(1/(1-x), x, 5)
print(result)  # 1 + x + x**2 + x**3 + x**4

result = calculus.maclaurin_series(sp.sqrt(1+x), x, 4)
print(result)  # 1 + x/2 - x**2/8 + x**3/16

result = calculus.maclaurin_series(sp.atan(x), x, 6)
print(result)  # x - x**3/3 + x**5/5
```

---

## Common Use Cases

### Finding Critical Points

```python
from anvaya import calculus
from anvaya.symbolic import var, engine

x = var('x')
f = x**3 - 3*x**2 + 2

# First derivative
f_prime = calculus.diff(f, x)
print(f"f'(x) = {f_prime}")  # 3*x**2 - 6*x

# Find critical points (where f'(x) = 0)
critical_points = engine.solve(f_prime, x)
print(f"Critical points: {critical_points}")  # [0, 2]

# Second derivative test
f_double_prime = calculus.diff(f, x, order=2)
for point in critical_points:
    value = f_double_prime.subs(x, point)
    if value > 0:
        print(f"x={point}: Local minimum")
    elif value < 0:
        print(f"x={point}: Local maximum")
```

### Area Between Curves

```python
from anvaya import calculus
from anvaya.symbolic import var

x = var('x')

# Area between y = x² and y = x from x=0 to x=1
f = x
g = x**2
area = calculus.integrate(f - g, x, lower=0, upper=1)
print(f"Area = {area}")  # 1/6
```

### Verifying Fundamental Theorem of Calculus

```python
from anvaya import calculus
from anvaya.symbolic import var

x = var('x')

# The derivative of an integral gives back the original function
f = x**3
F = calculus.integrate(f, x)  # Antiderivative
f_recovered = calculus.diff(F, x)
print(f"Original: {f}")
print(f"Recovered: {f_recovered}")  # Should be same
```

---

## Mathematical Background

### Common Derivatives

| Function | Derivative |
|----------|------------|
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln(x)$ | $1/x$ |
| $\sin(x)$ | $\cos(x)$ |
| $\cos(x)$ | $-\sin(x)$ |
| $\tan(x)$ | $\sec^2(x)$ |

### Common Integrals

| Function | Integral |
|----------|----------|
| $x^n$ | $\frac{x^{n+1}}{n+1}$ |
| $e^x$ | $e^x$ |
| $1/x$ | $\ln|x|$ |
| $\sin(x)$ | $-\cos(x)$ |
| $\cos(x)$ | $\sin(x)$ |

---

## See Also

- [Symbolic Engine](symbolic_engine.md) — Creating variables and expressions
- [Vector Calculus](vector_calculus.md) — Gradient, divergence, curl
- [Differential Equations](differential_equations.md) — Solving ODEs and PDEs
- [API Reference: Calculus](api_reference/calculus.md)
