# Discrete Mathematics Module

The `discrete` module provides set theory and boolean logic operations.

---

## Import

```python
from anvaya import discrete
```

---

## Classes

### `Set`
Wrapper for SymPy FiniteSet operations.

```python
A = discrete.Set.new(1, 2, 3)
B = discrete.Set.new(2, 3, 4)

# Union
discrete.Set.union(A, B)  # {1, 2, 3, 4}

# Intersection
discrete.Set.intersection(A, B)  # {2, 3}

# Difference
discrete.Set.difference(A, B)  # {1}
```

---

## Functions

### `truth_table(expression, variables)`
Generates a truth table for a boolean expression.

```python
from sympy import symbols
from sympy.logic.boolalg import And, Or, Not

A, B = symbols('A B')
expr = And(A, Or(B, Not(A)))

table = discrete.truth_table(expr, [A, B])
for row in table:
    print(row)
```

---

### `simplify_logic(expr)`
Simplifies a logical expression.

```python
from sympy import symbols
from sympy.logic.boolalg import Or, And, Not

A, B = symbols('A B')
expr = Or(And(A, B), And(A, Not(B)))
simplified = discrete.simplify_logic(expr)
print(simplified)  # A
```

---

### `satisfiable(expr)`
Checks if a boolean expression is satisfiable.

```python
from sympy import symbols
from sympy.logic.boolalg import And, Not

A, B = symbols('A B')

# Satisfiable
expr1 = And(A, B)
print(discrete.satisfiable(expr1))  # {A: True, B: True}

# Unsatisfiable
expr2 = And(A, Not(A))
print(discrete.satisfiable(expr2))  # False
```

---

## See Also

- [Graph Theory](graph_theory.md)
- [Algebra](algebra.md)
