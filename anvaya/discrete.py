import sympy as sp
from sympy.logic.boolalg import truth_table as sp_truth_table

class Set:
    """Wrapper for SymPy FiniteSet/Interval."""
    @staticmethod
    def new(*args):
        return sp.FiniteSet(*args)
    
    @staticmethod
    def union(s1, s2):
        return s1.union(s2)
    
    @staticmethod
    def intersection(s1, s2):
        return s1.intersect(s2)
    
    @staticmethod
    def difference(s1, s2):
        return s1 - s2

def truth_table(expression, variables):
    """
    Generates a truth table for a boolean expression.
    """
    return list(sp_truth_table(expression, variables))

def simplify_logic(expr):
    """Simplifies a logical expression."""
    return sp.simplify_logic(expr)

def satisfiable(expr):
    """Checks satisfiability."""
    return sp.satisfiable(expr)
