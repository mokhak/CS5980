import battle_sim
import random

def test_initiative_seed_100():
    random.seed(100)
    assert battle_sim.initiative() == 2

def test_initiative():
    random.seed(10000000000)
    assert battle_sim.initiative() == 1