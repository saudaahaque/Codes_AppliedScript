
import calculator 
import pytest

def test_add():
    assert calculator.add(2, 3) == 5

def test_sub():
    assert calculator.sub(10, 5) == 5

def test_multi():
    assert calculator.multi(2, 5) == 10

def test_divison():
    assert calculator.divison(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divison(10, 0)