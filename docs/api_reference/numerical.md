# API Reference: Numerical Methods

## Module: `anvaya.numerical`

---

## Functions

### `root_find`

```python
root_find(func: callable, x0: float, method: str = 'newton') -> float
```

Finds the root of a numerical function.

| Parameter | Type | Description |
|-----------|------|-------------|
| `func` | `callable` | Python function to evaluate |
| `x0` | `float` | Initial guess |
| `method` | `str` | Algorithm: 'newton', 'bisect', etc. |

**Returns:** `float` — The root value.

---

### `numeric_integrate`

```python
numeric_integrate(func: callable, a: float, b: float) -> float
```

Computes the definite integral of a function from $a$ to $b$ numerically (Quadrature).

---

### `interp1d`

```python
interp1d(x: list, y: list, kind: str = 'linear') -> callable
```

Returns a 1D interpolation function based on data points.
