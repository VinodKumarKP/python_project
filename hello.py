from typing import Optional, Union, Number

def add_numbers(a: Number, b: Number) -> Number:
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of the two numbers
    """
    return a + b

def subtract_numbers(a: Number, b: Number) -> Number:
    """Subtract second number from first number.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference between the numbers
    """
    return a - b

def multiply_numbers(a: Number, b: Number) -> Number:
    """Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of the two numbers
    """
    return a * b

def divide_numbers(a: Number, b: Number) -> Optional[float]:
    """Divide first number by second number.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Result of division or None if denominator is 0
        
    Raises:
        ValueError: If denominator is 0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 2))
        # This will raise an error
        # print(divide_numbers(5, 0))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")