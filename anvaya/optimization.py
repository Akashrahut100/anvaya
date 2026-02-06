import scipy.optimize as opt
import numpy as np

def minimize(func, x0, method='BFGS', constraints=()):
    """
    Minimizes a function.
    """
    return opt.minimize(func, x0, method=method, constraints=constraints)

def linear_program(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    """
    Solves a linear programming problem:
    minimize c @ x
    such that:
    A_ub @ x <= b_ub
    A_eq @ x == b_eq
    lb <= x <= ub
    """
    return opt.linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

def gradient_descent(func, grad, x0, learning_rate=0.01, max_iter=1000, tol=1e-6):
    """
    Simple gradient descent implementation.
    func: The objective function (unused if grad is provided, but good for tracking).
    grad: The gradient function.
    x0: Initial point.
    """
    x = np.array(x0, dtype=float)
    for _ in range(max_iter):
        g = np.array(grad(x))
        diff = -learning_rate * g
        if np.linalg.norm(diff) < tol:
            break
        x += diff
    return x
