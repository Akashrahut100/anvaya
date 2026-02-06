# Complex Analysis Module

The `complex_analysis` module provides tools for complex number computations.

---

## Import

```python
from anvaya import complex_analysis as ca
from anvaya.symbolic import var
```

---

## Functions

### `residue(expr, variable, point)`
Computes the residue of an expression at a pole.

```python
z = var('z')
expr = 1/(z**2 + 1)
res = ca.residue(expr, z, 1j)  # Residue at z = i
```

---

### `complex_expand(expr)`
Expands into real and imaginary parts.

```python
z = var('z')
import sympy as sp

expr = sp.exp(1j * z)
expanded = ca.complex_expand(expr)
# cos(z) + I*sin(z)
```

---

### `complex_integrate(expr, variable, path)`
Basic contour integration (path as [start, end]).

```python
z = var('z')
result = ca.complex_integrate(z**2, z, [0, 1+1j])
```

**Note:** Full contour integration requires path parameterization.

---

## See Also

- [Calculus](calculus.md)
- [Symbolic Engine](symbolic_engine.md)
