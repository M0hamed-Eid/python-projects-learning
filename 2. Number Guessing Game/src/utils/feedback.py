# src/utils/feedback.py

def provide_feedback(guess, target):
    """
    Provide feedback based on the user's guess in relation to the target number.

    Args:
        guess (int): The number guessed by the user.
        target (int): The target number to guess.

    Returns:
        str: Feedback message indicating if the guess is too high, too low, or correct.
    """
    if guess < target:
        return "Too low! Try a higher number."
    elif guess > target:
        return "Too high! Try a lower number."
    else:
        return "Congratulations! You've guessed the correct number!"
