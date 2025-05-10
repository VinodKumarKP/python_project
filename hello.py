from typing import Union, Number

def add_numbers(a: Number, b: Number) -> Number:
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

def subtract_numbers(a: Number, b: Number) -> Number:
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

def multiply_numbers(a: Number, b: Number) -> Number:
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

def divide_numbers(a: Number, b: Number) -> Number:
    """Divide first number by second number.
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
        
    Returns:
        Quotient of the division
        
    Raises:
        ZeroDivisionError: If divisor is zero
        TypeError: If arguments are not numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

print(add_numbers(5, 3))
print(subtract_numbers(5, 3))
print(multiply_numbers(5, 3))
try:
    print(divide_numbers(5, 0))
except ZeroDivisionError as e:
    print(f"Error: {e}")
