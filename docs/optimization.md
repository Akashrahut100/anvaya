# Optimization Module

The `optimization` module provides function minimization and linear programming.

---

## Import

```python
from anvaya import optimization as opt
```

---

## Functions

### `minimize(func, x0, method='BFGS', constraints=())`
Minimizes a function.

```python
def f(x):
    return x[0]**2 + x[1]**2

result = opt.minimize(f, x0=[1, 1])
print(result.x)    # [0, 0]
print(result.fun)  # 0.0
```

---

### `linear_program(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None)`
Solves linear programming: minimize c @ x subject to constraints.

```python
# Minimize: -x - 2y
# Subject to: x + y ≤ 4, x ≤ 2, y ≤ 3
c = [-1, -2]
A_ub = [[1, 1], [1, 0], [0, 1]]
b_ub = [4, 2, 3]

result = opt.linear_program(c, A_ub=A_ub, b_ub=b_ub)
print(result.x)  # Optimal solution
```

---

### `gradient_descent(func, grad, x0, learning_rate=0.01, max_iter=1000, tol=1e-6)`
Custom gradient descent implementation.

```python
def f(x):
    return x[0]**2 + x[1]**2

def grad(x):
    return [2*x[0], 2*x[1]]

x_opt = opt.gradient_descent(f, grad, x0=[5, 5])
print(x_opt)  # ≈ [0, 0]
```

---

## See Also

- [Linear Algebra](linear_algebra.md)
- [Numerical Methods](numerical.md)
