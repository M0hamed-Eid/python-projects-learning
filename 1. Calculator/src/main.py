# main.py
"""
This is the entry point for the calculator application.
Prompts the user to choose an operation type and processes inputs accordingly.
"""

# Import necessary classes
from operations.basic import BasicOperations
from operations.advanced import AdvancedOperations
from operations.scientific import ScientificOperations
from utils.input_validation import is_number

def main():
    # Initialize classes
    basic_ops = BasicOperations()
    advanced_ops = AdvancedOperations()
    scientific_ops = ScientificOperations()
    
    # Display menu
    print("Welcome to the Complex Calculator!")
    print("Choose an operation type: [1] Basic [2] Advanced [3] Scientific")
    # More code will follow...

if __name__ == "__main__":
    main()
