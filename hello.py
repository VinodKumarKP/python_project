"""Mathematical operations module."""
from typing import Union, Optional
import numbers


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of the two numbers
    """
    if not isinstance(a, numbers.Number) or not isinstance(b, numbers.Number):
        raise TypeError("Arguments must be numbers")
    return a + b


def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract second number from first number.

    Args:
        a: First number
        b: Second number

    Returns:
        Difference between the numbers
    """
    if not isinstance(a, numbers.Number) or not isinstance(b, numbers.Number):
        raise TypeError("Arguments must be numbers")
    return a - b


def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of the two numbers
    """
    if not isinstance(a, numbers.Number) or not isinstance(b, numbers.Number):
        raise TypeError("Arguments must be numbers")
    return a * b


def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divide first number by second number.

    Args:
        a: First number (dividend)
        b: Second number (divisor)

    Returns:
        Quotient of the division

    Raises:
        ZeroDivisionError: If divisor is zero
        TypeError: If arguments are not numbers
    """
    if not isinstance(a, numbers.Number) or not isinstance(b, numbers.Number):
        raise TypeError("Arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


if __name__ == "__main__":
    # Example usage
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    try:
        print(divide_numbers(5, 0))
    except ZeroDivisionError as e:
        print(f"Error: {e}")