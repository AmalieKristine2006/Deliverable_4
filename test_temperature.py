from Task_1 import Temperature
import pytest

def default_unit_test():
    t = Temperature(25)
    assert t.unit == "C"

default_unit_test()

def test_caseinsensitive_unit():
    t1 = Temperature(25, "c")
    t2 = Temperature(25, "C")
    assert t1 == t2

def test_read_only_behavior():
    t = Temperature(25, "C")
    with pytest.raises(AttributeError):
        t.value = 30
    with pytest.raises(AttributeError):
        t.unit = "F"

test_read_only_behavior()

def test_invalid_strings():
    with pytest.raises(ValueError):
        Temperature(25, "X")
    with pytest.raises(ValueError):
        Temperature(25, "Celcius")
    with pytest.raises(ValueError):
        Temperature(25, "Fahrenheit")
    with pytest.raises(ValueError):
        Temperature(25, "Kelvin")

def test_temp_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-10, "K")
    with pytest.raises(ValueError):
        Temperature(-300, "C")
    with pytest.raises(ValueError):
        Temperature(-500, "F")


test_temp_below_absolute_zero() 

