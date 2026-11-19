class Fraction:
    def __init__(self, numerator: int, denominator: int)-> None: 
        # Check if numerator is an integer
        if type(numerator) != int:
            raise TypeError("Numerator must be an integer")

        # Check if denominator is an integer
        if type(denominator) != int:
            raise TypeError("Denominator must be an integer")

        # Check if denominator is positive
        if denominator <= 0:
            raise ValueError("Denominator must be a positive integer")

        # Save numerator and denominator
        self.numerator = numerator
        self.denominator = denominator  

    def __eq__(self, other)-> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other : 'Fraction')-> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return self.numerator * other.denominator != self.denominator * other.numerator

    def __lt__(self, other : 'Fraction')-> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other : 'Fraction')-> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other : 'Fraction')-> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other : 'Fraction')-> bool:
        if not isinstance(other, Fraction):
            return NotImplemented

        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __add__(self, other : 'Fraction')-> 'Fraction':
        if not isinstance(other, Fraction):
            return NotImplemented

        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other : 'Fraction')-> 'Fraction':
        if not isinstance(other, Fraction):
            return NotImplemented

        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other : 'Fraction')-> 'Fraction':
        if not isinstance(other, Fraction):
            return NotImplemented

        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)