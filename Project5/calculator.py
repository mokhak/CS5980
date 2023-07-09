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
                