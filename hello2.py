"""
This file should be removed as it duplicates hello.py
Consider importing functions from hello.py instead if needed
"""
from hello import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

if __name__ == "__main__":
    try:
        print(add_numbers(5, 3))
        print(subtract_numbers(5, 3))
        print(multiply_numbers(5, 3))
        print(divide_numbers(5, 2))
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error: {e}")