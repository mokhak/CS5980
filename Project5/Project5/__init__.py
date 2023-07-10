# Importing necessary libraries
import argparse

# Creating calculator class
class Calculator:
    # Initializing class with both numbers, operator, and result variables
    def __init__(self, number1, number2, operator, result):
        self.number1 = float(number1)
        self.number2 = float(number2)
        self.operator = operator
        self.result = float(result)
    
    # Creating class method to do operation and store results in result variable
    def calculate(self):
        match self.operator:
            case "+":
                self.result = self.number1 + self.number2
            case "-":
                self.result = self.number1 - self.number2
            case "X":
                self.result = self.number1 * self.number2
            case "/":
                self.result = self.number1 / self.number2
            case "%":
                self.result = self.number1 % self.number2
            case "^":
                self.result = self.number1 ** self.number2
                
# Method to check if user entered value is a float or not
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Method to check if user entered a valid operator 
def checkOperator(operator):
    if(operator == "+") or (operator == "-") or (operator == "/") or (operator == "X") or (operator == "%") or (operator == "^"):
        return True
    else:
        return False

# Method to check all user entered inputs and print out error message
def errorCheck(number1, number2, operator):
    if(isFloat(number1) == False):
        print("Enter a numeric value for number 1!")
        return False
    elif(isFloat(number2) == False):
        print("Enter a numeric value for Number 2!")
        return False
    elif(checkOperator(operator) == False):
        print("Enter a valid operator!")
        return False
    else:
        return True
        
# Main method to run code
def main():
    
    # Creating a new Calculator from Class
    new_calc = Calculator(0, 0, None, 0)
    
    # Create variable to track error
    tmpError = False
    
    # Parsing arguments entered by the user
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="Number 1")
    parser.add_argument("operator", help="Operation")
    parser.add_argument("number2", help="Number 2")
    args = parser.parse_args()
    tmpError = errorCheck(args.number1, args.number2, args.operator)
    
    # Only run calculation if there are no errors with what user has entered
    # If calculation is successful, then print out result
    if tmpError:
        new_calc.number1 = float(args.number1)
        new_calc.number2 = float(args.number2)
        new_calc.operator = args.operator
        new_calc.calculate()
        
        print(f"The result is {new_calc.result}")