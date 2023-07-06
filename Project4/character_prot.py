from typing import Protocol, runtime_checkable

@runtime_checkable
class CharacterProt(Protocol):
    def __init__(self, aiController:bool):
        pass
    
    def attack(self, attack_type:int) -> int:
        pass
    
    def takeDamage(self, amount: int):
        pass