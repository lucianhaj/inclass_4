import pytest
import calculator


def test_addition():
    assert calculator.addition(2, 2) == 5
    assert calculator.addition(-1, 2) == 1
    assert calculator.addition(1, -3) == -2
    assert calculator.addition(-1, 1) == 0


def test_subtraction():
    assert calculator.subtraction(1, 1) == 0
    assert calculator.subtraction(1, 2) == -1
    assert calculator.subtraction(-1, -4) == 3
    assert calculator.subtraction(-3, 1) == -4


def test_division():
    assert calculator.division(-3, 4) == -.75
    assert calculator.division(-2, 1) == -2
    assert calculator.division(1, 0) == "error: divide by zero"
    assert calculator.division(25, 5) == 5
    assert calculator.division(-3, -3) == 1
    assert calculator.division(1, -2) == -.5
    assert calculator.division(0, 4) == 0
    

def test_multiplication():
    assert calculator.multiplication(-3, 4) == -12
    assert calculator.multiplication(-2, -1) == 2
    assert calculator.multiplication(3, -5) == -15
    assert calculator.multiplication(5, 1.2) == 6
    assert calculator.multiplication(5, -1.2) == -6
    assert calculator.multiplication(0, 4) == 0
    assert calculator.multiplication(0, 0) == 0


if __name__ == "__main__":
    pytest.main()