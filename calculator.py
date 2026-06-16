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
    """
    if a == 0 and b == 0:
        raise ValueError("0**0 is undefined")
    return a ** b
