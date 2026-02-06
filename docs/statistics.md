# Statistics Module

The `statistics` module provides descriptive statistics and regression analysis.

---

## Import

```python
from anvaya import statistics as stats
```

---

## Functions

### `mean(data)`
Computes arithmetic mean.

```python
stats.mean([1, 2, 3, 4, 5])  # 3.0
```

---

### `median(data)`
Computes median value.

```python
stats.median([1, 2, 3, 4, 5])  # 3.0
```

---

### `mode(data)`
Finds most frequent value.

```python
stats.mode([1, 2, 2, 3])  # 2
```

---

### `variance(data)`
Computes variance.

```python
stats.variance([1, 2, 3, 4, 5])  # 2.0
```

---

### `stdev(data)`
Computes standard deviation.

```python
stats.stdev([1, 2, 3, 4, 5])  # 1.414...
```

---

### `percentile(data, q)`
Computes q-th percentile.

```python
stats.percentile([1, 2, 3, 4, 5], 75)  # 4.0
```

---

### `correlation(x, y)`
Computes Pearson correlation coefficient.

```python
stats.correlation([1, 2, 3], [1, 2, 3])  # 1.0
```

---

### `linear_regression(x, y)`
Returns slope, intercept, r_value, p_value, std_err.

```python
result = stats.linear_regression([1, 2, 3], [2, 4, 6])
print(result.slope)      # 2.0
print(result.intercept)  # 0.0
print(result.rvalue)     # 1.0
```

---

### `describe(data)`
Returns detailed descriptive statistics.

```python
stats.describe([1, 2, 3, 4, 5])
# nobs, minmax, mean, variance, skewness, kurtosis
```

---

## See Also

- [Probability](probability.md)
