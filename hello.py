"""Mathematical operations module providing basic arithmetic functions."""

def add_numbers(a: float, b: float) -> float:
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


def subtract_numbers(a: float, b: float) -> float:
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


def multiply_numbers(a: float, b: float) -> float:
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


def divide_numbers(a: float, b: float) -> float:
    """Divide first number by second number.
    
    Args:
        a: First number (numerator)
        b: Second number (denominator)
        
    Returns:
        Quotient of the division or None if denominator is zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    if b != 0:
        return a / b
    return None


# Test cases
print(add_numbers(5, 3))
print(subtract_numbers(5, 3))
print(multiply_numbers(5, 3))
print(divide_numbers(5, 0))
