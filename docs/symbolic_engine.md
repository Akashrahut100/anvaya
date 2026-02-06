# Symbolic Engine Module

The `symbolic` module provides the core symbolic computation utilities.

---

## Import

```python
from anvaya.symbolic import var, engine, simplify, diff, integrate
```

---

## Quick Functions

### `var(names)`
Create symbolic variables.

```python
from anvaya.symbolic import var

# Single variable
x = var('x')

# Multiple variables
x, y, z = var('x y z')
```

---

### `simplify(expr)`
Simplifies expressions.

```python
from anvaya.symbolic import var, simplify

x = var('x')
expr = (x**2 - 1)/(x - 1)
simplify(expr)  # x + 1
```

---

### `diff(expr, var, n=1)`
Symbolic differentiation.

```python
from anvaya.symbolic import var, diff

x = var('x')
diff(x**3, x)  # 3*x**2
```

---

### `integrate(expr, var, limits=None)`
Symbolic integration.

```python
from anvaya.symbolic import var, integrate

x = var('x')
integrate(x**2, x)  # x**3/3
```

---

## SymbolicEngine Class

For more control, use the engine directly.

```python
from anvaya.symbolic import engine

# Create symbols
x = engine.symbol('x')
a, b = engine.symbols('a b')

# Parse string to expression
expr = engine.expr('x**2 + 2*x + 1')

# Operations
engine.simplify(expr)
engine.expand((x + 1)**2)
engine.factor(x**2 - 1)
engine.solve(x**2 - 4, x)  # [-2, 2]

# Calculus
engine.diff(x**3, x)
engine.integrate(x**2, x)
engine.limit(1/x, x, 0, direction='+')
```

---

## See Also

- [Algebra](algebra.md)
- [Calculus](calculus.md)
