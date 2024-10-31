# src/utils/input_validation.py

def is_valid_number(input_str):
    """
    Check if the input string represents a valid integer.

    Args:
        input_str (str): The input provided by the user.

    Returns:
        bool: True if the input is a valid integer, False otherwise.
    """
    try:
        int(input_str)
        return True
    except ValueError:
        return False


def is_in_range(number, min_value, max_value):
    """
    Check if a number is within a specified range.

    Args:
        number (int): The number to check.
        min_value (int): The minimum allowed value.
        max_value (int): The maximum allowed value.

    Returns:
        bool: True if the number is within range, False otherwise.
    """
    return min_value <= number <= max_value
