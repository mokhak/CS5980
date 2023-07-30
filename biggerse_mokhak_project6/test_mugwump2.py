import pytest
from character import Mugwump


@pytest.fixture
def my_mugwump():
    mugwump = Mugwump()

    # artificially set max hitpoints
    mugwump.maxHitPoints = 20
    mugwump.hitPoints = 20
    return mugwump


def test_attack_damage(monkeypatch):
    my_mugwump = Mugwump(is_computer=False)

    # Test player-controlled attack with Razor Sharp Claws
    monkeypatch.setattr('builtins.input', lambda _: '1')
    damage = my_mugwump.attack()
    assert -6 <= damage <= 12  # Damage should be between -6 and 12 (inclusive)

    # Test player-controlled attack with Fangs of Death
    monkeypatch.setattr('builtins.input', lambda _: '2')
    monkeypatch.setattr(my_mugwump.d20, 'roll', lambda: 16)  # Mocking the roll to guarantee a hit
    damage = my_mugwump.attack()
    assert -6 <= damage <= 18  # Damage should be between -6 and 18

    # Test player-controlled healing attack
    monkeypatch.setattr('builtins.input', lambda _: '3')
    damage = my_mugwump.attack()
    assert -6 <= damage <= 6  # Healing value should be between -6 and 6

    # Test computer-controlled attack (miss)
    monkeypatch.setattr(my_mugwump, 'ai', lambda self: 1)
    monkeypatch.setattr(my_mugwump.d20, 'roll', lambda: 12)  # Mocking the roll to guarantee a miss
    damage = my_mugwump.attack()
    assert -6 <= damage <= 6  # Damage should be between -6 and 6


@pytest.mark.parametrize("initial_hp, damage, expected_hp", [
    (10, 5, 5),  # Case 1: Damage less than current HP
    (8, 8, 0),   # Case 2: Damage equal to current HP
    (15, 20, 0),  # Case 3: Damage greater than current HP
    (12, 0, 12),  # Case 4: Damage equal to 0
    (5, 10, 0)   # Case 5: Damage greater than current HP, resulting in 0 HP
])
def test_take_damage(initial_hp, damage, expected_hp):
    # Create a Mugwump object
    mugwump = Mugwump(is_computer=True)

    # Set the initial HP
    mugwump.hitPoints = initial_hp

    # Call the takeDamage method
    mugwump.takeDamage(damage)

    # Verify the resulting HP matches the expected HP
    assert mugwump.hitPoints == expected_hp


def test_ai():
    # Create a Mugwump object
    mugwump = Mugwump(is_computer=True)

    # Test the output of __ai method over multiple iterations
    for _ in range(1000):
        attack_type = mugwump.ai()  # Accessing private method

        # Verify that the attack_type is within the expected range
        assert attack_type in [1, 2, 3]
