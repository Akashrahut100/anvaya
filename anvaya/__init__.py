"""
Anvaya (अन्वय) - A comprehensive Python mathematics library.

Inspired by ancient Indian mathematical traditions, Anvaya provides
a unified interface for:

    - **algebra**: Equations, polynomials, factorization
    - **linear_algebra**: Matrices, eigenvalues, vectors
    - **calculus**: Derivatives, integrals, series
    - **differential_equations**: ODEs, PDEs
    - **statistics**: Descriptive statistics, regression
    - **probability**: Distributions, Bayes theorem
    - **discrete**: Set theory, logic, Boolean algebra
    - **graph_theory**: Graphs, shortest paths, MST
    - **number_theory**: Primes, GCD, modular arithmetic
    - **numerical**: Root finding, integration
    - **optimization**: Linear programming, gradient descent
    - **vector_calculus**: Gradient, divergence, curl
    - **complex_analysis**: Residues, contour integration
    - **symbolic**: Expression manipulation

Quick Start
-----------
>>> from anvaya import algebra, calculus
>>> from anvaya.symbolic import var
>>> x = var('x')
>>> algebra.solve_quadratic(x**2 - 4, x)
[-2, 2]

Installation
------------
pip install anvaya

Links
-----
- GitHub: https://github.com/Akashrahut100/anvaya
- Documentation: https://anvaya.readthedocs.io
"""

__version__ = "1.0.0"
__author__ = "Akash Rahut"
__all__ = [
    'algebra',
    'calculus',
    'complex_analysis',
    'core',
    'differential_equations',
    'discrete',
    'graph_theory',
    'linear_algebra',
    'number_theory',
    'numerical',
    'optimization',
    'probability',
    'statistics',
    'symbolic',
    'vector_calculus',
]

# Core module (types, exceptions)
from . import core

# Mathematical modules
from . import algebra
from . import linear_algebra
from . import calculus
from . import differential_equations
from . import statistics
from . import probability
from . import discrete
from . import graph_theory
from . import number_theory
from . import numerical
from . import optimization
from . import vector_calculus
from . import complex_analysis
from . import symbolic

# Convenience re-exports
from .core.exceptions import (
    AnvayaError,
    SingularMatrixError,
    ConvergenceError,
    DimensionMismatchError,
    InvalidInputError,
)

