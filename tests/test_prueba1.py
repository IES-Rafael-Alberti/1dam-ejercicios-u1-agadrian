from prueba1 import suma
import pytest

def test_suma():
    assert suma(1, 1) == 2
    assert suma(0, 0) == 0
    assert suma(100, -100) == 0


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1, 1, 2),
        (0, 0, 0),
        (100, -100, 0),
        (-15, -1, -16),
        (-3, 8, 5),
        (9, suma(-1, -2), 6)
    ]
  )
def test_suma_params(input_n1, input_n2, expected):
    assert suma(input_n1, input_n2) == expected