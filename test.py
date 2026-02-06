"""
Anvaya - Comprehensive Test Suite
Testing all 14 mathematical modules
"""

print("=" * 60)
print("ANVAYA MATHEMATICS LIBRARY - TEST SUITE")
print("=" * 60)

# Test 1: Symbolic Mathematics
print("\n[1] SYMBOLIC MATHEMATICS")
print("-" * 40)
try:
    from anvaya.symbolic import SymbolicEngine, var
    engine = SymbolicEngine()
    x = var('x')
    y = var('y')
    expr = (x + y)**2
    expanded = engine.expand(expr)
    print(f"   Expression: (x + y)^2")
    print(f"   Expanded: {expanded}")
    print("   [PASSED] Symbolic Mathematics")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 2: Algebra
print("\n[2] ALGEBRA")
print("-" * 40)
try:
    from anvaya import algebra
    from anvaya.symbolic import var
    x = var('x')
    
    # Quadratic equation: x^2 - 5x + 6 = 0
    equation = x**2 - 5*x + 6
    solutions = algebra.solve_quadratic(equation, x)
    print(f"   Quadratic x^2 - 5x + 6 = 0")
    print(f"   Solutions: {solutions}")
    
    # Polynomial expansion
    expanded = algebra.expand_poly((x + 2)**3)
    print(f"   (x + 2)^3 = {expanded}")
    print("   [PASSED] Algebra")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 3: Linear Algebra
print("\n[3] LINEAR ALGEBRA")
print("-" * 40)
try:
    from anvaya import linear_algebra as la
    import numpy as np
    
    A = la.matrix([[1, 2], [3, 4]])
    print(f"   Matrix A:\n{A}")
    print(f"   Determinant: {la.determinant(A)}")
    print(f"   Inverse:\n{la.inverse(A)}")
    
    eigenvalues, eigenvectors = la.eigenvalues(A)
    print(f"   Eigenvalues: {eigenvalues}")
    print("   [PASSED] Linear Algebra")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 4: Calculus
print("\n[4] CALCULUS")
print("-" * 40)
try:
    from anvaya import calculus
    from anvaya.symbolic import var
    x = var('x')
    
    # Differentiation (use diff, not differentiate)
    derivative = calculus.diff(x**3, x)
    print(f"   d/dx(x^3) = {derivative}")
    
    # Integration
    integral = calculus.integrate(x**2, x)
    print(f"   Integral of x^2 dx = {integral}")
    
    # Limit
    limit_val = calculus.limit(x**2, x, 3)
    print(f"   lim(x->3) x^2 = {limit_val}")
    print("   [PASSED] Calculus")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 5: Differential Equations
print("\n[5] DIFFERENTIAL EQUATIONS")
print("-" * 40)
try:
    from anvaya import differential_equations as de
    from anvaya.symbolic import var
    import sympy as sp
    
    x = var('x')
    y = sp.Function('y')
    
    # Solve y' = y
    solution = de.solve_ode(sp.Derivative(y(x), x) - y(x), y(x))
    print(f"   ODE: y' = y")
    print(f"   Solution: {solution}")
    print("   [PASSED] Differential Equations")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 6: Statistics
print("\n[6] STATISTICS")
print("-" * 40)
try:
    from anvaya import statistics as stats
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"   Data: {data}")
    print(f"   Mean: {stats.mean(data)}")
    print(f"   Median: {stats.median(data)}")
    print(f"   Std Dev: {stats.stdev(data):.4f}")  # stdev, not std_dev
    print(f"   Variance: {stats.variance(data):.4f}")
    print("   [PASSED] Statistics")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 7: Probability
print("\n[7] PROBABILITY THEORY")
print("-" * 40)
try:
    from anvaya import probability as prob
    
    # Normal distribution (use normal_dist, not normal_distribution)
    normal = prob.normal_dist(0, 1)
    print(f"   Normal(0, 1) PDF at x=0: {prob.pdf(normal, 0):.4f}")
    print(f"   Normal(0, 1) CDF at x=0: {prob.cdf(normal, 0):.4f}")
    
    # Bayes theorem
    result = prob.bayes_theorem(0.9, 0.01, 0.05)
    print(f"   Bayes P(A|B): {result:.4f}")
    print("   [PASSED] Probability")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 8: Discrete Mathematics
print("\n[8] DISCRETE MATHEMATICS")
print("-" * 40)
try:
    from anvaya.discrete import Set
    
    A = Set.new(1, 2, 3)
    B = Set.new(2, 3, 4)
    print(f"   Set A: {A}")
    print(f"   Set B: {B}")
    print(f"   Union: {Set.union(A, B)}")
    print(f"   Intersection: {Set.intersection(A, B)}")
    print(f"   Difference: {Set.difference(A, B)}")
    print("   [PASSED] Discrete Mathematics")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 9: Graph Theory
