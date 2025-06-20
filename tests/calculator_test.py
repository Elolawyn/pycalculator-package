import pytest

from elolawyn_calculator.calculator import PI, Calculator


def test_pi():
    assert PI == 3.141592653589793


def test_calculator_cannot_be_instantiated():
    with pytest.raises(TypeError, match="no se puede instanciar"):
        Calculator()


# Tests para .add
def test_add_positive():
    assert Calculator.add(2, 3) == 5


def test_add_negative():
    assert Calculator.add(-1, -1) == -2


def test_add_zero():
    assert Calculator.add(0, 10) == 10


def test_add_mixed_signs():
    assert Calculator.add(-5, 15) == 10


# Tests para .subtract
def test_subtract_positive():
    assert Calculator.subtract(10, 5) == 5


def test_subtract_negative():
    assert Calculator.subtract(-3, -2) == -1


def test_subtract_zero():
    assert Calculator.subtract(7, 0) == 7


# Tests para .multiply
def test_multiply_positive():
    assert Calculator.multiply(4, 5) == 20


def test_multiply_negative():
    assert Calculator.multiply(-2, 3) == -6


def test_multiply_zero():
    assert Calculator.multiply(0, 100) == 0


# Tests para .divide
def test_divide_positive():
    assert Calculator.divide(10, 2) == 5


def test_divide_negative():
    assert Calculator.divide(-15, 3) == -5


def test_divide_float_result():
    assert Calculator.divide(7, 2) == 3.5


def test_divide_zero_numerator():
    assert Calculator.divide(0, 3) == 0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        Calculator.divide(10, 0)
