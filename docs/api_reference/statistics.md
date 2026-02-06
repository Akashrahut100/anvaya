# API Reference: Statistics

## Module: `anvaya.statistics`

---

## Functions

### Central Tendency

| Function | Description |
|----------|-------------|
| `mean(data)` | Arithmetic average |
| `median(data)` | Middle value |
| `mode(data)` | Most frequent value |

### Dispersion

| Function | Description |
|----------|-------------|
| `variance(data)` | Variance |
| `stdev(data)` | Standard deviation |
| `percentile(data, q)` | q-th percentile |

### Relationships

| Function | Description |
|----------|-------------|
| `correlation(x, y)` | Pearson correlation coefficient |
| `linear_regression(x, y)` | Linear least-squares regression |

---

### `describe`

```python
describe(data: list) -> DescribeResult
```

Returns summary statistics (count, min, max, mean, variance, skewness, kurtosis).
