import pytest
from Task_2 import Fraction

def test_negative_denominator()-> None:
    with pytest.raises(ValueError):
        Fraction(1, -1)

def test_initialization()-> None:
    f = Fraction(1, 2)

    assert f.numerator == 1
    assert f.denominator == 2

def test_invalid_denominator()-> None:
    with pytest.raises(ValueError):
        Fraction(1, 0)

def test_invalid_denominator_type()-> None:
    with pytest.raises(TypeError):
        Fraction(1, "a")

def test_invalid_numerator_type()-> None:
    with pytest.raises(TypeError):
        Fraction("a", 1)

def test_addition()-> None:
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    result = f1 + f2

    assert result.numerator == 5
    assert result.denominator == 6

def test_subtraction()-> None:
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    result = f1 - f2

    assert result.numerator == 1
    assert result.denominator == 6

def test_multiplication() -> None:
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    result = f1 * f2

    assert result.numerator == 1
    assert result.denominator == 6

def test_division() -> None:
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    result = f1 / f2

    assert result.numerator == 3
    assert result.denominator == 2

def test_division_by_zero() -> None:
    f1 = Fraction(1, 2)
    f2 = Fraction(0, 3)

    with pytest.raises(ZeroDivisionError):
        f1 / f2

def test_equality() -> None:
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)

    assert f1 == f2

def test_inequality() -> None:
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)

    assert f1 != f2

def test_less_than() -> None:
    assert Fraction(1, 2) < Fraction(3, 4)


def test_less_than_or_equal() -> None:
    assert Fraction(1, 2) <= Fraction(2, 4)


def test_greater_than() -> None:
    assert Fraction(3, 4) > Fraction(1, 2)


def test_greater_than_or_equal() -> None:
    assert Fraction(2, 4) >= Fraction(1, 2)


