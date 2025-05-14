"""
Simple arithmetic operations with improved code quality and error handling.
"""

def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers and return the result.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    try:
        return float(a) + float(b)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid input: {e}")

def subtract_numbers(a: float, b: float) -> float:
    """
    Subtract second number from first number.
    
    Args:
        a (float): First number
        b (float): Number to subtract
    
    Returns:
        float: Result of subtraction
    """
    try:
        return float(a) - float(b)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid input: {e}")

def multiply_numbers(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Product of a and b
    """
    try:
        return float(a) * float(b)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid input: {e}")

def divide_numbers(a: float, b: float) -> float:
    """
    Divide first number by second number.
    
    Args:
        a (float): Numerator
        b (float): Denominator
    
    Returns:
        float: Result of division
    
    Raises:
        ZeroDivisionError: If denominator is zero
        ValueError: If inputs are invalid
    """
    try:
        a, b = float(a), float(b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid input: {e}")

def main():
    """
    Demonstrate arithmetic operations with error handling.
    """
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 2))
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()