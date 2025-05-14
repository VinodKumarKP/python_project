"""
Mathematical operations module with improved code quality.
"""
from typing import Union, Optional

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        Union[int, float]: Sum of a and b
    """
    return a + b

def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        Union[int, float]: Difference between a and b
    """
    return a - b

def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        Union[int, float]: Product of a and b
    """
    return a * b

def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divide two numbers.
    
    Args:
        a (int/float): Numerator
        b (int/float): Denominator
    
    Returns:
        Union[int, float]: Result of division
    
    Raises:
        ValueError: If denominator is zero
        TypeError: If inputs are not numeric
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric")
    
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    return a / b

def main():
    """
    Demonstrate mathematical operations.
    """
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 2))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()