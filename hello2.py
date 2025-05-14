"""
Simple arithmetic operations with improved code quality and error handling.
"""
from typing import Union, Optional

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a + b

def subtract_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract second number from first.
    
    Args:
        a (int or float): First number
        b (int or float): Number to subtract
    
    Returns:
        int or float: Difference between a and b
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
        int or float: Product of a and b
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a * b

def divide_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divide first number by second number.
    
    Args:
        a (int or float): Numerator
        b (int or float): Denominator
    
    Returns:
        int or float: Result of division
    
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
    Demonstrate arithmetic operations with error handling.
    """
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 2))
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()