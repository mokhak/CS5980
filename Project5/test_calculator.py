import pytest
from Project5.__init__ import Calculator

@pytest.fixture
def testCalculator():
    testCalc = Calculator(20,10,None,0)
    return testCalc

def testAdd(testCalculator):
    testCalculator.operator = "+"
    testCalculator.calculate()
    assert testCalculator.result == float(30)
    
def testSub(testCalculator):
    testCalculator.operator = "-"
    testCalculator.calculate()
    assert testCalculator.result == float(10)
    
def testDiv(testCalculator):
    testCalculator.operator = "/"
    testCalculator.calculate()
    assert testCalculator.result == float(2)
    
def testMult(testCalculator):
    testCalculator.operator = "X"
    testCalculator.calculate()
    assert testCalculator.result == float(200)
    
def testMod(testCalculator):
    testCalculator.operator = "%"
    testCalculator.calculate()
    assert testCalculator.result == float(0)
    
def testExp(testCalculator):
    testCalculator.operator = "^"
    testCalculator.calculate()
    assert testCalculator.result == float(10240000000000)
    

    
