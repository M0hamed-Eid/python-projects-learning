# Number Guessing Game

This project is a command-line-based Number Guessing Game built in Python, intended to enhance skills in loops, conditionals, and modular coding. The game prompts the user to guess a randomly generated number within a range, offering feedback after each guess and allowing them to exit at any time.

## Project Structure

```bash
2. Number Guessing Game/
│
├── src/
│   ├── main.py           # Main game loop and user interaction
│   ├── game_logic.py     # Core game logic and feedback control
│   ├── utils/
│   │   ├── input_validation.py  # Functions for validating user input
│   │   ├── feedback.py         # Feedback on guesses (too high/low)
│   │   └── __init__.py        # Initialize utils module
│   │
│   └── __init__.py      # Initialize src module
│
└── README.md
```

## Features

- **Random Number Generation**: A new random target number is generated for each game.
- **User Feedback**: After each guess, the game provides feedback if the guess is too high, too low, or correct.
- **Input Validation**: Ensures user input is a valid integer and within the allowed range.
- **Exit Option**: The player can exit the game at any time by typing "exit."

## Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/M0hamed-Eid/NumberGuessingGame.git](https://github.com/M0hamed-Eid/python-projects-learning/tree/main/2.%20Number%20Guessing%20Game/src)
   cd NumberGuessingGame

2. Set up and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate
    ```

3. Run the game:
    ```bash
    python -u src/main.py

4. Guess the number by entering a value within the specified range. Type "exit" to quit the game.

## Example Interaction

   ```bash
    Welcome to the Number Guessing Game!
    Guess the number between 1 and 100, or type 'exit' to quit.
    Enter your guess: 50
    Too low! Try a higher number.
    Enter your guess: 75
    Too high! Try a lower number.
    Enter your guess: 62
    Congratulations! You've guessed the correct number!
   ```
   
## Future Enhancements
- **Difficulty Levels**: Introduce multiple difficulty levels with different ranges.
- **Scorekeeping**: Track the number of guesses made by the user.
- **Replay Option**: Allow the user to play multiple rounds without restarting the program.
