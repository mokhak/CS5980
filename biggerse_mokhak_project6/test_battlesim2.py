from unittest.mock import patch
from battle_sim2 import playAgain
from battle_sim2 import initiative

# the attackChoice method was moved from battle_sim into character.py
# to be included in the attack methods for both warrior and mugwump classes


def test_initiative():
    result = initiative()
    assert result == 1 or result == 2


def test_play_again():
    # User chooses to play again
    with patch('builtins.input', return_value='yes'):
        assert playAgain() is True

    # User chooses not to play again
    with patch('builtins.input', return_value='no'):
        assert playAgain() is False

    # User provides invalid input
    with patch('builtins.input', return_value='maybe'):
        assert playAgain() is False

