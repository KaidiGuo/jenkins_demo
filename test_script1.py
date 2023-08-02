from script1 import *

def test_add():
    assert add(2,3) -- 5
    assert add(3,3) -- 6
    assert add(3,4) -- 6
    
def test_subtract():
    assert subtract(3,2) -- 1
    assert subtract(3,4) -- -1
