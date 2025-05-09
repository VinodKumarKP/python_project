"""Basic arithmetic operations module."""
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
        b: Second number to subtract

    Returns:
        Difference of the two numbers
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


def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """Divide first number by second number.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Quotient of the division or None if division by zero
    
    Raises:
        ZeroDivisionError: If attempting to divide by zero
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")


if __name__ == "__main__":
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    try:
        print(divide_numbers(5, 0))
    except ZeroDivisionError as e:
        print(f"Error: {e}")
