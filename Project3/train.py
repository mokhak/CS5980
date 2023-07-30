# Importing Abstract Base Vehicle Class
from vehicle import Vehicle

# Creating Train class by inheriting from Vehicle base class
class Train(Vehicle):
    
    # Inheriting all attributes from Base Vehicle Class and adding railType attribute 
    def __init__(self, name, fuel_capacity, mpg, passengers, railType):
        super().__init__(name, fuel_capacity, mpg, passengers)
        self.railType = railType
        
    # Creating getRange method to return product of Fuel Capacity and MPG
    def getRange(self) -> float:
        return float(self.fuel_capacity)*float(self.mpg)