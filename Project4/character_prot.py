from typing import Protocol, runtime_checkable

@runtime_checkable
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