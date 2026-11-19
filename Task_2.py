class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        # Check if numerator is an integer
        if not isinstance(numerator, int):
            raise TypeError("Numerator must be an integer")

        # Check if denominator is an integer
        if not isinstance(denominator, int):
            raise TypeError("Denominator must be an integer")

        # Check if denominator is positive
        if denominator <= 0:
            raise ValueError("Denominator must be a positive integer")

        # Save numerator and denominator
        self.numerator = numerator
        self.denominator = denominator  