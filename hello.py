#!/usr/bin/env python3
"""
Mathematical operations module providing basic arithmetic functions.
"""

def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return their sum."""
    return a + b

def subtract_numbers(a: float, b: float) -> float:
    """Subtract second number from first and return the difference."""
    return a - b

def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers and return their product."""
    return a * b

def divide_numbers(a: float, b: float) -> float | None:
    """
    Divide first number by second number.
    
    Args:
        a: Numerator
        b: Denominator
    
    Returns:
        float: Result of division
        None: If denominator is zero
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None

def main():
    """Main function to demonstrate arithmetic operations."""
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    print(divide_numbers(5, 0))

if __name__ == "__main__":
    main()
