import pytest
from Task_2 import Fraction

def test_negative_denominator():
    with pytest.raises(ValueError):
        Fraction(1, -1)

def test_initialization():
    f = Fraction(1, 2)

    assert f.numerator == 1
    assert f.denominator == 2

def test_invalid_denominator():
    with pytest.raises(ValueError):
        Fraction(1, 0)


