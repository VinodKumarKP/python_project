"""Mathematical operations module."""
from typing import Union, Optional
from decimal import Decimal


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of the two numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
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
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
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
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    return a * b


def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """Divide first number by second number.

    Args:
        a: First number (dividend)
        b: Second number (divisor)

    Returns:
        Quotient of the division, or None if dividing by zero

    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If attempting to divide by zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 2))
        
        # This will raise an error
        print(divide_numbers(5, 0))
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error: {e}")