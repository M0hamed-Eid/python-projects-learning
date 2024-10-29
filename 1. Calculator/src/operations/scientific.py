# src/operations/scientific.py

import math

class ScientificOperations:
    """Class for scientific operations like trigonometric functions."""

    @staticmethod
    def sin(angle):
        """Returns the sine of the given angle (in degrees)."""
        return math.sin(math.radians(angle))

    @staticmethod
    def cos(angle):
        """Returns the cosine of the given angle (in degrees)."""
        return math.cos(math.radians(angle))

    @staticmethod
    def tan(angle):
        """Returns the tangent of the given angle (in degrees). Raises ValueError if angle is 90 + n*180."""
        if (angle % 180) == 90:
            raise ValueError("Tangent is undefined for angles of 90 + n*180 degrees.")
        return math.tan(math.radians(angle))
