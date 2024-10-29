# src/operations/basic.py

class BasicOperations:
    """Class for basic arithmetic operations."""

    @staticmethod
    def add(x, y):
        """Returns the sum of x and y."""
        return x + y

    @staticmethod
    def subtract(x, y):
        """Returns the difference of x and y."""
        return x - y

    @staticmethod
    def multiply(x, y):
        """Returns the product of x and y."""
        return x * y

    @staticmethod
    def divide(x, y):
        """Returns the quotient of x and y. Raises ValueError if dividing by zero."""
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y
