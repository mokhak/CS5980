import argparse

class Calculator:
    def __init__(self, number1, number2, operator, result):
        self.number1 = float(number1)
        self.number2 = float(number2)
        self.operator = operator
        self.result = float(result)
    
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
                

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def checkOperator(operator):
    if(operator == "+") or (operator == "-") or (operator == "/") or (operator == "X") or (operator == "%") or (operator == "^"):
        return True
    else:
        return False

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
        

def main():
    
    new_calc = Calculator(0, 0, None, 0)
    tmpError = False
    
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="Number 1")
    parser.add_argument("operator", help="Operation")
    parser.add_argument("number2", help="Number 2")
    args = parser.parse_args()
    tmpError = errorCheck(args.number1, args.number2, args.operator)
    
    if tmpError:
        new_calc.number1 = float(args.number1)
        new_calc.number2 = float(args.number2)
        new_calc.operator = args.operator
        new_calc.calculate()
        
        print(f"The result is {new_calc.result}")