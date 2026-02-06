# Installation

This guide will help you install Anvaya and its dependencies.

---

## 📋 Requirements

Before installing Anvaya, ensure you have:

- **Python 3.8** or higher
- **pip** (Python package manager)

---

## 🚀 Installation Methods

### Method 1: Install from PyPI (Recommended)

```bash
pip install anvaya
```

### Method 2: Install from Source

```bash
# Clone the repository
git clone https://github.com/yourusername/anvaya.git
cd anvaya

# Install in development mode
pip install -e .
```

### Method 3: Install with Optional Dependencies

```bash
# Install with all optional dependencies
pip install anvaya[all]

# Install with visualization support
pip install anvaya[viz]

# Install with Jupyter notebook support
pip install anvaya[jupyter]
```

---

## 📦 Dependencies

Anvaya automatically installs the following core dependencies:

| Package | Version | Purpose |
|---------|---------|---------|
| `numpy` | ≥1.20.0 | Numerical array operations |
| `scipy` | ≥1.7.0 | Scientific computing |
| `sympy` | ≥1.10.0 | Symbolic mathematics |
| `networkx` | ≥2.6.0 | Graph algorithms |

### Optional Dependencies

| Package | Purpose |
|---------|---------|
| `matplotlib` | Visualization and plotting |
| `jupyter` | Interactive notebooks |
| `pytest` | Running tests |

---

## ✅ Verify Installation

After installation, verify everything is working:

```python
# Check version
import anvaya
print(anvaya.__version__)

# Quick test
from anvaya.symbolic import var
from anvaya import algebra

x = var('x')
result = algebra.solve_quadratic(x**2 - 4, x)
print(result)  # [-2, 2]
```

You can also run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run with verbose output
python -m pytest tests/ -v
```

---

## 🐛 Troubleshooting

### Common Issues

#### 1. SymPy Import Errors

If you see deprecation warnings about `sympy.ntheory.totient`:

```
DeprecationWarning: sympy.ntheory.totient is deprecated
```

**Solution:** Update SymPy to version 1.13 or higher:

```bash
pip install --upgrade sympy
```

#### 2. NumPy Compatibility

If you encounter NumPy-related errors:

```bash
pip install --upgrade numpy
```

#### 3. Missing `py.typed` File

If your IDE doesn't recognize type hints:

The `py.typed` marker file should be included in the package. If missing, create it:

```bash
touch anvaya/py.typed
```

---

## 🔄 Upgrading

To upgrade to the latest version:

```bash
pip install --upgrade anvaya
```

---

## 🗑️ Uninstalling

To remove Anvaya:

```bash
pip uninstall anvaya
```

---

## 📝 Next Steps

- [Quickstart Guide](quickstart.md) — Learn the basics
- [API Reference](api_reference/index.md) — Explore all functions
