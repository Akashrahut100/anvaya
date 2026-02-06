import sympy as sp
from .symbolic import engine

def solve_linear(equations, variables):
    """
    Solves a system of linear equations.
    equations: List of equations (expressions equal to 0).
    variables: List of variables to solve for.
    """
    return sp.solve(equations, variables)

def solve_quadratic(equation, variable):
    """
    Solves a quadratic equation.
    """
    return sp.solve(equation, variable)

def expand_poly(expression):
    """Expands a polynomial."""
    return sp.expand(expression)

def factor_poly(expression):
    """Factors a polynomial."""
    return sp.factor(expression)

def rational_simplify(expression):
    """Simplifies rational expressions."""
    return sp.cancel(expression)

def partial_fraction(expression, variable):
    """
    Computes partial fraction decomposition.
    """
    return sp.apart(expression, variable)

def solve_system(equations, variables):
    """
    Solves a system of equations (linear or non-linear).
    """
    return sp.solve(equations, variables)
