# Custom Utility Module for Lab 6.2
"""
my_utils.py - Custom Utility Module
Contains reusable functions for greeting and primality testing.
Created for Lab 6: Functions, Custom Modules, and Standard Library Usage.
"""

def greet(name: str) -> None:
    """
    Prints a friendly greeting message for the specified person.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    None
    """
    print(f"Hello, {name}!")


def is_prime(number: int) -> bool:
    """
    Determines whether a given integer is a prime number.

    A prime number is a natural number greater than 1 that cannot be formed
    by multiplying two smaller natural numbers.

    Parameters:
    number (int): The integer to test for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    # Numbers less than or equal to 1 are not prime
    if not isinstance(number, int) or number <= 1:
        return False
    # 2 and 3 are prime numbers
    if number <= 3:
        return True
    # Exclude even numbers and multiples of 3
    if number % 2 == 0 or number % 3 == 0:
        return False
    # Check possible factors up to sqrt(number)
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    print("Testing my_utils module standalone:")
    greet("World")
    sample_nums = [1, 2, 3, 4, 7, 10, 13, 29, 35]
    for n in sample_nums:
        print(f"is_prime({n:2d}) -> {is_prime(n)}")
