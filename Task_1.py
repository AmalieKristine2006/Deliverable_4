

class Temperature:
    # Should be able to take any temperature value and unit and check wheter it is an approved unit and value
    def __init__(self, value: float, unit: str = "C"):
        #The unit needs to be uppercase
        unit = unit.upper()
        #Checks that the unit is correct
        if unit not in ["C", "F", "K"]:
            raise ValueError("Unit must be 'C', 'F', or 'K'")
        if value < 0 and unit == "K":
            raise ValueError("Temperature cannot be below absolute zero")
        if value < -273.15 and unit == "C":
            raise ValueError("Temperature cannot be below absolute zero")
        if value < -459.67 and unit == "F":
            raise ValueError("Temperature cannot be below absolute zero")
        self._value = value
        self._unit = unit

    # "Use a tolerance of 1e-9 for floating-point value comparisons"
    def tolerance(self, other: Temperature) -> bool:
        # If other isnt a temp it sends an errormessage
        if not isinstance(other, Temperature):
            return NotImplemented
        #transform the temps to celsius so that they are easier to compare
        self_celsius = self.to_celsius()
        other_celsius = other.to_celsius()
        return abs(self_celsius - other_celsius) <= 1e-9

    def __eq__(self, other):
        # Uses the tolerancefunction automatically when comparing temps
        return self.tolerance(other)

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    
    def to_celsius(self):
        if self.unit == "C":
            return self.value
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9
        elif self.unit == "K":
            return self.value - 273.15

    def to_fahrenheit(self):
        if self.unit == "C":
            return (self.value * 9 / 5) + 32
        elif self.unit == "F":
            return self.value
        elif self.unit == "K":
            return (self.value - 273.15) * 9 / 5 + 32

    def to_kelvin(self):
        if self.unit == "C":
            return self.value + 273.15
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9 + 273.15
        elif self.unit == "K":
            return self.value

    def convert_to(self, target_unit: str) -> Temperature:
        #Make target_unit an uppercase letter
        target_unit = target_unit.upper()
        #Does about the same as init, but for target_unit
        if target_unit not in ["C", "F", "K"]:
            raise ValueError("Target unit must be 'C', 'F', or 'K'")
        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")
        elif target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")
        elif target_unit == "K":
            return Temperature(self.to_kelvin(), "K")

    # "Returns an unambiguous representation"
    def __repr__(self) -> str :
        return f"Temperature({self.value}, {self.unit})"

    # "Returns a human-readable string"
    def __str__(self) -> str:
        return f"{self.value:.2f} {self.unit}"

    #Compares units despite being of differnt units
    def compare(self, other: Temperature) -> int:
        if not isinstance(other, Temperature):
            return NotImplemented
        #Turns them both into celsius to compare them
        self_celsius = self.to_celsius()
        other_celsius = other.to_celsius()
        #Compares and returns the answer
        if self.tolerance(other):
            return f"{self} is equal to {other}"
        elif self_celsius < other_celsius:
            return f"{self} is less than {other}"
        else:
            return f"{self} is greater than {other}"