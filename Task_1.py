

class Temperature:
    # Skal ta imot alle typer, og sjekke om de er gyldige
    def __init__(self, value: float, unit: str = "C"):
        #Bokstaven må være stor
        unit = unit.upper()
        #Sjeeker om enheten er riktig
        if unit not in ["C", "F", "K"]:
            raise ValueError("Unit must be 'C', 'F', or 'K'")
        if value < 0 and unit == "K":
            raise ValueError("Temperature cannot be below absolute zero")
        self.value = value
        self.unit = unit

    # "Use a tolerance of 1e-9 for floating-point value comparisons"
    def tolerance(self, other: Temperature) -> bool:
        # Hvis other ikke er en temp sender den feilmelding
        if not isinstance(other, Temperature):
            return NotImplemented
        #transformerer dem til celsius. Enklere å sammenligne dem da
        self_celsius = self.to_celsius()
        other_celsius = other.to_celsius()
        return abs(self_celsius - other_celsius) <= 10e-9

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
        #Gjør om target_unit til stor bokstav
        target_unit = target_unit.upper()
        #Gjør omtrent det samme som i init, men for target_unit. (Høre med lærer om det er riktig)
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

    #Skal sammenligne to temperaturer på tvers av enheter
    def compare(self, other: Temperature) -> int:
        if not isinstance(other, Temperature):
            return NotImplemented
        #gjør om begge temperaturene til celsius for å sammenligne dem
        self_celsius = self.to_celsius()
        other_celsius = other.to_celsius()
        #sammenligner dem og returnerer svaret
        if self_celsius < other_celsius:
            return f"{self} is less than {other}"
        elif self_celsius > other_celsius:
            return f"{self} is greater than {other}"
        else:
            return f"{self} is equal to {other}"