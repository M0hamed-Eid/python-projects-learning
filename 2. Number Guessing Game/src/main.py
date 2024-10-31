# src/main.py

from game_logic import NumberGuessingGame
from utils.input_validation import is_valid_number, is_in_range

def main():
    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100, or type 'exit' to quit.")

    # Initialize the game with default range values
    game = NumberGuessingGame(min_value=1, max_value=100)
    is_game_running = True

    while is_game_running:
        user_input = input("Enter your guess: ")

        # Check if the user wants to exit the game
        if user_input.lower() == "exit":
            print("Thank you for playing! Goodbye!")
            break

        # Validate user input to ensure it is a number and within the game range
        if is_valid_number(user_input):
            guess = int(user_input)
            if is_in_range(guess, game.min_value, game.max_value):
                # Provide feedback for the guess
                feedback = game.check_guess(guess)
                print(feedback)

                # Check if the guess is correct and end the game if so
                if game.is_guess_correct(guess):
                    print("You guessed the number! Game Over!")
                    is_game_running = False
            else:
                print(f"Please enter a number between {game.min_value} and {game.max_value}.")
        else:
            print("Invalid input! Please enter a valid number or type 'exit' to quit.")

if __name__ == "__main__":
    main()
