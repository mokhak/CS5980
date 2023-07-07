import battle_sim

# Trying multiple ways to enter yes and no and checking for expected bool value. 
def test_playAgain(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _:"yes")
    assert battle_sim.playAgain() == True
    
    monkeypatch.setattr("builtins.input", lambda _:"y")
    assert battle_sim.playAgain() == True
    
    monkeypatch.setattr("builtins.input", lambda _:"no")
    assert battle_sim.playAgain() == False
    
    monkeypatch.setattr("builtins.input", lambda _:"n")
    assert battle_sim.playAgain() == False