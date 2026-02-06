"""
Anvaya Core Module.

Contains type definitions, exceptions, and utility functions used across the library.
"""

from .exceptions import (
    AnvayaError,
    SingularMatrixError,
    ConvergenceError,
    DimensionMismatchError,
    InvalidInputError,
)
from .types import Scalar, Vector, Matrix

__all__ = [
    'AnvayaError',
    'SingularMatrixError',
    'ConvergenceError',
    'DimensionMismatchError',
    'InvalidInputError',
    'Scalar',
    'Vector',
    'Matrix',
]
