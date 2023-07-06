import battle_sim
import mock

def test_attackChoice1():
    with mock.patch.object(__builtins__, 'input', lambda: '1'):
        assert battle_sim.attackChoice() == 1
        
def test_attackChoice2():
    with mock.patch.object(__builtins__, 'input', lambda: '1'):
        assert battle_sim.attackChoice() == 2