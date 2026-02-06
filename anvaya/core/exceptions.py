"""
Custom Exceptions for Anvaya Mathematics Library.

All exceptions inherit from AnvayaError for easy catching.
"""


class AnvayaError(Exception):
    """
    Base exception for all Anvaya library errors.
    
    Catch this to handle any Anvaya-specific error.
    
    Examples
    --------
    >>> try:
    ...     result = some_anvaya_function()
    ... except AnvayaError as e:
    ...     print(f"Anvaya error: {e}")
    """
    pass


class SingularMatrixError(AnvayaError):
    """
    Raised when a matrix operation fails due to singularity.
    
    This typically occurs when attempting to invert a singular matrix
    or solve a system with a singular coefficient matrix.
    
    Attributes
    ----------
    condition_number : float, optional
        The condition number of the matrix, if available.
    """
    
    def __init__(self, message: str = "Matrix is singular", condition_number: float = None):
        self.condition_number = condition_number
        if condition_number is not None:
            message = f"{message} (condition number: {condition_number:.2e})"
        super().__init__(message)


class ConvergenceError(AnvayaError):
    """
    Raised when a numerical method fails to converge.
    
    This can occur in iterative methods like Newton-Raphson, gradient descent,
    or numerical integration when the maximum iterations are exceeded
    or the method diverges.
    
    Attributes
    ----------
    iterations : int, optional
        Number of iterations performed before failure.
    last_value : float, optional
        The last computed value before failure.
    """
    
    def __init__(
        self, 
        message: str = "Method failed to converge",
        iterations: int = None,
        last_value: float = None
    ):
        self.iterations = iterations
        self.last_value = last_value
        if iterations is not None:
            message = f"{message} after {iterations} iterations"
        super().__init__(message)


class DimensionMismatchError(AnvayaError):
    """
    Raised when array/matrix dimensions don't match the operation requirements.
    
    Examples include attempting to multiply incompatible matrices,
    or computing the inverse of a non-square matrix.
    
    Attributes
    ----------
    expected : tuple, optional
        Expected dimensions.
    got : tuple, optional
        Actual dimensions received.
    """
    
    def __init__(
        self, 
        message: str = "Dimension mismatch",
        expected: tuple = None,
        got: tuple = None
    ):
        self.expected = expected
        self.got = got
        if expected is not None and got is not None:
            message = f"{message}: expected {expected}, got {got}"
        super().__init__(message)


class InvalidInputError(AnvayaError):
    """
    Raised for mathematically invalid inputs.
    
    Examples include negative values where positive are required,
    probabilities outside [0, 1], or empty data sets.
    
    Attributes
    ----------
    parameter : str, optional
        Name of the invalid parameter.
    value : any, optional
        The invalid value that was provided.
    constraint : str, optional
        Description of the constraint that was violated.
    """
    
    def __init__(
        self,
        message: str = "Invalid input",
        parameter: str = None,
        value = None,
        constraint: str = None
    ):
        self.parameter = parameter
        self.value = value
        self.constraint = constraint
        
        if parameter is not None:
            if value is not None and constraint is not None:
                message = f"Invalid {parameter}={value}: {constraint}"
            elif value is not None:
                message = f"Invalid {parameter}={value}"
        super().__init__(message)
