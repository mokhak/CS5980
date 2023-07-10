from Project5.__init__ import checkOperator

def checkOperator_TRUE():
    assert checkOperator("+") == True
    
def checkOperator_FALSE():
    assert checkOperator("a") == False