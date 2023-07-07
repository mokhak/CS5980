# Importing necessary libraries
from typing import Protocol, runtime_checkable

@runtime_checkable
# Specifying protocol for character
# Must have __init__, attack, takeDamage, and ai methods
# Inputs into methods and specific variables also specified in protocol
class CharacterProt(Protocol):
    def __init__(self, aiController:bool):
        self.maxHitPoints
        self.hitPoints
        self.aiController
        pass
    
    def attack(self, attack_type:int) -> int:
        pass
    
    def takeDamage(self, amount: int):
        pass
    
    def ai(self) -> int:
        pass