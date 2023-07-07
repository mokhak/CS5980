import pytest
from die import Die
import random

#set seed
random.seed(1)

# Using fixture to create new temp die object for testing
@pytest.fixture
def my_die():
    die = Die(3)
    return die

# Testing with multiple rolls. Values should always remain same due to set seed. 
def test_die(my_die):
    my_die.roll()
    assert my_die.currentValue == 3
    
    my_die.roll()
    assert my_die.currentValue == 1
    
    my_die.roll()
    assert my_die.currentValue == 2