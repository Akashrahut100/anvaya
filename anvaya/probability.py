"""
Probability Module for Anvaya.

Provides probability distributions and related computations.
"""
from typing import Union
from dataclasses import dataclass
from scipy import stats
import numpy as np

# Import custom exceptions
try:
    from .core.exceptions import InvalidInputError
except ImportError:
    class InvalidInputError(Exception):
        pass


def _validate_probability(value: float, name: str = "probability") -> None:
    """Validate that a value is a valid probability [0, 1]."""
    if not 0 <= value <= 1:
        raise InvalidInputError(
            f"{name} must be in [0, 1], got {value}",
            parameter=name,
            value=value,
            constraint="must be between 0 and 1"
        )


@dataclass(frozen=True)
class Normal:
    """
    Normal (Gaussian) distribution.
    
    Parameters
    ----------
    mean : float, default 0.0
        Mean (μ) of the distribution.
    std : float, default 1.0
        Standard deviation (σ) of the distribution.
    
    Examples
    --------
    >>> dist = Normal(0, 1)
    >>> dist.pdf(0)  # Peak of standard normal
    0.3989...
    """
    mean: float = 0.0
    std: float = 1.0
    
    def __post_init__(self):
        if self.std <= 0:
            raise InvalidInputError("Standard deviation must be positive", "std", self.std)
    
    def pdf(self, x: float) -> float:
        """Probability density function at x."""
        return stats.norm.pdf(x, loc=self.mean, scale=self.std)
    
    def cdf(self, x: float) -> float:
        """Cumulative distribution function at x."""
        return stats.norm.cdf(x, loc=self.mean, scale=self.std)
    
    def ppf(self, q: float) -> float:
        """Percent point function (inverse CDF) at q."""
        _validate_probability(q, "quantile")
        return stats.norm.ppf(q, loc=self.mean, scale=self.std)
    
    def sample(self, size: int = 1) -> np.ndarray:
        """Generate random samples."""
        return np.random.normal(self.mean, self.std, size)


@dataclass(frozen=True)
class Binomial:
    """
    Binomial distribution.
    
    Parameters
    ----------
    n : int
        Number of trials.
    p : float
        Probability of success in each trial.
    """
    n: int
    p: float
    
    def __post_init__(self):
        if self.n < 0:
            raise InvalidInputError("n must be non-negative", "n", self.n)
        _validate_probability(self.p, "p")
    
    def pmf(self, k: int) -> float:
        """Probability mass function at k."""
        return stats.binom.pmf(k, n=self.n, p=self.p)
    
    def cdf(self, k: int) -> float:
        """Cumulative distribution function at k."""
        return stats.binom.cdf(k, n=self.n, p=self.p)
    
    def sample(self, size: int = 1) -> np.ndarray:
        """Generate random samples."""
        return np.random.binomial(self.n, self.p, size)


@dataclass(frozen=True)  
class Poisson:
    """
    Poisson distribution.
    
    Parameters
    ----------
    mu : float
        Expected number of events (λ).
    """
    mu: float
    
    def __post_init__(self):
        if self.mu < 0:
            raise InvalidInputError("mu must be non-negative", "mu", self.mu)
    
    def pmf(self, k: int) -> float:
        """Probability mass function at k."""
        return stats.poisson.pmf(k, mu=self.mu)
    
    def cdf(self, k: int) -> float:
        """Cumulative distribution function at k."""
        return stats.poisson.cdf(k, mu=self.mu)
    
    def sample(self, size: int = 1) -> np.ndarray:
        """Generate random samples."""
        return np.random.poisson(self.mu, size)


# Factory functions for backward compatibility
def normal_dist(mean: float = 0, std: float = 1) -> Normal:
    """Create a Normal distribution object."""
    return Normal(mean=mean, std=std)


def binomial_dist(n: int, p: float) -> Binomial:
    """Create a Binomial distribution object."""
    return Binomial(n=n, p=p)


def poisson_dist(mu: float) -> Poisson:
    """Create a Poisson distribution object."""
    return Poisson(mu=mu)


def pdf(dist: Union[Normal, object], x: float) -> float:
    """
    Probability Density Function.
    
    Parameters
    ----------
    dist : distribution object
        A distribution with a pdf method.
    x : float
        Point at which to evaluate the PDF.
    
    Returns
    -------
    float
        PDF value at x.
    """
    return dist.pdf(x)


def pmf(dist: Union[Binomial, Poisson, object], k: int) -> float:
    """
    Probability Mass Function (for discrete distributions).
    
    Parameters
    ----------
    dist : distribution object
        A distribution with a pmf method.
    k : int
        Point at which to evaluate the PMF.
    
    Returns
    -------
    float
        PMF value at k.
    """
    return dist.pmf(k)


def cdf(dist: Union[Normal, Binomial, Poisson, object], x: float) -> float:
    """
    Cumulative Distribution Function.
    
    Parameters
    ----------
    dist : distribution object
        A distribution with a cdf method.
    x : float
        Point at which to evaluate the CDF.
    
    Returns
    -------
    float
        CDF value at x.
    """
    return dist.cdf(x)


def bayes_theorem(
    p_b_given_a: float,
    p_a: float,
    p_b: float,
    *,
    validate: bool = True
) -> float:
    """
    Apply Bayes' theorem: P(A|B) = P(B|A) * P(A) / P(B)
    
    Parameters
    ----------
    p_b_given_a : float
        P(B|A), probability of B given A. Must be in [0, 1].
    p_a : float
        P(A), prior probability of A. Must be in [0, 1].
    p_b : float
        P(B), marginal probability of B. Must be in (0, 1].
    validate : bool, default True
        If True, validate probability constraints.
    
    Returns
    -------
    float
        P(A|B), the posterior probability.
    
    Raises
    ------
    InvalidInputError
        If probabilities are out of valid range.
    ZeroDivisionError
        If p_b is zero.
    
    Examples
    --------
    >>> # Medical test: sensitivity=0.99, disease prevalence=0.01, positive rate=0.05
    >>> bayes_theorem(0.99, 0.01, 0.05)
    0.198
    """
    if validate:
        _validate_probability(p_b_given_a, "p_b_given_a")
        _validate_probability(p_a, "p_a")
        _validate_probability(p_b, "p_b")
        
        if p_b == 0:
            raise ZeroDivisionError("p_b cannot be zero (event B has zero probability)")
    
    return (p_b_given_a * p_a) / p_b


def expected_value(values: list, probabilities: list) -> float:
    """
    Compute expected value E[X] = Σ x_i * P(x_i).
    
    Parameters
    ----------
    values : list of float
        Possible values of the random variable.
    probabilities : list of float
        Corresponding probabilities (must sum to 1).
    
    Returns
    -------
    float
        Expected value.
    """
    values = np.array(values)
    probs = np.array(probabilities)
    
    if not np.isclose(probs.sum(), 1.0, rtol=1e-6):
        raise InvalidInputError(
            f"Probabilities must sum to 1, got {probs.sum()}",
            parameter="probabilities"
        )
    
    return float(np.sum(values * probs))


def variance_discrete(values: list, probabilities: list) -> float:
    """
    Compute variance Var(X) = E[(X - μ)²].
    
    Parameters
    ----------
    values : list of float
        Possible values of the random variable.
    probabilities : list of float
        Corresponding probabilities (must sum to 1).
    
    Returns
    -------
    float
        Variance.
    """
    mu = expected_value(values, probabilities)
    values = np.array(values)
    probs = np.array(probabilities)
    return float(np.sum(probs * (values - mu) ** 2))

