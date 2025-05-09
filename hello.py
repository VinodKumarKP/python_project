"""Basic arithmetic operations module."""
from typing import Union, Number


def add_numbers(a: Number, b: Number) -> Number:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of the two numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a + b


def subtract_numbers(a: Number, b: Number) -> Number:
    """Subtract second number from first number.

    Args:
        a: First number
        b: Second number

    Returns:
        Difference between the two numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a - b


def multiply_numbers(a: Number, b: Number) -> Number:
    """Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of the two numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a * b


def divide_numbers(a: Number, b: Number) -> Number:
    """Divide first number by second number.

    Args:
        a: First number (dividend)
        b: Second number (divisor)

    Returns:
        Quotient of the division

    Raises:
        ValueError: If attempting to divide by zero
        TypeError: If inputs are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 2))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
