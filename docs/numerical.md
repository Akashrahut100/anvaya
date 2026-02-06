# Numerical Methods Module

The `numerical` module provides numerical computation methods using SciPy.

---

## Import

```python
from anvaya import numerical
```

---

## Functions

### `root_find(func, x0, method='newton')`
Finds a root of a function.

**Parameters**
- `func`: Function to find root of
- `x0`: Initial guess
- `method`: 'newton', 'bisect', etc.

```python
def f(x):
    return x**2 - 4

root = numerical.root_find(f, 1)  # 2.0
```

---

### `numeric_integrate(func, a, b)`
Computes definite integral numerically.

```python
import math

def f(x):
    return math.sin(x)

result = numerical.numeric_integrate(f, 0, math.pi)  # 2.0
```

---

### `interp1d(x, y, kind='linear')`
Returns an interpolation function.

```python
x = [0, 1, 2, 3]
y = [0, 1, 4, 9]

f = numerical.interp1d(x, y, kind='quadratic')
print(f(1.5))  # Interpolated value
```

---

## See Also

- [Optimization](optimization.md)
- [Calculus](calculus.md)
