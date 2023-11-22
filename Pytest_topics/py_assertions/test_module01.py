# run - pytest -s -v Pytest_topics/py_assertions/test_module01.py
def test_a0():
    print("This is my first test")
    assert 4 >= 3


def test_a1():
    print("This is my second test")
    assert 1


def test_a2():
    print("This is a failed test")
    assert 3-1*4/2 == 4.0
