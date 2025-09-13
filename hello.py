# Mathematical operations module
# Contains basic arithmetic functions with input validation

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
    Returns None if denominator is zero.
    """
    try:
        if b == 0:
            return None
        return a / b
    except (TypeError, ValueError):
        return None

# Test cases
if __name__ == "__main__":
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    print(divide_numbers(5, 0))
