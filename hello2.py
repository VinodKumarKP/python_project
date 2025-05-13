"""
Mathematical operations module with proper error handling and validation.
"""
from typing import Union, Optional
import sys


def validate_numeric(a: Union[int, float], b: Union[int, float]) -> None:
    """Validate that inputs are numeric types."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numeric types")


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of the two numbers
    """
    validate_numeric(a, b)
    return a + b


def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract second number from first number.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference between the numbers
    """
    validate_numeric(a, b)
    return a - b


def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of the two numbers
    """
    validate_numeric(a, b)
    return a * b


def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divide first number by second number.
    
    Args:
        a: First number (numerator)
        b: Second number (denominator)
        
    Returns:
        Quotient of the division
        
    Raises:
        ZeroDivisionError: If denominator is zero
        OverflowError: If result exceeds system limits
    """
    validate_numeric(a, b)
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


if __name__ == "__main__":
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 2))
        # This will raise an exception
        # print(divide_numbers(5, 0))
    except (TypeError, ZeroDivisionError, OverflowError) as e:
        print(f"Error: {e}", file=sys.stderr)