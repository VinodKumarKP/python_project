"""
Import math operations from main module instead of duplicating code.
"""
from hello import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

if __name__ == "__main__":
    print(add_numbers(5, 3))
    print(subtract_numbers(5, 3))
    print(multiply_numbers(5, 3))
    print(divide_numbers(5, 0))