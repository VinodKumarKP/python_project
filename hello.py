"""Mathematical operations module."""
from typing import Union, NoReturn
from decimal import Decimal


class DivisionByZeroError(Exception):
    """Raised when attempting to divide by zero."""
    pass


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of the two numbers
    """
    return a + b


def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract second number from first number.

    Args:
        a: First number
        b: Second number to subtract

    Returns:
        Difference between the numbers
    """
    return a - b


def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of the two numbers
    """
    return a * b


def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[float, NoReturn]:
    """Divide first number by second number.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Result of division

    Raises:
        DivisionByZeroError: If attempting to divide by zero
    """
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 0))
    except DivisionByZeroError as e:
        print(f"Error: {e}")