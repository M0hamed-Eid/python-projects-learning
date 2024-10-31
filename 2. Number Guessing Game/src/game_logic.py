# src/game_logic.py

import random
from utils.feedback import provide_feedback
from utils.input_validation import is_valid_number, is_in_range

class NumberGuessingGame:
    def __init__(self, min_value=1, max_value=100):
        """
        Initialize the game with a random target number within a specified range.

        Args:
            min_value (int): The minimum value of the range.
            max_value (int): The maximum value of the range.
        """
        self.min_value = min_value
        self.max_value = max_value
        self.target_number = random.randint(self.min_value, self.max_value)

    def check_guess(self, guess):
        """
        Compare the user's guess to the target number and provide feedback.

        Args:
            guess (int): The number guessed by the user.

        Returns:
            str: Feedback message indicating if the guess is too high, too low, or correct.
        """
        return provide_feedback(guess, self.target_number)

    def is_guess_correct(self, guess):
        """
        Determine if the user's guess matches the target number.

        Args:
            guess (int): The number guessed by the user.

        Returns:
            bool: True if the guess is correct, False otherwise.
        """
        return guess == self.target_number
