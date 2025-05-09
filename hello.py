"""
This file contains basic arithmetic operations
"""

def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together
    Args:
        a: First number
        b: Second number
    Returns:
        Sum of a and b
    """
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """
    Subtract second number from first
    Args:
        a: First number
        b: Second number to subtract
    Returns:
        Result of a minus b
    """
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """
    Multiply two numbers together
    Args:
        a: First number
        b: Second number
    Returns:
        Product of a and b
    """
    return a * b


def divide_numbers(a: float, b: float) -> float | None:
    """
    Divide first number by second number
    Args:
        a: Numerator
        b: Denominator
    Returns:
        Result of division or None if denominator is zero
    """
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    except ZeroDivisionError:
        return None


def main():
    """Main function to test arithmetic operations"""
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    print(divide_numbers(5, 0))


if __name__ == "__main__":
    main()
