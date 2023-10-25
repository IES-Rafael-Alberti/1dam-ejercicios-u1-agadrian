from tests.prueba1 import numeroMayor
import pytest

def test_numeroMayor():
    assert numeroMayor(1, 1) == 0
    assert numeroMayor(45, 3) == 45
    assert numeroMayor(20, -50) == 20
    assert numeroMayor(20, 100) == 100


@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1, 1, 0),
        (0, 0, 0),
        (100, -100, 100),
        (-15, -1, -1),
        (-3, 8, 8),
    ]
  )
def test_numero_mayor(input_n1, input_n2, expected):
    assert numeroMayor(input_n1, input_n2) == expected