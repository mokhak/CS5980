import pytest
from Project5.__init__ import Calculator

# Creating a fixture to test out the calculator class
@pytest.fixture
def testCalculator():
    # Inputting class with Number 1 as 20 and Number 2 as 10
    testCalc = Calculator(20,10,None,0)
    return testCalc

# Testing Addition
def testAdd(testCalculator):
    testCalculator.operator = "+"
    testCalculator.calculate()
    assert testCalculator.result == float(30)

# Testing Subtraction
def testSub(testCalculator):
    testCalculator.operator = "-"
    testCalculator.calculate()
    assert testCalculator.result == float(10)

# Testing Division
def testDiv(testCalculator):
    testCalculator.operator = "/"
    testCalculator.calculate()
    assert testCalculator.result == float(2)

# Testing Multiplication
def testMult(testCalculator):
    testCalculator.operator = "X"
    testCalculator.calculate()
    assert testCalculator.result == float(200)

# Testing Modulus
def testMod(testCalculator):
    testCalculator.operator = "%"
    testCalculator.calculate()
    assert testCalculator.result == float(0)

# Testing Exponential
def testExp(testCalculator):
    testCalculator.operator = "^"
    testCalculator.calculate()
    assert testCalculator.result == float(10240000000000)
    

    
