# src/operations/advanced.py

import math

class AdvancedOperations:
    """Class for advanced mathematical operations."""

    @staticmethod
    def power(base, exponent):
        """Returns the result of base raised to the power of exponent."""
        return math.pow(base, exponent)

    @staticmethod
    def root(number, degree=2):
        """Returns the root of a given number. Default is square root if degree is not specified."""
        if degree == 0:
            raise ValueError("Degree of root cannot be zero.")
        return number ** (1 / degree)

    @staticmethod
    def logarithm(number, base=10):
        """Returns the logarithm of a number to a given base. Default base is 10."""
        if number <= 0:
            raise ValueError("Logarithm input must be greater than zero.")
        return math.log(number, base)
