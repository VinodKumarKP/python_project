"""Mathematical operations module.

This module provides basic mathematical operations with proper error handling.
"""
from typing import Union, Optional

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
        b: Second number

    Returns:
        Difference between the two numbers
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


def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divide first number by second number.

    Args:
        a: First number
        b: Second number

    Returns:
        Quotient of the division

    Raises:
        ValueError: If attempting to divide by zero
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


if __name__ == "__main__":
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    try:
        print(divide_numbers(5, 0))
    except ValueError as e:
        print(f"Error: {e}")