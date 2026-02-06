# Linear Algebra Module

The `linear_algebra` module provides matrix and vector operations using NumPy.

---

## Import

```python
from anvaya import linear_algebra as la
```

---

## Functions

### `matrix(data)`
Creates a matrix from nested lists or array-like data.

```python
A = la.matrix([[1, 2], [3, 4]])
```

---

### `multiply(A, B)`
Matrix multiplication (A @ B).

```python
C = la.multiply(A, B)
```

**Raises:** `DimensionMismatchError` if dimensions incompatible.

---

### `determinant(A, *, check_numerical=True)`
Calculates determinant of a square matrix.

```python
det = la.determinant([[1, 2], [3, 4]])  # -2.0
```

---

### `inverse(A, *, check_singular=True)`
Calculates the inverse of a matrix.

```python
A_inv = la.inverse([[1, 2], [3, 4]])
```

**Raises:** `SingularMatrixError` if matrix is singular.

---

### `rank(A)`
Calculates matrix rank.

```python
r = la.rank([[1, 2], [2, 4]])  # 1
```

---

### `eigenvalues(A)`
Computes eigenvalues and eigenvectors.

```python
result = la.eigenvalues([[4, 2], [1, 3]])
print(result.values)   # Eigenvalues
print(result.vectors)  # Eigenvectors
```

---

### `dot_product(v1, v2)`
Vector dot product.

```python
la.dot_product([1, 2, 3], [4, 5, 6])  # 32
```

---

### `cross_product(v1, v2)`
3D vector cross product.

```python
la.cross_product([1, 0, 0], [0, 1, 0])  # [0, 0, 1]
```

---

### `solve_linear_system(A, b)`
Solves Ax = b.

```python
x = la.solve_linear_system([[2, 1], [1, 3]], [1, 2])
```

---

### `norm(v, ord=2)`
Computes vector/matrix norm.

```python
la.norm([3, 4])  # 5.0 (Euclidean)
```

---

### `trace(A)`
Sum of diagonal elements.

```python
la.trace([[1, 2], [3, 4]])  # 5
```

---

## See Also

- [Vector Calculus](vector_calculus.md)
- [Errors](errors.md)
