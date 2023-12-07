from hypothesis import given, example
from hypothesis.strategies import text
from Hypothesis_examples.funciones.funciones_01 import decode, encode


@given(text())
@example("")
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s


if __name__ == "__main__":
    test_decode_inverts_encode()
