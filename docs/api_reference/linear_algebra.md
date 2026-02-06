# API Reference: Linear Algebra

## Module: `anvaya.linear_algebra`

---

## Type Aliases

```python
Matrix = NDArray[np.floating]
Vector = NDArray[np.floating]
```

---

## Functions

### `matrix`
```python
matrix(data: ArrayLike) -> np.ndarray
```
Creates 2D matrix from nested lists.

---

### `multiply`
```python
multiply(A: ArrayLike, B: ArrayLike) -> np.ndarray
```
Matrix multiplication A @ B.

**Raises:** `DimensionMismatchError`

---

### `determinant`
```python
determinant(A: ArrayLike, *, check_numerical: bool = True) -> float
```
Computes determinant of square matrix.

**Raises:** `DimensionMismatchError`

---

### `inverse`
```python
inverse(A: ArrayLike, *, check_singular: bool = True) -> np.ndarray
```
Computes matrix inverse.

**Raises:** `SingularMatrixError`, `DimensionMismatchError`

---

### `rank`
```python
rank(A: ArrayLike) -> int
```
Computes matrix rank.

---

### `eigenvalues`
```python
eigenvalues(A: ArrayLike) -> EigenResult
```
Computes eigenvalues and eigenvectors.

**Returns:** `EigenResult(values, vectors)`

---

### `dot_product`
```python
dot_product(v1: ArrayLike, v2: ArrayLike) -> float
```
Vector dot product.

---

### `cross_product`
```python
cross_product(v1: ArrayLike, v2: ArrayLike) -> np.ndarray
```
3D vector cross product.

**Raises:** `DimensionMismatchError`

---

### `solve_linear_system`
```python
solve_linear_system(A: ArrayLike, b: ArrayLike) -> np.ndarray
```
Solves Ax = b.

**Raises:** `SingularMatrixError`

---

### `norm`
```python
norm(v: ArrayLike, ord: Union[int, float, str] = 2) -> float
```
Computes vector/matrix norm.

---

### `trace`
```python
trace(A: ArrayLike) -> float
```
Sum of diagonal elements.

---

## Classes

### `EigenResult`
Named tuple with `values` and `vectors` attributes.
