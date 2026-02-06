# Anvaya Mathematics Library

<p align="center">
  <strong>A comprehensive Python mathematics library for symbolic and numerical computation</strong>
</p>

<p align="center">
  <em>Sanskrit: अन्वय (anvaya) — "connection, logical sequence"</em>
</p>

---

## 🎯 What is Anvaya?

**Anvaya** is a unified mathematics library that brings together symbolic computation, numerical methods, linear algebra, probability, statistics, and more — all in one cohesive package. Built on top of industry-standard libraries like SymPy, NumPy, SciPy, and NetworkX, Anvaya provides a clean, Pythonic API for mathematical operations.

---

## ✨ Key Features

| Module | Description |
|--------|-------------|
| **Algebra** | Equation solving, polynomial manipulation, partial fractions |
| **Calculus** | Limits, derivatives, integrals, Taylor series |
| **Linear Algebra** | Matrix operations, eigenvalues, linear systems |
| **Number Theory** | Primes, GCD/LCM, modular arithmetic, CRT |
| **Probability** | Normal, Binomial, Poisson distributions, Bayes' theorem |
| **Statistics** | Mean, variance, regression, correlation |
| **Optimization** | Minimization, linear programming, gradient descent |
| **Graph Theory** | Shortest path, MST, BFS/DFS |
| **Differential Equations** | ODEs, PDEs, initial value problems |
| **Complex Analysis** | Residues, complex expansion |
| **Vector Calculus** | Gradient, divergence, curl |
| **Numerical Methods** | Root finding, numerical integration, interpolation |
| **Discrete Mathematics** | Set theory, boolean logic, satisfiability |
| **Symbolic Engine** | Core symbolic computation utilities |

---

## 🚀 Quick Example

```python
from anvaya import algebra, calculus, linear_algebra
from anvaya.symbolic import var

# Symbolic algebra
x = var('x')
solutions = algebra.solve_quadratic(x**2 - 5*x + 6, x)
print(solutions)  # [2, 3]

# Calculus
derivative = calculus.diff(x**3 + 2*x, x)
print(derivative)  # 3*x**2 + 2

# Linear algebra
A = linear_algebra.matrix([[1, 2], [3, 4]])
det = linear_algebra.determinant(A)
print(det)  # -2.0
```

---

## 📚 Documentation

- [Installation](installation.md) — Get started with Anvaya
- [Quickstart Guide](quickstart.md) — Learn the basics in 5 minutes
- [API Reference](api_reference/index.md) — Complete function documentation

### Module Guides

| Module | Guide |
|--------|-------|
| Algebra | [algebra.md](algebra.md) |
| Calculus | [calculus.md](calculus.md) |
| Linear Algebra | [linear_algebra.md](linear_algebra.md) |
| Probability | [probability.md](probability.md) |
| Statistics | [statistics.md](statistics.md) |
| Number Theory | [number_theory.md](number_theory.md) |
| Numerical Methods | [numerical.md](numerical.md) |
| Optimization | [optimization.md](optimization.md) |
| Graph Theory | [graph_theory.md](graph_theory.md) |
| Differential Equations | [differential_equations.md](differential_equations.md) |
| Complex Analysis | [complex_analysis.md](complex_analysis.md) |
| Vector Calculus | [vector_calculus.md](vector_calculus.md) |
| Discrete Mathematics | [discrete.md](discrete.md) |
| Symbolic Engine | [symbolic_engine.md](symbolic_engine.md) |
| Error Handling | [errors.md](errors.md) |

---

## 🔧 Requirements

- Python 3.8+
- NumPy
- SciPy
- SymPy
- NetworkX

---

## 📄 License

MIT License — See [LICENSE](../LICENSE) for details.

---

## 🤝 Contributing

Contributions are welcome! Please read the contributing guidelines before submitting a pull request.

---

<p align="center">
  Made with ❤️ for the mathematics community
</p>
