from Project5.__init__ import isFloat

# Testing isFloat Method
def test_isFloat_TRUE():
    assert isFloat(2.5) == True

def test_isFloat_FALSE():
    assert isFloat("a") == False