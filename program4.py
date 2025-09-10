# clean_code_big.py
from typing import List

def filter_even(numbers: List[int]) -> List[int]:
    """Return a list of even numbers."""
    return [n for n in numbers if n % 2 == 0]

def double_numbers(numbers: List[int]) -> List[int]:
    """Return a list with each number doubled."""
    return [n * 2 for n in numbers]

def main():
    data = [1, 2, 3, 4, 5, 6]
    evens = filter_even(data)
    doubled = double_numbers(evens)
    print("Even numbers:", evens)
    print("Doubled even numbers:", doubled)

if __name__ == "__main__":
    main()