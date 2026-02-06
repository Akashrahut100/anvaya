"""
Linear Algebra Module for Anvaya.

Provides matrix operations, decompositions, and vector operations
using NumPy as the backend.
"""
from typing import Tuple, Union, List
import numpy as np
from numpy.typing import ArrayLike, NDArray
import warnings

# Import custom exceptions
try:
    from .core.exceptions import SingularMatrixError, DimensionMismatchError
except ImportError:
    # Fallback for direct module usage
    class SingularMatrixError(Exception):
        pass
    class DimensionMismatchError(Exception):
        pass


# Type alias
Matrix = NDArray[np.floating]
Vector = NDArray[np.floating]


def matrix(data: ArrayLike) -> Matrix:
    """
    Create a matrix from data (list of lists or array).
    
    Parameters
    ----------
    data : array_like
        Input data, can be nested lists or numpy array.
    
    Returns
    -------
    np.ndarray
        2D numpy array.
    
    Examples
    --------
    >>> matrix([[1, 2], [3, 4]])
    array([[1, 2],
           [3, 4]])
    """
    return np.array(data, dtype=np.float64)


def multiply(A: ArrayLike, B: ArrayLike) -> Matrix:
    """
    Matrix multiplication.
    
    Parameters
    ----------
    A, B : array_like
        Matrices to multiply.
    
    Returns
    -------
    np.ndarray
        Result of A @ B.
    
    Raises
    ------
    DimensionMismatchError
        If matrix dimensions are incompatible for multiplication.
    """
    A, B = np.asarray(A), np.asarray(B)
    if A.shape[-1] != B.shape[0]:
        raise DimensionMismatchError(
            f"Cannot multiply matrices with shapes {A.shape} and {B.shape}"
        )
    return np.dot(A, B)


def determinant(A: ArrayLike, *, check_numerical: bool = True) -> float:
    """
    Calculate the determinant of a matrix.
    
    Parameters
    ----------
    A : array_like
        Square matrix.
    check_numerical : bool, default True
        If True, warn about potential numerical instability.
    
    Returns
    -------
    float
        Determinant of the matrix.
    
    Raises
    ------
    DimensionMismatchError
        If matrix is not square.
    
    Examples
    --------
    >>> determinant([[1, 2], [3, 4]])
    -2.0
    """
    A = np.asarray(A, dtype=np.float64)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise DimensionMismatchError(
            f"Determinant requires square matrix, got shape {A.shape}"
        )
    
    det = np.linalg.det(A)
    
    if check_numerical and A.shape[0] > 10:
        cond = np.linalg.cond(A)
        if cond > 1e10:
            warnings.warn(
                f"Matrix has high condition number ({cond:.2e}). "
                "Determinant may be numerically unreliable.",
                RuntimeWarning
            )
    
    return float(det)


def inverse(A: ArrayLike, *, check_singular: bool = True) -> Matrix:
    """
    Calculate the inverse of a matrix.
    
    Parameters
    ----------
    A : array_like
        Square matrix to invert.
    check_singular : bool, default True
        If True, check for singularity before attempting inversion.
    
    Returns
    -------
    np.ndarray
        Inverse of A.
    
    Raises
    ------
    SingularMatrixError
        If matrix is singular or nearly singular.
    DimensionMismatchError
        If matrix is not square.
    
    Examples
    --------
    >>> inverse([[1, 2], [3, 4]])
    array([[-2. ,  1. ],
           [ 1.5, -0.5]])
    """
    A = np.asarray(A, dtype=np.float64)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise DimensionMismatchError(
            f"Inverse requires square matrix, got shape {A.shape}"
        )
    
    if check_singular:
        cond = np.linalg.cond(A)
        if cond > 1 / np.finfo(A.dtype).eps:
            raise SingularMatrixError(
                f"Matrix is singular or nearly singular",
                condition_number=cond
            )
    
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError as e:
        raise SingularMatrixError(str(e)) from e


def rank(A: ArrayLike) -> int:
    """
    Calculate the rank of a matrix.
    
    Parameters
    ----------
    A : array_like
        Input matrix.
    
    Returns
    -------
    int
        Rank of the matrix.
    """
    return int(np.linalg.matrix_rank(A))


# Import the named tuple type if available
try:
    from .core.types import EigenResult
except ImportError:
    from typing import NamedTuple
    class EigenResult(NamedTuple):
        values: np.ndarray
        vectors: np.ndarray


