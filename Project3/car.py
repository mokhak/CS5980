# Importing Abstract Base Vehicle Class
from vehicle import Vehicle

# Creating Plane class by inheriting from Vehicle base class
class Car(Vehicle):
    
    # Inheriting all attributes from Base Vehicle Class and adding horsepower attribute
    def __init__(self, name, fuel_capacity, mpg, passengers, horsepower):
        super().__init__(name, fuel_capacity, mpg, passengers)
        self.horsepower = horsepower
        
    # Creating getRange method to return product of Fuel Capacity and MPG
    def getRange(self) -> float:
        return float(self.fuel_capacity)*float(self.mpg)