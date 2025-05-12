"""Mathematical operations module.

This module provides basic mathematical operations with input validation.
"""
from typing import Union, Optional
import numbers


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of the two numbers

    Raises:
        TypeError: If inputs are not numbers
    """
    if not all(isinstance(x, numbers.Number) for x in (a, b)):
        raise TypeError("Inputs must be numbers")
    return a + b


def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract second number from first number.

    Args:
        a: First number
        b: Second number

    Returns:
        Difference between the numbers

    Raises:
        TypeError: If inputs are not numbers
    """
    if not all(isinstance(x, numbers.Number) for x in (a, b)):
        raise TypeError("Inputs must be numbers")
    return a - b


def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of the two numbers

    Raises:
        TypeError: If inputs are not numbers
    """
    if not all(isinstance(x, numbers.Number) for x in (a, b)):
        raise TypeError("Inputs must be numbers")
    return a * b


def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divide first number by second number.

    Args:
        a: First number (dividend)
        b: Second number (divisor)

    Returns:
        Quotient of the division

    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If divisor is zero
    """
    if not all(isinstance(x, numbers.Number) for x in (a, b)):
        raise TypeError("Inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


if __name__ == "__main__":
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 2))
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error: {e}")