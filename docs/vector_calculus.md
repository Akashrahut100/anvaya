# Vector Calculus Module

The `vector_calculus` module provides gradient, divergence, curl, and line integrals.

---

## Import

```python
from anvaya import vector_calculus as vc
from anvaya.symbolic import var
```

---

## Functions

### `gradient(scalar_field, variables)`
Computes the gradient of a scalar field.

```python
x, y, z = var('x y z')
f = x**2 + y**2 + z**2

grad = vc.gradient(f, [x, y, z])
print(grad)  # [2*x, 2*y, 2*z]
```

---

### `divergence(vector_field, variables)`
Computes divergence of a vector field.

```python
x, y, z = var('x y z')
F = [x**2, y**2, z**2]

div = vc.divergence(F, [x, y, z])
print(div)  # 2*x + 2*y + 2*z
```

---

### `curl(vector_field, variables)`
Computes curl of a 3D vector field.

```python
x, y, z = var('x y z')
F = [-y, x, 0]

curl_F = vc.curl(F, [x, y, z])
print(curl_F)  # [0, 0, 2]
```

**Raises:** `ValueError` if not 3D.

---

### `line_integral(vector_field, curve_param, limits)`
Framework for line integrals (requires parameterization).

**Note:** Currently raises `NotImplementedError`. Use symbolic integration with substitutions.

---

## Examples

### Verify Vector Identity

```python
x, y, z = var('x y z')

# ∇ × (∇f) = 0 (curl of gradient is zero)
f = x*y*z
grad_f = vc.gradient(f, [x, y, z])
curl_grad = vc.curl(grad_f, [x, y, z])
print(curl_grad)  # [0, 0, 0]
```

---

## See Also

- [Calculus](calculus.md)
- [Linear Algebra](linear_algebra.md)
