import argparse
from calculator import Calculator



def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def check_operator(operator):
    if(operator == ("+" or "-" or "X" or "/" or "%" or "^")):
        return True
    else:
        return False

def error_check(number1, number2, operator):
    if(is_float(number1) == False):
        print("Enter a numeric value for number 1!")
        return False
    elif(is_float(number2) == False):
        print("Enter a numeric value for Number 2!")
        return False
    elif(check_operator(operator) == False):
        print("Enter a valid operator!")
        return False
    else:
        return True
        

if __name__ == '__main__':
    
    new_calc = Calculator(0, 0, None, 0)
    tmpError = False
    
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="Number 1")
    parser.add_argument("operator", help="Operation")
    parser.add_argument("number2", help="Number 2")
    args = parser.parse_args()
    tmpError = error_check(args.number1, args.number2, args.operator)
    
    if tmpError:
        new_calc.number1 = float(args.number1)
        new_calc.number2 = float(args.number2)
        new_calc.operator = args.operator
        new_calc.calculate()
        
        print(f"The result is {new_calc.result}")
    
