import pytest

from warrior import Warrior

# Using fixture to create new temp object for testing.
@pytest.fixture
def my_warrior():
    warrior = Warrior(False)

    # artificially set max hitpoints
    warrior.maxHitPoints = 20
    warrior.hitPoints = 20
    return warrior

# Taking various damages and checking for proper calculation of health. 
def test_take_damage(my_warrior):
    my_warrior.takeDamage(10)
    assert my_warrior.hitPoints == 10
    
    my_warrior.takeDamage(-200)
    assert my_warrior.hitPoints == 210
    
    my_warrior.takeDamage(10000000)
    assert my_warrior.hitPoints == 0