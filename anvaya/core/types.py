"""
Type definitions for Anvaya Mathematics Library.

Provides type aliases for common mathematical objects and protocols
for backend implementations.
"""
from typing import Union, List, Tuple, TypeVar, Protocol, runtime_checkable
import numpy as np
from numpy.typing import ArrayLike, NDArray

# Type aliases for mathematical objects
Scalar = Union[int, float, complex]
Vector = NDArray[np.floating]
Matrix = NDArray[np.floating]
Expression = TypeVar('Expression')  # Generic type for symbolic expressions


@runtime_checkable
class SymbolicBackend(Protocol):
    """Protocol for symbolic computation backends."""
    
    def symbol(self, name: str) -> Expression:
        """Create a symbolic variable."""
        ...
    
    def simplify(self, expr: Expression) -> Expression:
        """Simplify an expression."""
        ...
    
    def diff(self, expr: Expression, var: Expression, n: int = 1) -> Expression:
        """Differentiate an expression."""
        ...
    
    def integrate(self, expr: Expression, var: Expression) -> Expression:
        """Integrate an expression."""
        ...


# Named tuple types for structured returns
from typing import NamedTuple


class EigenResult(NamedTuple):
    """Result of eigenvalue computation."""
    values: np.ndarray
    """Eigenvalues of the matrix."""
    vectors: np.ndarray
    """Matrix of eigenvectors (each column is an eigenvector)."""


class RootResult(NamedTuple):
    """Result of root-finding computation."""
    root: float
    """The computed root."""
    converged: bool
    """Whether the method converged."""
    iterations: int
    """Number of iterations performed."""
    function_calls: int
    """Number of function evaluations."""


class OptimizeResult(NamedTuple):
    """Result of optimization."""
    x: np.ndarray
    """Optimal point."""
    fun: float
    """Function value at optimal point."""
    success: bool
    """Whether optimization succeeded."""
    message: str
    """Description of termination."""
    iterations: int
    """Number of iterations."""


class LinearRegressionResult(NamedTuple):
    """Result of linear regression."""
    slope: float
    """Slope of the regression line."""
    intercept: float
    """Y-intercept of the regression line."""
    r_value: float
    """Correlation coefficient."""
    p_value: float
    """Two-sided p-value for hypothesis test."""
    std_err: float
    """Standard error of the estimated slope."""
