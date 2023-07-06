import battle_sim
import random

def test_initiative():
    random.seed(1)
    
    assert(battle_sim.initiative() == 2)
