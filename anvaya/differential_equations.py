import sympy as sp

def solve_ode(equation, function):
    """
    Solves an Ordinary Differential Equation.
    equation: SymPy Eq or expression equal to 0.
    function: function to solve for (e.g. f(x)).
    """
    return sp.dsolve(equation, function)

def solve_pde(equation, function):
    """
    Solves a Partial Differential Equation.
    """
    return sp.pdsolve(equation, function)

def solve_ivp(equation, function, ics):
    """
    Solves an Initial Value Problem for ODEs.
    ics: Dictionary of initial conditions, e.g. {f(0): 1, f(x).diff(x).subs(x, 0): 0}
    """
    return sp.dsolve(equation, function, ics=ics)
