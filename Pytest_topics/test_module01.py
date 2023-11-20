def test_a0():
    print("This is my first test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1


def test_a1():
    assert 5 + 5 == 10
    # No es recomendado tener varios assert en  una misma funcion test
    assert 5 - 5 == 0  # esto es solo pro practiva
    assert 5 * 5 == 25
    assert 5 / 5 == 1


def test_a2():
    assert 9/5 == 1.5, "failed test intencionalmente"


# test no.3
def test_a3():
    assert 9//5 == 1
