import sympy as sp

def residue(expr, variable, point):
    """
    Computes the residue of an expression at a given point.
    """
    return sp.residue(expr, variable, point)

def complex_expand(expr):
    """
    Expands a complex expression into real and imaginary parts.
    """
    return sp.expand_complex(expr)

def complex_integrate(expr, variable, path):
    """
    Computes a contour integral.
    Currently wraps basic integration; full contour integration requires path parameterization.
    """
    # SymPy doesn't have a direct 'contour_integrate' function that takes a geometric path object easily
    # typically one parameterizes the path.
    return sp.integrate(expr, (variable, path[0], path[1])) # Very basic interpretation
