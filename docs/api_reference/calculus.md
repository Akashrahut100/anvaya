# API Reference: Calculus

## Module: `anvaya.calculus`

---

## Functions

### `limit`

```python
limit(expr: Expr, variable: Symbol, point, direction: str = '+') -> Expr
```

Computes limit of expression as variable approaches point.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `expr` | `Expr` | — | Expression |
| `variable` | `Symbol` | — | Variable |
| `point` | `number` | — | Point (use `sp.oo` for ∞) |
| `direction` | `str` | `'+'` | `'+'`, `'-'`, or `'+-'` |

**Returns:** Limit value

---

### `diff`

```python
diff(expr: Expr, variable: Symbol, order: int = 1) -> Expr
```

Computes derivative of any order.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `expr` | `Expr` | — | Expression |
| `variable` | `Symbol` | — | Differentiation variable |
| `order` | `int` | `1` | Derivative order |

**Returns:** `Expr` — Derivative

---

### `integrate`

```python
integrate(expr: Expr, variable: Symbol, lower=None, upper=None) -> Expr
```

Computes indefinite or definite integral.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `expr` | `Expr` | — | Expression |
| `variable` | `Symbol` | — | Integration variable |
| `lower` | `number` | `None` | Lower bound |
| `upper` | `number` | `None` | Upper bound |

**Returns:** `Expr` — Integral

---

### `taylor_series`

```python
taylor_series(expr: Expr, variable: Symbol, point, n: int) -> Expr
```

Taylor series expansion around a point.

| Parameter | Type | Description |
|-----------|------|-------------|
| `expr` | `Expr` | Expression |
| `variable` | `Symbol` | Variable |
| `point` | `number` | Center point |
| `n` | `int` | Number of terms |

**Returns:** `Expr` — Taylor polynomial

---

### `maclaurin_series`

```python
maclaurin_series(expr: Expr, variable: Symbol, n: int) -> Expr
```

Maclaurin series (Taylor at 0).

| Parameter | Type | Description |
|-----------|------|-------------|
| `expr` | `Expr` | Expression |
| `variable` | `Symbol` | Variable |
| `n` | `int` | Number of terms |

**Returns:** `Expr` — Maclaurin polynomial