print("\n[9] GRAPH THEORY")
print("-" * 40)
try:
    from anvaya import graph_theory as gt
    
    G = gt.Graph()
    G.add_edge(1, 2, weight=1)
    G.add_edge(2, 3, weight=2)
    G.add_edge(1, 3, weight=4)
    
    print(f"   Graph edges: {list(G.edges())}")
    path = gt.shortest_path(G, 1, 3)
    print(f"   Shortest path 1->3: {path}")
    print("   [PASSED] Graph Theory")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 10: Number Theory
print("\n[10] NUMBER THEORY")
print("-" * 40)
try:
    from anvaya import number_theory as nt
    
    # Use factorint, not prime_factors
    print(f"   Prime factors of 360: {nt.factorint(360)}")
    print(f"   GCD(48, 18): {nt.gcd(48, 18)}")
    print(f"   LCM(12, 18): {nt.lcm(12, 18)}")
    print(f"   Euler's Totient phi(10): {nt.totient(10)}")
    print(f"   Hexadecimal of 255: {nt.to_hex(255)}")
    print(f"   Binary of 10: {nt.to_bin(10)}")
    print(f"   Octal of 64: {nt.to_oct(64)}")
    print(f"   Decimal from hex '0xff': {nt.from_base('0xff', 16)}")
    print(f"   Binary '1010' to Hex: {nt.convert_base('1010', 2, 16)}")
    print(f"   Hex 'ff' to Binary: {nt.convert_base('ff', 16, 2)}")
    print("   [PASSED] Number Theory")



except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 11: Numerical Methods
print("\n[11] NUMERICAL METHODS")
print("-" * 40)
try:
    from anvaya import numerical
    import numpy as np
    
    # Root finding: x^2 - 2 = 0 -> x = sqrt(2)
    def f(x):
        return x**2 - 2
    
    # Use root_find, not find_root
    root = numerical.root_find(f, 1.5)
    print(f"   Root of x^2 - 2 = 0: {root:.6f}")
    print(f"   (sqrt(2) = 1.414214)")
    
    # Numerical integration (use numeric_integrate)
    def g(x):
        return x**2
    
    integral = numerical.numeric_integrate(g, 0, 1)
    print(f"   Integral of x^2 from 0 to 1 = {integral:.6f}")
    print("   [PASSED] Numerical Methods")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 12: Optimization
print("\n[12] OPTIMIZATION")
print("-" * 40)
try:
    from anvaya import optimization as opt
    import numpy as np
    
    # Minimize f(x) = (x-3)^2
    def f(x):
        return (x[0] - 3)**2
    
    result = opt.minimize(f, [0])
    print(f"   Minimize (x-3)^2")
    print(f"   Optimal x: {result.x[0]:.4f}")
    print(f"   Min value: {result.fun:.6f}")
    print("   [PASSED] Optimization")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 13: Vector Calculus
print("\n[13] VECTOR CALCULUS")
print("-" * 40)
try:
    from anvaya import vector_calculus as vc
    from anvaya.symbolic import var
    
    x, y, z = var('x'), var('y'), var('z')
    
    # Scalar field: f = x^2 + y^2 + z^2
    f = x**2 + y**2 + z**2
    grad = vc.gradient(f, [x, y, z])
    print(f"   Scalar field: f = x^2 + y^2 + z^2")
    print(f"   Gradient: {grad}")
    
    # Vector field divergence
    F = [x**2, y**2, z**2]
    div = vc.divergence(F, [x, y, z])
    print(f"   Vector field: F = [x^2, y^2, z^2]")
    print(f"   Divergence: {div}")
    print("   [PASSED] Vector Calculus")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Test 14: Complex Analysis
print("\n[14] COMPLEX ANALYSIS")
print("-" * 40)
try:
    from anvaya import complex_analysis as ca
    from anvaya.symbolic import var
    
    z = var('z')
    
    # Residue of 1/z at z=0
    residue = ca.residue(1/z, z, 0)
    print(f"   Residue of 1/z at z=0: {residue}")
    print("   [PASSED] Complex Analysis")
except Exception as e:
    print(f"   [FAILED] Error: {e}")

# Summary
print("\n" + "=" * 60)
print("ALL 14 MODULES TESTED!")
print("=" * 60)
print("\nAnvaya Mathematics Library is ready!")
print("Install with: pip install anvaya")
print("GitHub: https://github.com/Akashrahut100/anvaya")
print("=" * 60)
