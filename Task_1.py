

class Temperature:
    # Skal ta imot alle typer, og sjekke om de er gyldige
    def __init__(self, value, unit):
        #Bokstaven må være stor
        unit = unit.upper()
        #Sjeeker om enheten er riktig
        if unit not in ["C", "F", "K"]:
            raise ValueError("Unit must be 'C', 'F', or 'K'")
        if value < 0 and unit == "K":
            raise ValueError("Temperature cannot be below absolute zero")
        self.value = value
        self.unit = unit