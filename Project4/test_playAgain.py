import pytest
import battle_sim
import mock


@pytest.fixture

def test_playAgain():

    with mock.patch.object(__builtins__, 'input', lambda: 'yes'):
        assert battle_sim.playAgain() == True
        
    with mock.patch.object(__builtins__, 'input', lambda: 'y'):
        assert battle_sim.playAgain() == True
        
    with mock.patch.object(__builtins__, 'input', lambda: 'no'):
        assert battle_sim.playAgain() == False
        
    with mock.patch.object(__builtins__, 'input', lambda: 'n'):
        assert battle_sim.playAgain() == False
