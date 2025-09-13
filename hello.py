from typing import Union, float

def add_numbers(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: Sum of the two numbers
    """
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """Subtract second number from first number.

    Args:
        a (float): First number
        b (float): Second number to subtract

    Returns:
        float: Result of subtraction
    """
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: Product of the two numbers
    """
    return a * b


def divide_numbers(a: float, b: float) -> float:
    """Divide first number by second number.

    Args:
        a (float): Numerator
        b (float): Denominator

    Returns:
        float: Result of division

    Raises:
        ZeroDivisionError: If denominator is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


try:
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    print(divide_numbers(5, 0))
except ZeroDivisionError as e:
    print(f"Error: {e}")
