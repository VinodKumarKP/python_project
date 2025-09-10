"""
Simple arithmetic operations module with improved code quality.
"""
from typing import Union, Optional

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        Union[int, float]: Sum of a and b
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a + b

def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract two numbers.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        Union[int, float]: Difference between a and b
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a - b

def multiply_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        Union[int, float]: Product of a and b
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a * b

def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divide two numbers.
    
    Args:
        a (int or float): Numerator
        b (int or float): Denominator
    
    Returns:
        Union[int, float]: Result of division
    
    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If denominator is zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def main():
    """
    Demonstrate arithmetic operations.
    """
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 2))
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()