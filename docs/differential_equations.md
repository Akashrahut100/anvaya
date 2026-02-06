# Differential Equations Module

The `differential_equations` module provides solvers for ODEs and PDEs.

---

## Import

```python
from anvaya import differential_equations as de
from anvaya.symbolic import var
import sympy as sp
```

---

## Functions

### `solve_ode(equation, function)`
Solves an Ordinary Differential Equation.

```python
x = var('x')
f = sp.Function('f')

# f'(x) = f(x)
eq = sp.Eq(f(x).diff(x), f(x))
solution = de.solve_ode(eq, f(x))
print(solution)  # Eq(f(x), C1*exp(x))
```

---

### `solve_pde(equation, function)`
Solves a Partial Differential Equation.

```python
x, y = var('x y')
f = sp.Function('f')

# ∂f/∂x = 0
eq = sp.Eq(f(x, y).diff(x), 0)
solution = de.solve_pde(eq, f(x, y))
```

---

### `solve_ivp(equation, function, ics)`
Solves Initial Value Problems.

```python
x = var('x')
f = sp.Function('f')

# f'(x) = f(x), f(0) = 1
eq = sp.Eq(f(x).diff(x), f(x))
ics = {f(0): 1}

solution = de.solve_ivp(eq, f(x), ics)
print(solution)  # Eq(f(x), exp(x))
```

---

## Examples

### Second-Order ODE

```python
x = var('x')
f = sp.Function('f')

# f''(x) + f(x) = 0 (harmonic oscillator)
eq = sp.Eq(f(x).diff(x, 2) + f(x), 0)
solution = de.solve_ode(eq, f(x))
# Solution: C1*sin(x) + C2*cos(x)
```

---

## See Also

- [Calculus](calculus.md)
- [Symbolic Engine](symbolic_engine.md)