def eigenvalues(A: ArrayLike) -> EigenResult:
    """
    Compute eigenvalues and eigenvectors of a matrix.
    
    Parameters
    ----------
    A : array_like
        Square matrix.
    
    Returns
    -------
    EigenResult
        Named tuple with:
        - values: eigenvalues (1D array)
        - vectors: eigenvectors (columns of 2D array)
    
    Examples
    --------
    >>> result = eigenvalues([[1, 0], [0, 2]])
    >>> result.values
    array([1., 2.])
    """
    A = np.asarray(A, dtype=np.float64)
    vals, vecs = np.linalg.eig(A)
    return EigenResult(values=vals, vectors=vecs)


def dot_product(v1: ArrayLike, v2: ArrayLike) -> float:
    """
    Compute vector dot product.
    
    Parameters
    ----------
    v1, v2 : array_like
        Vectors of the same length.
    
    Returns
    -------
    float
        Dot product v1 · v2.
    """
    return float(np.dot(v1, v2))


def cross_product(v1: ArrayLike, v2: ArrayLike) -> Vector:
    """
    Compute vector cross product (3D only).
    
    Parameters
    ----------
    v1, v2 : array_like
        3D vectors.
    
    Returns
    -------
    np.ndarray
        Cross product v1 × v2.
    
    Raises
    ------
    DimensionMismatchError
        If vectors are not 3D.
    """
    v1, v2 = np.asarray(v1), np.asarray(v2)
    if v1.shape != (3,) or v2.shape != (3,):
        raise DimensionMismatchError(
            f"Cross product requires 3D vectors, got shapes {v1.shape} and {v2.shape}"
        )
    return np.cross(v1, v2)


def solve_linear_system(A: ArrayLike, b: ArrayLike) -> Vector:
    """
    Solve the linear system Ax = b.
    
    Parameters
    ----------
    A : array_like
        Coefficient matrix (n x n).
    b : array_like
        Right-hand side vector (n,).
    
    Returns
    -------
    np.ndarray
        Solution vector x.
    
    Raises
    ------
    SingularMatrixError
        If system is singular or underdetermined.
    
    Examples
    --------
    >>> solve_linear_system([[2, 1], [1, 3]], [1, 2])
    array([0.2, 0.6])
    """
    A = np.asarray(A, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    
    try:
        return np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        raise SingularMatrixError(f"Cannot solve system: {e}") from e


def norm(v: ArrayLike, ord: Union[int, float, str] = 2) -> float:
    """
    Compute vector or matrix norm.
    
    Parameters
    ----------
    v : array_like
        Vector or matrix.
    ord : {non-zero int, inf, -inf, 'fro', 'nuc'}, optional
        Order of the norm. Default is 2 (Euclidean).
    
    Returns
    -------
    float
        Norm of the input.
    """
    return float(np.linalg.norm(v, ord=ord))


def trace(A: ArrayLike) -> float:
    """
    Compute the trace (sum of diagonal elements) of a matrix.
    
    Parameters
    ----------
    A : array_like
        Square matrix.
    
    Returns
    -------
    float
        Sum of diagonal elements.
    """
    return float(np.trace(A))


def transpose(A: ArrayLike) -> Matrix:
    """
    Transpose a matrix.
    
    Parameters
    ----------
    A : array_like
        Input matrix.
    
    Returns
    -------
    np.ndarray
        Transposed matrix.
    """
    return np.transpose(A)


def is_symmetric(A: ArrayLike, rtol: float = 1e-10) -> bool:
    """
    Check if a matrix is symmetric.
    
    Parameters
    ----------
    A : array_like
        Square matrix.
    rtol : float, default 1e-10
        Relative tolerance for comparison.
    
    Returns
    -------
    bool
        True if A is symmetric within tolerance.
    """
    A = np.asarray(A)
    return np.allclose(A, A.T, rtol=rtol)


def is_positive_definite(A: ArrayLike) -> bool:
    """
    Check if a matrix is positive definite.
    
    A symmetric matrix is positive definite if all eigenvalues are positive.
    
    Parameters
    ----------
    A : array_like
        Square matrix.
    
    Returns
    -------
    bool
        True if A is positive definite.
    """
    A = np.asarray(A, dtype=np.float64)
    try:
        np.linalg.cholesky(A)
        return True
    except np.linalg.LinAlgError:
        return False

