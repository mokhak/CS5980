import battle_sim

# Set input values to both options and check for expected output.
def test_attackChoice_1(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _:"1")
    assert int(battle_sim.attackChoice()) == 1
    
def test_attackChoice_2(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _:"2")
    assert int(battle_sim.attackChoice()) == 2