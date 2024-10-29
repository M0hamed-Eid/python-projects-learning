# src/main.py

from calculator import Calculator
from utils.input_validation import is_number

def main():
    calculator = Calculator()
    print("Welcome to the Complex Calculator!")
    operation_type = input("Choose an operation type: [1] Basic [2] Advanced [3] Scientific\n")

    if operation_type == "1":  # Basic Operations
        print("Available basic operations: add, subtract, multiply, divide")
        operation = input("Enter the basic operation (add, subtract, multiply, divide):\n").lower()
        x = input("Enter the first number:\n")
        y = input("Enter the second number:\n")

        # Validate inputs
        if not (is_number(x) and is_number(y)):
            print("Invalid input. Please enter valid numbers.")
            return
        
        # Convert inputs to float
        x, y = float(x), float(y)
        result = calculator.perform_basic_operation(operation, x, y)
        print(f"Result: {result}")

    elif operation_type == "2":  # Advanced Operations 
        print("Available advanced operations: power, root, logarithm")
        operation = input("Enter the advanced operation (power, root, logarithm):\n").lower()
        base = input("Enter the base number:\n")

        # Validate input
        if not is_number(base):
            print("Invalid input. Please enter a number.")
            return
        base = float(base)

        if operation == "power":
            exponent = input("Enter the exponent:\n")
            if not is_number(exponent):
                print("Invalid exponent. Please enter a number.")
                return
            result = calculator.perform_advanced_operation(operation, base, float(exponent))
        
        elif operation == "root":
            degree = input("Enter the degree (default is 2 for square root):\n") or 2
            if not is_number(degree):
                print("Invalid degree. Please enter a number.")
                return
            result = calculator.perform_advanced_operation(operation, base, float(degree))
        
        elif operation == "logarithm":
            log_base = input("Enter the logarithm base (default is 10):\n") or 10
            if not is_number(log_base):
                print("Invalid base. Please enter a number.")
                return
            result = calculator.perform_advanced_operation(operation, base, float(log_base))
        
        else:
            print("Invalid operation.")
            return
        
        print(f"Result: {result}")

    elif operation_type == "3":  # Scientific Operations
        print("Available scientific operations: sine, cosine, tangent")
        operation = input("Enter the scientific operation (sin, cos, tan):\n").lower()
        angle = input("Enter the angle in degrees:\n")

        # Validate input
        if not is_number(angle):
            print("Invalid angle. Please enter a number.")
            return

        # Convert input to float
        angle = float(angle)
        result = calculator.perform_scientific_operation(operation, angle)
        print(f"Result: {result}")

    else:
        print("Please select a valid operation type.")

if __name__ == "__main__":
    main()
