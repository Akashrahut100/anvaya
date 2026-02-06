# API Reference: Differential Equations

## Module: `anvaya.differential_equations`

---

## Functions

### `solve_ode`

```python
solve_ode(equation: Expr, function: AppliedUndef) -> Expr
```

Solves an Ordinary Differential Equation (ODE).

| Parameter | Type | Description |
|-----------|------|-------------|
| `equation` | `Expr` | Differential equation (expression = 0) |
| `function` | `AppliedUndef` | The function to solve for (e.g., `f(x)`) |

**Returns:** `Expr` — General solution of the ODE.

---

### `solve_pde`

```python
solve_pde(equation: Expr, function: AppliedUndef) -> Expr
```

Solves a Partial Differential Equation (PDE).

| Parameter | Type | Description |
|-----------|------|-------------|
| `equation` | `Expr` | Partial differential equation |
| `function` | `AppliedUndef` | The function to solve for |

**Returns:** `Expr` — General solution of the PDE.

---

### `solve_ivp`

```python
solve_ivp(equation: Expr, function: AppliedUndef, ics: dict) -> Expr
```

Solves an Initial Value Problem (IVP) for an ODE.

| Parameter | Type | Description |
|-----------|------|-------------|
| `equation` | `Expr` | Differential equation |
| `function` | `AppliedUndef` | The function to solve for |
| `ics` | `dict` | Initial conditions (e.g., `{f(0): 1}`) |

**Returns:** `Expr` — Particular solution matching initial conditions.
