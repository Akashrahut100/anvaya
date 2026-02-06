# API Reference: Discrete Mathematics

## Module: `anvaya.discrete`

---

## Classes

### `Set`

A wrapper class for set operations.

#### `new(*args)`
Creates a new finite set.

#### `union(s1, s2)`
Computes the union of two sets.

#### `intersection(s1, s2)`
Computes the intersection of two sets.

#### `difference(s1, s2)`
Computes the difference between two sets (`s1 - s2`).

---

## Functions

### `truth_table`

```python
truth_table(expression: Expr, variables: list) -> list
```

Generates a truth table for a boolean logic expression.

| Parameter | Type | Description |
|-----------|------|-------------|
| `expression` | `Expr` | Boolean expression |
| `variables` | `list` | List of boolean variables |

**Returns:** `list` — Rows of the truth table.

---

### `simplify_logic`

```python
simplify_logic(expr: Expr) -> Expr
```

Simplifies a logical expression to its simplest form.

---

### `satisfiable`

```python
satisfiable(expr: Expr) -> dict | bool
```

Checks if a logical expression is satisfiable (can be true).
