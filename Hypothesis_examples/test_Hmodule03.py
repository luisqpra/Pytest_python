from hypothesis import (event, given,
                        assume, strategies as st,
                        target, settings)
from math import isnan


# Test parametrizados
@given(st.integers().filter(lambda x: x % 2 == 0))
def test_even_integers(i):
    event(f"i mod 3 = {i%3}")


# Asumir condiciones de los parametros
@given(st.floats())
def test_negation_is_self_inverse_for_non_nan(x):
    assume(not isnan(x))
    assert x == -(-x)


# Generación de ejemplos específicos
@settings(max_examples=500)  # Maximo de pruebas
@given(st.integers(0, 10), st.integers(0, 20), st.integers(0, 25))
def test_associativity_with_target(a, b, c):
    ab_c = (a + b) + c
    a_bc = a + (b + c)
    difference = abs(ab_c - a_bc)
    target(difference)  # Without this, the test almost always passes
    assert difference == 0
