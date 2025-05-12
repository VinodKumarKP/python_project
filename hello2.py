"""
Mathematical operations module providing basic arithmetic functions.
"""
from typing import Union, float64


def add_numbers(a: float64, b: float64) -> float64:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of the two numbers
    """
    return a + b


def subtract_numbers(a: float64, b: float64) -> float64:
    """
    Subtract second number from first number.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference between the numbers
    """
    return a - b


def multiply_numbers(a: float64, b: float64) -> float64:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of the two numbers
    """
    return a * b


def divide_numbers(a: float64, b: float64) -> Union[float64, None]:
    """
    Divide first number by second number.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Quotient of the division or None if division by zero
    
    Raises:
        ZeroDivisionError: If b is zero
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    print(divide_numbers(5, 0))