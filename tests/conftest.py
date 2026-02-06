"""
Pytest configuration and fixtures for Anvaya tests.
"""
import pytest
import numpy as np


@pytest.fixture
def rng():
    """Provide a seeded random number generator for reproducibility."""
    return np.random.default_rng(42)


@pytest.fixture
def sample_matrix():
    """Provide a sample 3x3 matrix for testing."""
    return np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 10]  # Note: not singular (det ≠ 0)
    ], dtype=np.float64)


@pytest.fixture
def singular_matrix():
    """Provide a singular matrix for testing error handling."""
    return np.array([
        [1, 2, 3],
        [2, 4, 6],  # Row 2 = 2 * Row 1
        [1, 1, 1]
    ], dtype=np.float64)


@pytest.fixture
def identity_matrix():
    """Provide an identity matrix."""
    return np.eye(3)


@pytest.fixture
def symbolic_var():
    """Provide a symbolic variable for calculus tests."""
    from anvaya.symbolic import var
    return var('x')
