from die2 import Die
import random


def test_die_constructor():
    random.seed(1)  # Set the seed to ensure predictable results

    # Number of sides less than 2
    die1 = Die(1)
    assert die1._Die__numberSides == 6  # Private attribute set to 6

    # Number of sides greater than 100
    die2 = Die(150)
    assert die2._Die__numberSides == 6

    # Number of sides within valid range
    die3 = Die(10)
    assert die3._Die__numberSides == 10


def test_die_roll():
    random.seed(1)  # Set the seed to ensure predictable results

    # Roll a die with 6 sides
    die1 = Die(6)
    for _ in range(100):
        result1 = die1.roll()
        assert 1 <= result1 <= 6  # Check if the result is within the valid range

    # Roll a die with 20 sides
    die2 = Die(20)
    for _ in range(100):
        result2 = die2.roll()
        assert 1 <= result2 <= 20

    # Roll a die with 10 sides
    die3 = Die(10)
    for _ in range(100):
        result3 = die3.roll()
        assert 1 <= result3 <= 10
