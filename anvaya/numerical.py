import scipy.optimize as opt
import scipy.integrate as integrate
import scipy.interpolate as interpolate

def root_find(func, x0, method='newton'):
    """
    Finds a root of a function.
    x0: Initial guess.
    method: 'newton', 'bisect', 'brentq' etc.
    """
    if method == 'newton':
        return opt.newton(func, x0)
    elif method == 'bisect':
        # Bisect requires a bracket (a, b)
        raise ValueError("Bisect requires a bracket specific call, use optimize.root_scalar")
    else:
        return opt.root(func, x0, method=method).x

def numeric_integrate(func, a, b):
    """
    Computes definite integral of func from a to b numerically.
    """
    return integrate.quad(func, a, b)[0]

def interp1d(x, y, kind='linear'):
    """
    Returns an interpolation function.
    """
    return interpolate.interp1d(x, y, kind=kind)
