# API Reference: Algebra

## Module: `anvaya.algebra`

---

## Functions

### `solve_linear`

```python
solve_linear(equations: list, variables: list) -> dict
```

Solves a system of linear equations.

| Parameter | Type | Description |
|-----------|------|-------------|
| `equations` | `list` | Equations (expressions = 0) |
| `variables` | `list` | Variables to solve for |

**Returns:** `dict` — Variable → solution mapping

---

### `solve_quadratic`

```python
solve_quadratic(equation: Expr, variable: Symbol) -> list
```

Solves a quadratic equation.

| Parameter | Type | Description |
|-----------|------|-------------|
| `equation` | `Expr` | Quadratic expression |
| `variable` | `Symbol` | Variable to solve for |

**Returns:** `list` — Solutions (may be complex)

---

### `expand_poly`

```python
expand_poly(expression: Expr) -> Expr
```

Expands a polynomial expression.

---

### `factor_poly`

```python
factor_poly(expression: Expr) -> Expr
```

Factors a polynomial expression.

---

### `rational_simplify`

```python
rational_simplify(expression: Expr) -> Expr
```

Simplifies rational expressions by canceling.

---

### `partial_fraction`

```python
partial_fraction(expression: Expr, variable: Symbol) -> Expr
```

Partial fraction decomposition.

---

### `solve_system`

```python
solve_system(equations: list, variables: list) -> dict | list
```

Solves systems of equations (linear or non-linear).
