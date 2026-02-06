# API Reference: Probability

## Module: `anvaya.probability`

---

## Classes

### `Normal(mean=0, std=1)`
Represents a Normal (Gaussian) distribution.
- `pdf(x)`: Probability Density Function.
- `cdf(x)`: Cumulative Distribution Function.
- `ppf(q)`: Inverse CDF (Quantile).
- `sample(size)`: Generate random samples.

### `Binomial(n, p)`
Represents a Binomial distribution.
- `pmf(k)`: Probability Mass Function.
- `cdf(k)`: Cumulative Distribution Function.

### `Poisson(mu)`
Represents a Poisson distribution.
- `pmf(k)`: Probability Mass Function.

---

## Functions

### `bayes_theorem`

```python
bayes_theorem(p_b_given_a: float, p_a: float, p_b: float) -> float
```

Computes $P(A|B)$ using Bayes' Theorem.

---

### `expected_value`

```python
expected_value(values: list, probabilities: list) -> float
```

Computes the expected value $E[X]$ of a discrete random variable.

---

### `variance_discrete`

```python
variance_discrete(values: list, probabilities: list) -> float
```

Computes the variance $Var(X)$ of a discrete random variable.
