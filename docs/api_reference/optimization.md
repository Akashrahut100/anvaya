# API Reference: Optimization

## Module: `anvaya.optimization`

---

## Functions

### `minimize`

```python
minimize(func: callable, x0: ndarray, method: str = 'BFGS', constraints: tuple = ()) -> OptimizeResult
```

Finds the minimum of a scalar function.

| Parameter | Type | Description |
|-----------|------|-------------|
| `func` | `callable` | Objective function |
| `x0` | `ndarray` | Initial guess |
| `method` | `str` | Solver algorithm |
| `constraints` | `tuple` | Dictionary of constraints |

---

### `linear_program`

```python
linear_program(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None) -> OptimizeResult
```

Solves linear programming problems (simplex/interior-point).

---

### `gradient_descent`

```python
gradient_descent(func, grad, x0, learning_rate=0.01, max_iter=1000) -> ndarray
```

A manual implementation of the gradient descent algorithm.
