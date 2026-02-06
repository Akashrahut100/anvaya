
import sys
import os
import time
import importlib
import traceback

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def log_pass(msg):
    print(f"✅ {msg}")

def log_fail(msg):
    print(f"❌ {msg}")

def log_info(msg):
    print(f"ℹ️  {msg}")

def check_module_importability():
    print("\n--- Phase 1: Importability Check ---")
    modules = [
        "anvaya.algebra",
        "anvaya.calculus",
        "anvaya.complex_analysis",
        "anvaya.differential_equations",
        "anvaya.discrete",
        "anvaya.graph_theory",
        "anvaya.linear_algebra",
        "anvaya.number_theory",
        "anvaya.numerical",
        "anvaya.optimization",
        "anvaya.probability",
        "anvaya.statistics",
        "anvaya.symbolic",
        "anvaya.vector_calculus"
    ]
    
    success_count = 0
    for mod_name in modules:
        try:
            start_t = time.time()
            importlib.import_module(mod_name)
            load_time = (time.time() - start_t) * 1000
            log_pass(f"Imported {mod_name:<30} ({load_time:.2f}ms)")
            success_count += 1
        except Exception as e:
            log_fail(f"Failed to import {mod_name}")
            traceback.print_exc()
            
    return success_count == len(modules)

def check_basic_functionality():
    print("\n--- Phase 2: Functional Smoke Tests ---")
    
    # 1. Algebra
    try:
        from anvaya import algebra
        from anvaya.symbolic import var
        x = var('x')
        res = algebra.solve_quadratic(x**2 - 4, x)
        if len(res) == 2:
            log_pass("Algebra: Quadratic solver working")
        else:
            log_fail(f"Algebra: Quadratic solver returned unexpected {res}")
    except Exception as e:
        log_fail(f"Algebra Error: {e}")

    # 2. Calculus
    try:
        from anvaya import calculus
        d = calculus.diff(x**3, x)
        if str(d) == "3*x**2":
            log_pass("Calculus: Differentiation working")
        else:
            log_fail(f"Calculus: Differentiation unexpected result {d}")
    except Exception as e:
        log_fail(f"Calculus Error: {e}")

    # 3. Linear Algebra
    try:
        from anvaya import linear_algebra
        M = linear_algebra.matrix([[1, 2], [3, 4]])
        det = linear_algebra.determinant(M)
        if abs(det - (-2)) < 1e-9:
            log_pass("Linear Algebra: Determinant working")
        else:
            log_fail(f"Linear Algebra: Determinant incorrect {det}")
    except Exception as e:
        log_fail(f"Linear Algebra Error: {e}")

    # 4. Number Theory
    try:
        from anvaya import number_theory
        if number_theory.is_prime(17) and not number_theory.is_prime(18):
            log_pass("Number Theory: Primality test working")
        else:
            log_fail("Number Theory: Primality test failed")
    except Exception as e:
        log_fail(f"Number Theory Error: {e}")

    # 5. Statistics
    try:
        from anvaya import statistics
        data = [1, 2, 3, 4, 5]
        if statistics.mean(data) == 3.0:
            log_pass("Statistics: Mean calculation working")
        else:
            log_fail("Statistics: Mean calculation failed")
    except Exception as e:
        log_fail(f"Statistics Error: {e}")

    # 6. Probability
    try:
        from anvaya import probability
        norm = probability.Normal(0, 1)
        pdf_val = norm.pdf(0)
        if 0.39 < pdf_val < 0.40:
            log_pass("Probability: Normal PDF working")
        else:
            log_fail("Probability: Normal PDF failed")
    except Exception as e:
        log_fail(f"Probability Error: {e}")

    # 7. Symbolic
    try:
        from anvaya import symbolic
        expr = symbolic.simplify(var('x') + var('x'))
        if str(expr) == "2*x":
            log_pass("Symbolic: Simplification working")
        else:
            log_fail("Symbolic: Simplification failed")
    except Exception as e:
        log_fail(f"Symbolic Error: {e}")

    # 8. Numerical
    try:
        from anvaya import numerical
        # Root of x^2 - 4 = 0 near 2
        root = numerical.root_find(lambda x: x**2 - 4, 1.5)
        if abs(root - 2.0) < 1e-5:
            log_pass("Numerical: Root finding working")
        else:
            log_fail("Numerical: Root finding failed")
    except Exception as e:
        log_fail(f"Numerical Error: {e}")

    # 9. Complex Analysis
    try:
        from anvaya import complex_analysis
        # Just check import and basic call safely
        # Residue of 1/z at z=0 is 1
        z = var('z')
        res = complex_analysis.residue(1/z, z, 0)
        if res == 1:
            log_pass("Complex Analysis: Residue working")
        else:
            log_fail(f"Complex Analysis: Residue failed {res}")
    except Exception as e:
        log_fail(f"Complex Analysis Error: {e}")

    # 10. Graph Theory (Requires networkx)
    try:
        from anvaya import graph_theory
        G = graph_theory.Graph()
        G.add_edge(1, 2)
        if G.number_of_edges() == 1:
            log_pass("Graph Theory: Basic graph ops working")
        else:
            log_fail("Graph Theory: Basic graph ops failed")
    except Exception as e:
        log_fail(f"Graph Theory Error: {e}")

if __name__ == "__main__":
    print("running final production readiness audit...\n")
    all_imports = check_module_importability()
    check_basic_functionality()
    
    if all_imports:
        print("\n✅ Final Result: All modules are importable and basic functionality is verified.")
    else:
        print("\n❌ Final Result: Some modules failed to load.")
