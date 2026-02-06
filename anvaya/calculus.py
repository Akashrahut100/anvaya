import sympy as sp

def limit(expr, variable, point, direction='+'):
    """
    Computes the limit of an expression as variable approaches point.
    """
    return sp.limit(expr, variable, point, dir=direction)

def diff(expr, variable, order=1):
    """
    Computes the derivative of an expression.
    """
    return sp.diff(expr, variable, order)

def integrate(expr, variable, lower=None, upper=None):
    """
    Computes the integral of an expression.
    If lower and upper are provided, computes the definite integral.
    Otherwise, computes the indefinite integral.
    """
    if lower is not None and upper is not None:
        return sp.integrate(expr, (variable, lower, upper))
    return sp.integrate(expr, variable)

def taylor_series(expr, variable, point, n):
    """
    Expands an expression into a Taylor series up to order n around point.
    """
    return sp.series(expr, variable, point, n).removeO()

def maclaurin_series(expr, variable, n):
    """
    Expands an expression into a Maclaurin series (Taylor series at 0).
    """
    return sp.series(expr, variable, 0, n).removeO()
