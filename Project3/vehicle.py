# Importing Abstract Base Class
from abc import ABC, abstractmethod

# Creating abstract base class for Vehicle
class Vehicle(ABC):

    # Initializing attributes in base class
    def __init__(self, name, fuel_capacity, mpg, passengers):
        self.name = name
        self.fuel_capacity = fuel_capacity
        self.mpg = mpg
        self.passengers = passengers
    
    # Creating an abstract method that can be overwritten by the actual class
    @property
    @abstractmethod
    def getRange(self) -> float:
        pass