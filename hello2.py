"""
Mathematical operations module providing basic arithmetic functions.
"""
from typing import Union, Number


def add_numbers(a: Number, b: Number) -> Number:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of the two numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric types")
    return a + b


def subtract_numbers(a: Number, b: Number) -> Number:
    """
    Subtract second number from first number.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference between the two numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric types")
    return a - b


def multiply_numbers(a: Number, b: Number) -> Number:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of the two numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric types")
    return a * b


def divide_numbers(a: Number, b: Number) -> Union[Number, None]:
    """
    Divide first number by second number.
    
    Args:
        a: First number (numerator)
        b: Second number (denominator)
        
    Returns:
        Quotient of the division or None if denominator is zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric types")
    if b == 0:
        return None
    return a / b


# Example usage
if __name__ == "__main__":
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    print(divide_numbers(5, 0))