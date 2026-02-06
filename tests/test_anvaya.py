"""
Unit tests for Anvaya Mathematics Library.
"""
import pytest
import numpy as np
from numpy.testing import assert_array_almost_equal


class TestLinearAlgebra:
    """Tests for linear algebra module."""
    
    def test_determinant_2x2(self):
        from anvaya import linear_algebra as la
        A = [[1, 2], [3, 4]]
        assert la.determinant(A) == pytest.approx(-2.0)
    
    def test_determinant_identity(self):
        from anvaya import linear_algebra as la
        I = np.eye(3)
        assert la.determinant(I) == pytest.approx(1.0)
    
    def test_inverse_roundtrip(self):
        from anvaya import linear_algebra as la
        A = np.array([[1, 2], [3, 4]])
        A_inv = la.inverse(A)
        result = A @ A_inv
        assert_array_almost_equal(result, np.eye(2), decimal=10)
    
    def test_eigenvalues_diagonal(self):
        from anvaya import linear_algebra as la
        D = np.diag([1, 2, 3])
        result = la.eigenvalues(D)
        assert set(np.round(result.values, 10)) == {1.0, 2.0, 3.0}
    
    def test_solve_linear_system(self):
        from anvaya import linear_algebra as la
        A = [[2, 1], [1, 3]]
        b = [1, 2]
        x = la.solve_linear_system(A, b)
        assert_array_almost_equal(A @ x, b)


class TestNumberTheory:
    """Tests for number theory module."""
    
    def test_prime_factors_360(self):
        from anvaya import number_theory as nt
        factors = nt.prime_factors(360)
        assert factors == {2: 3, 3: 2, 5: 1}
    
    def test_gcd(self):
        from anvaya import number_theory as nt
        assert nt.gcd(48, 18) == 6
    
    def test_lcm(self):
        from anvaya import number_theory as nt
        assert nt.lcm(12, 18) == 36
    
    def test_totient(self):
        from anvaya import number_theory as nt
        assert nt.totient(10) == 4  # {1, 3, 7, 9}
    
    def test_is_prime(self):
        from anvaya import number_theory as nt
        assert nt.is_prime(17) == True
        assert nt.is_prime(18) == False
    
    def test_mod_inverse(self):
        from anvaya import number_theory as nt
        # 3 * 4 = 12 ≡ 1 (mod 11)
        assert nt.mod_inverse(3, 11) == 4
    
    def test_is_coprime(self):
        from anvaya import number_theory as nt
        assert nt.is_coprime(15, 28) == True
        assert nt.is_coprime(12, 18) == False


class TestProbability:
    """Tests for probability module."""
    
    def test_normal_pdf_at_mean(self):
        from anvaya import probability as prob
        dist = prob.Normal(0, 1)
        # PDF at mean of standard normal ≈ 0.3989
        assert dist.pdf(0) == pytest.approx(0.3989, rel=0.01)
    
    def test_normal_cdf_at_mean(self):
        from anvaya import probability as prob
        dist = prob.Normal(0, 1)
        # CDF at mean = 0.5
        assert dist.cdf(0) == pytest.approx(0.5)
    
    def test_bayes_theorem(self):
        from anvaya import probability as prob
        # P(A|B) = P(B|A) * P(A) / P(B)
        result = prob.bayes_theorem(0.9, 0.01, 0.05)
        expected = (0.9 * 0.01) / 0.05
        assert result == pytest.approx(expected)
    
    def test_bayes_invalid_probability(self):
        from anvaya import probability as prob
        from anvaya.core.exceptions import InvalidInputError
        with pytest.raises(InvalidInputError):
            prob.bayes_theorem(1.5, 0.5, 0.5)  # p > 1 is invalid


class TestCalculus:
    """Tests for calculus module."""
    
    def test_differentiation(self):
        from anvaya import calculus
        from anvaya.symbolic import var
        import sympy as sp
        
        x = var('x')
        result = calculus.diff(x**3, x)
        assert result == 3*x**2
    
    def test_integration(self):
        from anvaya import calculus
        from anvaya.symbolic import var
        
        x = var('x')
        result = calculus.integrate(x**2, x)
        # Should be x³/3 (without constant)
        assert str(result) == 'x**3/3'
    
    def test_limit(self):
        from anvaya import calculus
        from anvaya.symbolic import var
        
        x = var('x')
        result = calculus.limit(x**2, x, 3)
        assert result == 9


class TestStatistics:
    """Tests for statistics module."""
    
    def test_mean(self):
        from anvaya import statistics as stats
        data = [1, 2, 3, 4, 5]
        assert stats.mean(data) == pytest.approx(3.0)
    
    def test_median_odd(self):
        from anvaya import statistics as stats
        data = [1, 2, 3, 4, 5]
        assert stats.median(data) == pytest.approx(3.0)
    
    def test_median_even(self):
        from anvaya import statistics as stats
        data = [1, 2, 3, 4, 5, 6]
        assert stats.median(data) == pytest.approx(3.5)
    
    def test_variance(self):
        from anvaya import statistics as stats
        data = [1, 2, 3, 4, 5]
        # Population variance = 2.0
        assert stats.variance(data) == pytest.approx(2.0)


class TestAlgebra:
    """Tests for algebra module."""
    
    def test_solve_quadratic(self):
        from anvaya import algebra
        from anvaya.symbolic import var
        
        x = var('x')
        solutions = algebra.solve_quadratic(x**2 - 5*x + 6, x)
        assert set(solutions) == {2, 3}
    
    def test_expand_poly(self):
        from anvaya import algebra
        from anvaya.symbolic import var
        import sympy as sp
        
        x = var('x')
        result = algebra.expand_poly((x + 1)**2)
        expected = x**2 + 2*x + 1
        assert sp.expand(result - expected) == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
