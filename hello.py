# Mathematical operations with input validation and error handling

def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return their sum."""
    return a + b

def subtract_numbers(a: float, b: float) -> float:
    """Subtract second number from first and return difference."""
    return a - b

def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers and return their product."""
    return a * b

def divide_numbers(a: float, b: float) -> float | None:
    """
    Divide first number by second and return quotient.
    Returns None if denominator is zero.
    """
    try:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b
    except ZeroDivisionError:
        return None

def main():
    """Main function to demonstrate arithmetic operations."""
    # Test cases
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    print(divide_numbers(5, 0))

if __name__ == "__main__":
    main()
