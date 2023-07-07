import battle_sim
from pytest import MonkeyPatch

def test_attackChoice1():
    MonkeyPatch.setattr("builtins.input", lambda _:"1")
    i = battle_sim.attackChoice()
    assert int(i) == 1