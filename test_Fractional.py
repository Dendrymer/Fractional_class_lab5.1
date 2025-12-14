
import pytest
from Fractional import Fractional

def test_init_and_str():
    f = Fractional(2, 4)
    assert str(f) == "1/2"   #powinno się skrócić
    f2 = Fractional(-3, -6)
    assert str(f2) == "1/2"  #znak przeniesiony do licznika i skrócenie

def test_zero_mianownik():
    with pytest.raises(ValueError):
        Fractional(1, 0)

def test_addition():
    a = Fractional(1, 2)
    b = Fractional(1, 3)
    result = a + b
    assert str(result) == "5/6"

def test_subtraction():
    a = Fractional(3, 4)
    b = Fractional(1, 2)
    result = a - b
    assert str(result) == "1/4"

def test_multiplication():
    a = Fractional(2, 3)
    b = Fractional(3, 5)
    result = a * b
    assert str(result) == "2/5"

def test_division():
    a = Fractional(1, 2)
    b = Fractional(3, 4)
    result = a / b
    assert str(result) == "2/3"

def test_division_by_zero():
    a = Fractional(1, 2)
    with pytest.raises(ZeroDivisionError):
        a / Fractional(0, 1)

def test_rowne():
    a = Fractional(2, 4)
    b = Fractional(1, 2)
    assert a == b

def test_mniejsze_od():
    a = Fractional(1, 3)
    b = Fractional(1, 2)
    assert a < b
    assert not (b < a)

def test_int_konwersja_do_ulamka():
    a = Fractional(1, 2)
    result = a + 2   # powinno zamienić 2 na 2/1
    assert str(result) == "5/2"