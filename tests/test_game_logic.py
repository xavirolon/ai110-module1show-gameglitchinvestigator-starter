from logic_utils import check_guess, start_new_game

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_message_matches_direction():
    # Regression test for the swapped-hint bug:
    # a "Too High" guess must tell the player to go LOWER,
    # and a "Too Low" guess must tell the player to go HIGHER.
    high_outcome, high_message = check_guess(60, 50)
    assert high_outcome == "Too High"
    assert "LOWER" in high_message

    low_outcome, low_message = check_guess(40, 50)
    assert low_outcome == "Too Low"
    assert "HIGHER" in low_message


def test_new_game_resets_guesses():
    # Regression test for the New Game bug:
    # starting a new game must clear the guesses/history from the
    # previous game, not just reset attempts and the secret.
    fresh = start_new_game(1, 100)

    assert fresh["history"] == []
    assert fresh["attempts"] == 0
    assert fresh["status"] == "playing"
    assert 1 <= fresh["secret"] <= 100


def test_new_game_respects_difficulty_range():
    # The new secret must fall inside the provided difficulty range.
    fresh = start_new_game(1, 20)
    assert 1 <= fresh["secret"] <= 20
