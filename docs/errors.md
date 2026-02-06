# Error Handling

Anvaya provides custom exceptions for clear, informative error messages.

---

## Import

```python
from anvaya.core.exceptions import (
    SingularMatrixError,
    DimensionMismatchError,
    InvalidInputError
)
```

---

## Exceptions

### `SingularMatrixError`

Raised when a matrix operation fails because the matrix is singular (non-invertible).

**Common causes:**
- Determinant equals zero
- Matrix is rank deficient

```python
from anvaya import linear_algebra as la
from anvaya.core.exceptions import SingularMatrixError

try:
    A = la.matrix([[1, 2], [2, 4]])  # Singular (row 2 = 2 × row 1)
    la.inverse(A)
except SingularMatrixError as e:
    print(f"Cannot compute inverse: {e}")
```

---

### `DimensionMismatchError`

Raised when operation requires specific dimensions that don't match.

**Common causes:**
- Matrix multiplication with incompatible shapes
- Non-square matrix for square-only operations
- Vector operations with different lengths

```python
from anvaya import linear_algebra as la
from anvaya.core.exceptions import DimensionMismatchError

try:
    A = la.matrix([[1, 2, 3]])  # Shape: (1, 3)
    B = la.matrix([[1, 2]])     # Shape: (1, 2)
    la.multiply(A, B)
except DimensionMismatchError as e:
    print(f"Shape error: {e}")
```

---

### `InvalidInputError`

Raised when input values don't meet requirements.

**Common causes:**
- Probability not in [0, 1]
- Negative values where positive required
- Invalid parameter combinations

```python
from anvaya import probability as prob
from anvaya.core.exceptions import InvalidInputError

try:
    # Standard deviation must be positive
    dist = prob.Normal(mean=0, std=-1)
except InvalidInputError as e:
    print(f"Invalid input: {e}")

try:
    # Probability must be in [0, 1]
    prob.bayes_theorem(1.5, 0.5, 0.5)
except InvalidInputError as e:
    print(f"Invalid probability: {e}")
```

---

## Best Practices

### Always Handle Potential Errors

```python
from anvaya import linear_algebra as la
from anvaya.core.exceptions import SingularMatrixError, DimensionMismatchError

def safe_inverse(A):
    """Safely compute matrix inverse."""
    try:
        return la.inverse(A)
    except SingularMatrixError:
        return None
    except DimensionMismatchError as e:
        raise ValueError(f"Matrix must be square: {e}")
```

### Check Before Operations

```python
from anvaya import linear_algebra as la

A = la.matrix([[1, 2], [2, 4]])

# Check determinant before inverting
det = la.determinant(A)
if abs(det) < 1e-10:
    print("Matrix is singular or near-singular")
else:
    A_inv = la.inverse(A)
```

---

## See Also

- [Linear Algebra](linear_algebra.md)
- [Probability](probability.md)
