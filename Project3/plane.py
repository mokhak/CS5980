# Importing Abstract Base Vehicle Class
from vehicle import Vehicle

# Creating Plane class by inheriting from Vehicle base class
class Plane(Vehicle):
    
    # Inheriting all attributes from Base Vehicle Class
    def __init__(self, name, fuel_capacity, mpg, passengers):
        super().__init__(name, fuel_capacity, mpg, passengers)
    
    # Creating getRange method that return product of Fuel Capacity and MPG but reserves 10% of Fuel for takeoff
    def getRange(self) -> float:
        fuel_post_takeoff = float(self.fuel_capacity) - (0.1 * float(self.fuel_capacity))
        return fuel_post_takeoff*float(self.mpg)