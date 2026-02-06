# Probability Module

The `probability` module provides probability distributions and related computations.

---

## Import

```python
from anvaya import probability as prob
```

---

## Classes

### `Normal(mean=0.0, std=1.0)`
Normal (Gaussian) distribution.

```python
dist = prob.Normal(mean=0, std=1)
dist.pdf(0)      # 0.3989...
dist.cdf(1.96)   # 0.975
dist.ppf(0.95)   # 1.645
dist.sample(5)   # 5 random samples
```

---

### `Binomial(n, p)`
Binomial distribution.

```python
dist = prob.Binomial(n=10, p=0.5)
dist.pmf(5)      # P(X = 5)
dist.cdf(5)      # P(X ≤ 5)
dist.sample(10)  # 10 random samples
```

---

### `Poisson(mu)`
Poisson distribution.

```python
dist = prob.Poisson(mu=3)
dist.pmf(2)      # P(X = 2)
dist.cdf(2)      # P(X ≤ 2)
dist.sample(5)   # 5 random samples
```

---

## Functions

### `bayes_theorem(p_b_given_a, p_a, p_b)`
Apply Bayes' theorem: P(A|B) = P(B|A) × P(A) / P(B)

```python
prob.bayes_theorem(0.99, 0.01, 0.05)  # 0.198
```

---

### `expected_value(values, probabilities)`
Compute E[X] = Σ xᵢ × P(xᵢ)

```python
prob.expected_value([1, 2, 3], [0.2, 0.5, 0.3])  # 2.1
```

---

### `variance_discrete(values, probabilities)`
Compute Var(X) = E[(X - μ)²]

```python
prob.variance_discrete([1, 2, 3], [0.2, 0.5, 0.3])
```

---

### `pdf(dist, x)` / `pmf(dist, k)` / `cdf(dist, x)`
Generic functions for any distribution.

```python
dist = prob.Normal(0, 1)
prob.pdf(dist, 0)  # 0.3989...
prob.cdf(dist, 0)  # 0.5
```

---

## See Also

- [Statistics](statistics.md)
