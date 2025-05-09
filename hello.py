from typing import Union, Number

def add_numbers(a: Number, b: Number) -> Number:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of the two numbers
    """
    if not all(isinstance(x, (int, float)) for x in [a, b]):
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
    if not all(isinstance(x, (int, float)) for x in [a, b]):
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
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise TypeError("Arguments must be numbers")
    return a * b


def divide_numbers(a: Number, b: Number) -> Union[Number, None]:
    """Divide first number by second number.

    Args:
        a: First number (dividend)
        b: Second number (divisor)

    Returns:
        Quotient of the division or None if division by zero
    
    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If attempting to divide by zero
    """
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise TypeError("Arguments must be numbers")
    
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")


if __name__ == "__main__":
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 2))
        # print(divide_numbers(5, 0))  # This would raise ZeroDivisionError
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error: {e}")
