# Import Libraries
import json

def combinedMPG_calc(car_index, data_frame, city_driving):
    return ( ( float(city_driving) * (data_frame[int(car_index)]['city-mpg']) ) + ( ( 100 - float(city_driving) ) * (data_frame[int(car_index)]['highway-mpg']) ) ) / 100

def main():
    # Import .json file and load data
    f = open('autos.json')
    data = json.load(f)
    print("File Imported")
    f.close()

    # Print Number of Cars
    print("Number of Cars in file:", len(data))

    # Print out full list of Cars
    for x in range(len(data)):
        print("Index:", x, "| Aspiration:", data[x]['aspiration'], "| Body Style:", data[x]['body-style'])
        
    # Ask User Feedback about what car they want to view
    while(1):
        Car_Index = input("Enter the index of the car you'd like to view: ")
        if(int(Car_Index) < len(data)):
            print(data[int(Car_Index)])
            break
        else:
            print("Error! Enter a valid value!")

    # Ask User Feedback about percentage of city driving 
    while(1):
        City_Driving = input("Enter percentage of city driving (between 0 and 100): ")
        if(float(City_Driving) <= 100):
            print("Combined mileage for the car picked:", combinedMPG_calc(Car_Index,data,City_Driving))
            break
        else:
            print("Error! Enter a valid value!") 
        
    # Calculate Average City and Highway MPG for all cars
    print("Calculating Average City and Highway MPG for all cars...")
    
    City_Sum = 0
    Highway_Sum = 0
    for x in range(len(data)):
        City_Sum += int(data[x]['city-mpg'])
        Highway_Sum += int(data[x]['highway-mpg'])
    City_Avg = City_Sum/int(len(data))
    Highway_Avg = Highway_Sum/int(len(data))
    
    print("Average Highway MPG of all cars is", Highway_Avg, "and Average City MPG of all cars is", City_Avg)
    print("City MPG of your car is", data[int(Car_Index)]['city-mpg'])
    
    if( (int(data[int(Car_Index)]['city-mpg'])) < City_Avg ):
        print("The car you picked has less City MPG than average.")
    elif( (int(data[int(Car_Index)]['city-mpg'])) == City_Avg ):
        print("The car you picked has same City MPG as average.")
    else:
        print("The car you picked has greater City MPG than average.")
    

    
if __name__ == "__main__":
    main()