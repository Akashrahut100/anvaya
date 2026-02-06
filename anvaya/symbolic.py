import sympy as sp

class SymbolicEngine:
    """
    Core symbolic engine for Sutra, powered by SymPy.
    """
    
    def symbol(self, name):
        """Create a symbolic variable."""
        return sp.Symbol(name)
    
    def symbols(self, names):
        """Create multiple symbolic variables."""
        return sp.symbols(names)
    
    def simplify(self, expression):
        """Simplifies a mathematical expression."""
        return sp.simplify(expression)
    
    def expand(self, expression):
        """Expands a mathematical expression."""
        return sp.expand(expression)
    
    def factor(self, expression):
        """Factors a mathematical expression."""
        return sp.factor(expression)
    
    def solve(self, equation, variable):
        """Solves an equation for a given variable."""
        return sp.solve(equation, variable)
    
    def expr(self, string_expr):
        """Parses a string into a symbolic expression."""
        return sp.sympify(string_expr)
    
    def diff(self, expr, var, n=1):
        """Symbolic differentiation."""
        return sp.diff(expr, var, n)
    
    def integrate(self, expr, var, limits=None):
        """
        Symbolic integration.
        limits: (var, min, max) for definite integral.
        """
        if limits:
            return sp.integrate(expr, limits)
        return sp.integrate(expr, var)
    
    def limit(self, expr, var, point, direction='+'):
        """Computes the limit of an expression."""
        return sp.limit(expr, var, point, dir=direction)

# Expose a default instance for easy usage
engine = SymbolicEngine()

def var(names):
    return engine.symbols(names)

def simplify(expr):
    return engine.simplify(expr)

def diff(expr, var, n=1):
    return engine.diff(expr, var, n)

def integrate(expr, var, limits=None):
    return engine.integrate(expr, var, limits)
