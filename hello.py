# Mathematical operations module

def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return their sum.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of the two numbers
    """
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """Subtract second number from first number.
    
    Args:
        a: First number
        b: Second number to subtract
        
    Returns:
        Difference between the numbers
    """
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of the two numbers
    """
    return a * b


def divide_numbers(a: float, b: float) -> float | None:
    """Divide first number by second number.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Quotient of division or None if denominator is zero
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def main():
    """Main function to demonstrate calculations."""
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    print(divide_numbers(5, 0))


if __name__ == "__main__":
    main()
