from typing import Protocol, runtime_checkable

@runtime_checkable
class AnimalAge(Protocol):
    AnimalAge: int
    pass
    
class myAnimals:
    def __init__(self, name, age: int):
        self.name = name
        self.AnimalAge = age

class badAnimal:
    def __init__(self, name):
        self.name = name

rightAnimal = myAnimals("Dog", 3)
wrongAnimal = badAnimal("Cat")

assert isinstance(rightAnimal,AnimalAge)
assert isinstance(wrongAnimal,AnimalAge)