import pytest
from die import Die
import random

random.seed(1)

@pytest.fixture
def my_die():
    die = Die(3)
    return die

def test_die(my_die):
    my_die.roll()
    assert my_die.currentValue == 3
    
    my_die.roll()
    assert my_die.currentValue == 1
    
    my_die.roll()
    assert my_die.currentValue == 2