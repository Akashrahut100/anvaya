import sympy as sp

def gradient(scalar_field, variables):
    """
    Computes the gradient of a scalar field.
    scalar_field: SymPy expression.
    variables: List of variables (e.g. [x, y, z]).
    """
    return [sp.diff(scalar_field, var) for var in variables]

def divergence(vector_field, variables):
    """
    Computes the divergence of a vector field.
    vector_field: List of expressions.
    variables: List of variables.
    """
    return sum(sp.diff(comp, var) for comp, var in zip(vector_field, variables))

def curl(vector_field, variables):
    """
    Computes the curl of a 3D vector field.
    vector_field: List of 3 expressions [Fx, Fy, Fz].
    variables: List of 3 variables [x, y, z].
    """
    if len(vector_field) != 3 or len(variables) != 3:
        raise ValueError("Curl is only defined for 3D vector fields.")
    
    Fx, Fy, Fz = vector_field
    x, y, z = variables
    
    return [
        sp.diff(Fz, y) - sp.diff(Fy, z),
        sp.diff(Fx, z) - sp.diff(Fz, x),
        sp.diff(Fy, x) - sp.diff(Fx, y)
    ]

def line_integral(vector_field, curve_param, limits):
    """
    Computes the line integral of a vector field along a curve.
    vector_field: List of expressions [P, Q, R] defined in terms of curve_param variables.
    curve_param: Dictionary mapping x, y, z to functions of parameter t.
    limits: (t, t_start, t_end).
    """
    # This is a bit complex to generalize simply without a proper Vector class, 
    # but let's provide a basic implementation where user substitutes themselves before calling
    # or improve later. For now, using SymPy's integrate.
    raise NotImplementedError("Use symbolic integration with parameterized substitutions.")
