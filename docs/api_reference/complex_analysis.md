# API Reference: Complex Analysis

## Module: `anvaya.complex_analysis`

---

## Functions

### `residue`

```python
residue(expr: Expr, variable: Symbol, point: complex) -> Expr
```

Computes the residue of an expression at a given point.

| Parameter | Type | Description |
|-----------|------|-------------|
| `expr` | `Expr` | Complex expression |
| `variable` | `Symbol` | Variable to evaluate with respect to |
| `point` | `complex` | The point at which to find the residue |

**Returns:** `Expr` — The residue at the point.

---

### `complex_expand`

```python
complex_expand(expr: Expr) -> Expr
```

Expands a complex expression into its real and imaginary parts ($a + bi$).

| Parameter | Type | Description |
|-----------|------|-------------|
| `expr` | `Expr` | Expression to expand |

**Returns:** `Expr` — Expanded expression.

---

### `complex_integrate`

```python
complex_integrate(expr: Expr, variable: Symbol, path: tuple) -> Expr
```

Computes a basic complex integral (parameterized).

| Parameter | Type | Description |
|-----------|------|-------------|
| `expr` | `Expr` | Expression to integrate |
| `variable` | `Symbol` | Integration variable |
| `path` | `tuple` | Tuple representing start and end points |
