# src/calculator.py

from operations.basic import BasicOperations
from operations.advanced import AdvancedOperations
from operations.scientific import ScientificOperations
from utils.input_validation import is_number

class Calculator:
    """Main calculator class that utilizes various operation classes."""

    def __init__(self):
        # Initialize instances of operation classes
        self.basic_ops = BasicOperations()
        self.advanced_ops = AdvancedOperations()
        self.scientific_ops = ScientificOperations()

    def perform_basic_operation(self, operation, x, y):
        """Performs a basic operation based on the provided operation name."""
        if operation == "add":
            return self.basic_ops.add(x, y)
        elif operation == "subtract":
            return self.basic_ops.subtract(x, y)
        elif operation == "multiply":
            return self.basic_ops.multiply(x, y)
        elif operation == "divide":
            return self.basic_ops.divide(x, y)
        else:
            raise ValueError("Unsupported basic operation")

    def perform_scientific_operation(self, operation, angle):
        """Performs a scientific operation based on the provided operation name."""
        if operation == "sin":
            return self.scientific_ops.sin(angle)
        elif operation == "cos":
            return self.scientific_ops.cos(angle)
        elif operation == "tan":
            return self.scientific_ops.tan(angle)
        else:
            raise ValueError("Unsupported scientific operation")
    
    def perform_advanced_operation(self, operation, base, *args):
        """Performs an advanced operation based on the provided operation name."""
        if operation == "power":
            return self.advanced_ops.power(base, *args)
        elif operation == "root":
            return self.advanced_ops.root(base, *args)
        elif operation == "logarithm":
            return self.advanced_ops.logarithm(base, *args)
        else:
            raise ValueError("Unsupported advanced operation")