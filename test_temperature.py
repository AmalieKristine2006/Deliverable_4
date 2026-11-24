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

def test_conversion_accuracy_absolute_zero():
    t_c = Temperature(-273.15, "C")
    t_f = Temperature(-459.67, "F")
    t_k = Temperature(0, "K")
    # absolute zero-test
    assert t_c.to_celsius() == t_f.to_celsius() == t_k.to_celsius()

def test_conversion_accuracy_Celsius_Fahrenheit():
    # Celsius–Fahrenheit crossover 
    t_c = Temperature(-40, "C")
    t_f = Temperature(-40, "F")
    t_k = Temperature(233.15, "K")
    assert t_c.to_fahrenheit() == t_f.to_fahrenheit() == t_k.to_fahrenheit()

def test_conversion_accuracy_Freezing_Point():
    # Freezing point of water
    t_c = Temperature(0, "C")
    t_f = Temperature(32, "F")
    t_k = Temperature(273.15, "K")
    assert t_c.to_kelvin() == t_f.to_kelvin() == t_k.to_kelvin()

def test_conversion_accuracy_Human():
    # Human body temperature
    t_c = Temperature(37, "C")
    t_f = Temperature(98.6, "F")
    t_k = Temperature(310.15, "K")
    assert t_c.to_celsius() == t_f.to_celsius() == t_k.to_celsius()

def test_conversion_accuracy_Boiling_Point():
    # Boiling point of water
    t_c = Temperature(100, "C")
    t_f = Temperature(212, "F")
    t_k = Temperature(373.15, "K")
    assert t_c.to_kelvin() == t_f.to_kelvin() == t_k.to_kelvin()

# Round-trip conversion tests
def test_round_trip_conversion_C_to_F_to_K_to_C():
    t_c = Temperature(25, "C")
    t_f = Temperature(t_c.to_fahrenheit(), "F")
    t_k = Temperature(t_f.to_kelvin(), "K")
    assert t_k.to_celsius() == pytest.approx(t_c.to_celsius(), rel=1e-9)

#Cross-unit comparisons:
def test_cross_unit_comparisons():
    t1 = Temperature(0, "C")
    t2 = Temperature(32, "F")
    t3 = Temperature(273.15, "K")
    assert t1 == t2 == t3

# FOrmatting test
def test_formatting():
    t = Temperature(25, "C")
    assert str(t) == "25.00 C"
    assert repr(t) == "Temperature(25.0, C)"
