from Project5.__init__ import errorCheck

def test_number1():
    assert errorCheck(1,2,"+") == True
    assert errorCheck("a",2,"+") == False
    
def test_number2():
    assert errorCheck(1,3,"+") == True
    assert errorCheck(1,"b","+") == False
    
def test_operator():
    assert errorCheck(2,3,"-") == True
    assert errorCheck(2,3,"a") == False