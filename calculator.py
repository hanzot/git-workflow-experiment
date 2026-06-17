"""Calculator module with arithmetic and power operations."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    """Return a raised to the power of b.

    Raises:
        ValueError: If both a and b are zero (0**0 is undefined).
        ValueError: If a is negative and b is not an integer (would produce complex result).
    """
    # 0**0 is an indeterminate form; mathematically undefined
    if a == 0 and b == 0:
        raise ValueError("0**0 is undefined")
    # Negative base with non-integer exponent produces complex number,
    # which violates our float return type
    if a < 0 and b != int(b):
        raise ValueError("Negative base with non-integer exponent is not supported")
    return a ** b


def sqrt(a: float) -> float:
    """Return the square root of a.

    Raises:
        ValueError: If a is negative (would produce complex result).
    """
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5
