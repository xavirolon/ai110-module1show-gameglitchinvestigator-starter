import random


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def start_new_game(low: int = 1, high: int = 100):
    """
    Return fresh game state for a new game.

    Resets the guesses/history from the previous game along with attempts,
    secret, and status.
    """
    #FIX: Refactored the start_new_game function from app.py into logic_utils.py using Claude code
    # Updated logic of code so the history of guesses resets when a new game is started, keeping previous game state intact.
    return {
        "attempts": 0,
        "secret": random.randint(low, high),
        "history": [],
        "status": "playing",
    }


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """

    #FIX: Swapped the guessing logic in logic.utilis.py using Claude code
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
