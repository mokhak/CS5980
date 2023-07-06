import pytest

from mugwump import Mugwump


@pytest.fixture
def my_mugwump():
    mugwump = Mugwump(False)

    # artificially set max hitpoints
    mugwump.maxHitPoints = 20
    mugwump.hitPoints = 20
    return mugwump


def test_take_damage(my_mugwump):
    # we use the fixture function to create the my_mugwump object
    # mugwump = Mugwump()
    # artificially set max hitpoints
    # mugwump.maxHitPoints = 20
    # mugwump.hitPoints = 20

    my_mugwump.takeDamage(5)

    assert (my_mugwump.hitPoints == 15)

    my_mugwump.takeDamage(-100)  # over heal

    assert (my_mugwump.hitPoints == 20)

    my_mugwump.takeDamage(2000000)

    assert (my_mugwump.hitPoints == 0)



