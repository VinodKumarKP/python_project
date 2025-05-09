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
    try:
        return a + b
    except TypeError:
        raise TypeError("Arguments must be numbers")


def subtract_numbers(a: Number, b: Number) -> Number:
    """
    Subtract second number from first number.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
        
    Returns:
        Result of subtraction
    """
    try:
        return a - b
    except TypeError:
        raise TypeError("Arguments must be numbers")


def multiply_numbers(a: Number, b: Number) -> Number:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of the two numbers
    """
    try:
        return a * b
    except TypeError:
        raise TypeError("Arguments must be numbers")


def divide_numbers(a: Number, b: Number) -> Union[Number, None]:
    """
    Divide first number by second number.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Result of division or None if denominator is zero
    """
    try:
        if b != 0:
            return a / b
        return None
    except TypeError:
        raise TypeError("Arguments must be numbers")


if __name__ == "__main__":
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    print(divide_numbers(5, 0))
