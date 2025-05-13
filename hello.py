"""
Mathematical operations module providing basic arithmetic functions.
"""
from typing import Union, Optional


def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of the two numbers
    """
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """
    Subtract second number from first number.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference between the two numbers
    """
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of the two numbers
    """
    return a * b


def divide_numbers(a: float, b: float) -> float:
    """
    Divide first number by second number.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Result of division
        
    Raises:
        ZeroDivisionError: If denominator is zero
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


if __name__ == "__main__":
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 0))
    except ZeroDivisionError as e:
        print(f"Error: {e}")