"""Tests for calculator module."""

import pytest

from calculator import add, subtract, multiply, divide, power


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_zero(self):
        assert add(0, 5) == 5

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_negative_result(self):
        assert subtract(3, 5) == -2

    def test_zero(self):
        assert subtract(5, 0) == 5


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-2, 3) == -6

    def test_floats(self):
        assert multiply(2.5, 4) == 10.0


class TestDivide:
    def test_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_negative_numbers(self):
        assert divide(-10, 2) == -5.0

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(1, 0)


class TestPower:
    def test_positive_exponent(self):
        assert power(2, 3) == 8

    def test_zero_exponent(self):
        assert power(5, 0) == 1

    def test_one_exponent(self):
        assert power(7, 1) == 7

    def test_negative_exponent(self):
        assert power(2, -1) == pytest.approx(0.5)

    def test_base_zero(self):
        assert power(0, 5) == 0

    def test_float_base(self):
        assert power(2.5, 2) == pytest.approx(6.25)

    def test_zero_power_zero(self):
        with pytest.raises(ValueError, match="0\\*\\*0 is undefined"):
            power(0, 0)

    def test_negative_base_integer_exponent(self):
        assert power(-2, 3) == -8

    def test_negative_base_non_integer_exponent(self):
        with pytest.raises(ValueError, match="Negative base with non-integer exponent"):
            power(-4, 0.5)
