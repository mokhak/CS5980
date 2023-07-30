# Importing necessary libraries
from typing import Protocol, runtime_checkable

@runtime_checkable
# Specifying protocol for character
# Must have __init__, attack, takeDamage, and ai methods
# Inputs into methods and specific variables also specified in protocol
class CharacterProt(Protocol):
    def __init__(self, is_computer):
        self.nickname
        self.maxHitPoints
        self.hitPoints
        self.is_computer
        pass
    
    def attack(self):
        pass
    
    def takeDamage(self, amount: int):
        pass
    
    def ai(self) -> int:
        pass