'''my calculator'''
from calculator import add, subtract
def test_addition():
    '''Test that addition function works '''    
    assert add(5,3) == 8

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(7,3) == 4
