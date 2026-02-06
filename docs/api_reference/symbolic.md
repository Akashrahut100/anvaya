# API Reference: Symbolic Engine

## Module: `anvaya.symbolic`

---

## Functions

### `var`

```python
var(names: str) -> symbols
```

Efficiently creates multiple symbolic variables.
Example: `x, y = var('x y')`

---

### `simplify`

```python
simplify(expr: Expr) -> Expr
```

Simplifies a mathematical expression algebraically.

---

### `diff`

```python
diff(expr: Expr, variable: Symbol, n: int = 1) -> Expr
```

Computes the $n$-th derivative of an expression.

---

### `integrate`

```python
integrate(expr: Expr, variable: Symbol, limits: tuple = None) -> Expr
```

Computes indefinite or definite integrals.
- For definite: `limits=(x, 0, 1)`

---

### `limit`

```python
limit(expr: Expr, variable: Symbol, point: Any, direction: str = '+') -> Expr
```

Computes the limit as a variable approaches a point.
