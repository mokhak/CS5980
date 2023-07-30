# Importing classes from relevant files
from car import Car
from train import Train
from plane import Plane

# Importing Duck Typing relevant items
from typing import Protocol, runtime_checkable

# Specifying vehicle protocol
@runtime_checkable
class VehicleProtocol(Protocol):
    
    # All vehicles should have these basic parameters inherited from the Vehicle Abstract Base Class
    def __init__(self, name, fuel_capacity, mpg, passengers):
        super().__init__(name, fuel_capacity, mpg, passengers)
    
    # All vehicles should have a getRange function
    def getRange(self):
        pass

# Prints out a long string of equals sign to format output better
def divider():
    print("\n========================================\n")

# Takes user_input and tries to convert it to an Integer
# Returns False if is unable to convert to Integer 
def error_check(user_input):
    try:
        int(user_input)
    except ValueError:
        return False

# Main Function Definition
if __name__ == "__main__":
    
    # Empty list to store all created vehicles
    list_vehicle = []
    
    # Variable to track whether user is finished entering all vehicles
    is_done = False
    
    # While loop to get user feedback on entering vehicles until user specifies that they are finished
    while(is_done  == False):
        divider()
        print("What kind of vehicle would you like to create?\
                \nEnter 1 for Car\
                \nEnter 2 for Train\
                \nEnter 3 for Plane\
                \nEnter 4 if Complete")
        divider()
        
        user_input = input()
        
        # Print error if user does not enter a valid number
        if(error_check(user_input) == False):
            divider()
            print("Invalid value entered! Try again!")
            
        # Print error if user does not enter a number between 1 and 4
        elif((int(user_input) > 4) and (int(user_input) < 1)):
            divider()
            print("Please enter a value between 1 and 4! Try again!") 
            
        # Set variable to end while loop if user indicates that they are finished
        elif(int(user_input) == 4):
            is_done = True          
            
        # Ask user to enter more information about the vehicle that they want to create
        else:
            
            # Standard information across all vehicles
            divider()
            name = input("Enter Name for your Vehicle: ")
            divider()
            fuel_capacity = input("Enter Fuel Capacity for your Vehicle: ")
            divider()
            mpg = input("Enter MPG for your Vehicle: ")
            divider()
            passengers = input("Enter number of Passenger for your Vehicle: ")
            divider()
            
            # Case specific information based on type of vehicle
            match int(user_input):
                case 1:
                    horsepower = input("Enter horsepower for your Vehicle: ")
                    divider()
                    new_car = Car(name, fuel_capacity, mpg, passengers, horsepower)
                    print(f"Car {new_car.name} created!")
                    list_vehicle.append(new_car)
                
                case 2:
                    railType = input("Enter rail type for your Vehicle: ")
                    divider()
                    new_train = Train(name, fuel_capacity, mpg, passengers, railType)
                    print(f"Train {new_train.name} created!")
                    list_vehicle.append(new_train)
                    
                case 3:
                    new_plane = Plane(name, fuel_capacity, mpg, passengers)
                    print(f"Plane {new_plane.name} created!")
                    list_vehicle.append(new_plane)
    
    divider()    
    
    # Print out range of each vehicle in the list after user is finished
    for x in range(len(list_vehicle)):
        
        # Check to make sure vehicle in list meets Protocol otherwise assert error
        assert isinstance(list_vehicle[x], VehicleProtocol)
        
        # Set vehicle type based on class type from the list of vehicles
        vehicle_type = ""
        if(type(list_vehicle[x]) is Car):
            vehicle_type = "Car"
        elif(type(list_vehicle[x]) is Train):
            vehicle_type = "Train"
        else:
            vehicle_type = "Plane"

        print(f"{list_vehicle[x].name} {vehicle_type}'s range is {list_vehicle[x].getRange()}")
        
    divider()
        
