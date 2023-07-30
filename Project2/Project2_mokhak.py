# Import libraries and files
from car import Car
import pandas as pd
import sys
import matplotlib.pyplot as plt

# Load JSON file into Dataframe
print('\n================================================\n')
df = pd.read_json('autos.json')
print('Loaded JSON File...')
print('\n================================================\n')

# Create Car Objects
print('Creating Car Objects...')
cars = []
for x in range(len(df)):
    cars.append(Car(df.iloc[x]))
print('Successfully Created Car Objects!')
print('\n================================================\n')

# Set Car Nicknames
print('Set nicknames for 5 cars...')
nicknames = [None]*5
# Ask for user input for all 5 cars
for x in range(len(nicknames)):
    correct_length = False
    while(correct_length == False):
        print('Enter nickname for Car',(x+1))
        nicknames[x] = input()
        # Check to make sure input is greater than 2 characters, if not, show error and try again
        if(len(nicknames[x]) <= 2):
            print("Enter a name greater than 2 characters!")
        else:
            cars[x].nickname = nicknames[x]
            correct_length = True
print('Nicknames set successfully!')
print('\n================================================\n')

# Print out first 5 cars
for x in range(len(nicknames)):
    print('Car',(x+1),'\t','Nickname:',cars[x].nickname,'\t','City MPG:',cars[x].city_mpg,'\t','Price:',cars[x].price)
print('\n================================================\n')

# Calculate Average, Min, and Max Price
print('Calculating Average, Minimum and Maximum Price...')
avg_price = 0
num_avg = 0
min_price = sys.maxsize
max_price = 0

for x in range(len(cars)):
    # Check for null value in the dataset
    # If value is null, do not parse through the loop
    if(pd.isna(cars[x].price) == False):
        # Sum up price and increment counter for demoninator to calculate average
        avg_price += (cars[x].price)
        num_avg += 1
        # Check if price of next car is lower than the previous car, if so, update minimum price
        if(cars[x].price < min_price):
            min_price = cars[x].price
        # Check if price of next car is higher than the previous car, if so, update maximum price
        if(cars[x].price > max_price):
            max_price = cars[x].price
# Calculate average
avg_price = avg_price/num_avg

print("Average Price:",avg_price,"\nMinimum Price:",min_price,"\nMaximum Price:",max_price)
print('\n================================================\n')

# Graph Price vs. Horsepower
print('Plotting Price vs. Horsepower...')
# Generating Scatter plot with price and horsepower data from data frame
plt.scatter(df['price'], df['horsepower'])
# Setting graph labels
plt.title("Price vs. Horsepower")
plt.xlabel("Price")
plt.ylabel("Horsepower")
print('\n================================================\n')
plt.show()