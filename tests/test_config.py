import pytest
class NotInRange(Exception):
    def __init__(self, message="value not in range"):
        #self.input_ = input_
        self.message = message
        super().__init__(self.message)

def test_genaric():
    a =5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange

def test_something():
    a=2
    b = 3
    assert True