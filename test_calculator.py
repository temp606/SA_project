import pytest
from calculator import add, subtract, multiply, divide, power, modulus


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5


def test_power_zero_to_zero():
    """Test that 0**0 raises ValueError (undefined in mathematics)"""
    with pytest.raises(ValueError, match="Cannot compute 0\\*\\*0"):
        power(0, 0)


def test_power_zero_base_with_positive_exponent():
    """Test that 0 to positive power returns 0"""
    assert power(0, 1) == 0
    assert power(0, 5) == 0


def test_power_zero_base_with_negative_exponent():
    """Test that 0 to negative power raises ValueError (undefined)"""
    with pytest.raises(ValueError, match="Cannot compute 0 to a negative power"):
        power(0, -1)


def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(15, 4) == 3


def test_modulus_by_zero():
    with pytest.raises(ValueError):
        modulus(5, 0)


def test_modulus_negative_dividend():
    """Test modulus with negative dividend (result sign follows divisor)"""
    # In Python: -7 % 3 = 2 (positive divisor, result is positive)
    assert modulus(-7, 3) == 2
    assert modulus(-8, 3) == 1


def test_modulus_negative_divisor():
    """Test modulus with negative divisor (result sign follows divisor)"""
    # In Python: 7 % -3 = -2 (negative divisor, result is negative)
    assert modulus(7, -3) == -2
    assert modulus(8, -3) == -1


def test_modulus_both_negative():
    """Test modulus with both operands negative"""
    # In Python: -7 % -3 = -1 (result sign follows divisor)
    assert modulus(-7, -3) == -1
    assert modulus(-8, -3) == -2
