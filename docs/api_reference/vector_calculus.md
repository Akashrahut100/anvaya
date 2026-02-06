# API Reference: Vector Calculus

## Module: `anvaya.vector_calculus`

---

## Functions

### `gradient`

```python
gradient(scalar_field: Expr, variables: list) -> list
```

Computes the gradient vector of a scalar field.

---

### `divergence`

```python
divergence(vector_field: list, variables: list) -> Expr
```

Computes the divergence of a vector field.

---

### `curl`

```python
curl(vector_field: list, variables: list) -> list
```

Computes the curl of a 3D vector field.
*Requires exactly 3 components and 3 variables.*

---

### `line_integral`

```python
line_integral(...)
```

*Note: Currently under development. Use symbolic integration with manual parameterization.*
