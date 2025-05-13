"""Mathematical operations module.

This module provides basic mathematical operations with proper error handling.
"""
from typing import Union, Optional
from numbers import Number


def add_numbers(a: Number, b: Number) -> Number:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of the two numbers
    """
    return a + b


def subtract_numbers(a: Number, b: Number) -> Number:
    """Subtract second number from first number.

    Args:
        a: First number
        b: Second number to subtract

    Returns:
        Difference between the numbers
    """
    return a - b


def multiply_numbers(a: Number, b: Number) -> Number:
    """Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of the two numbers
    """
    return a * b


def divide_numbers(a: Number, b: Number) -> Optional[float]:
    """Divide first number by second number.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Result of division or None if denominator is zero
    """
    try:
        if b == 0:
            return None
        return a / b
    except (TypeError, ValueError) as e:
        print(f"Error performing division: {e}")
        return None


if __name__ == "__main__":
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    print(divide_numbers(5, 0))