# src/utils/input_validation.py

def is_number(value):
    """Checks if the provided value can be converted to a float. Returns True if it can, False otherwise."""
    try:
        float(value)
        return True
    except ValueError:
        return False
