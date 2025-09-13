"""
Mathematical operations module providing basic arithmetic functions.
"""
from typing import Union, Optional


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of the two numbers
    """
    return a + b


def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract second number from first number.
    
    Args:
        a: First number
        b: Second number to subtract
        
    Returns:
        Difference between the numbers
    """
    return a - b


def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of the two numbers
    """
    return a * b


def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """
    Divide first number by second number.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Result of division or None if division by zero
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