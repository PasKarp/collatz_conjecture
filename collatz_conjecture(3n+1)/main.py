from animation import *

"""
Module: collatz_sequence

This module provides functions to calculate the Collatz sequence for a given number and update a dictionary with Collatz sequence information.

Functions:
    - calc(n): Calculate the next number in the Collatz sequence based on the given number.
    - update_sequence_dict(seq_dict, current_number): Update the given dictionary with Collatz sequence information starting from the specified number.
"""


def calc(n):
    """
    Calculate the next number in the Collatz sequence based on the given number.

    Parameters:
    - n (int): The current number in the sequence.

    Returns:
    - int: The next number in the sequence.
    """
    if n % 2 == 0:
        n = int(n / 2)
        return n
    else:
        n = int(3 * n + 1)
        return n


def update_sequence_dict(seq_dict, current_number):
    """
    Update the given dictionary with Collatz sequence information starting from the specified number.

    Parameters:
    - seq_dict (dict): Dictionary to store Collatz sequence information.
    - current_number (int): The starting number for the sequence update.

    Returns:
    - None
    """
    while current_number not in seq_dict:
        next_number = calc(current_number)
        seq_dict[current_number] = next_number
        current_number = next_number


sequence_dict = {}

# Generate and update Collatz sequences for numbers from 1 to 10000
for i in range(1, 10001):
    update_sequence_dict(sequence_dict, i)

# Print the resulting Collatz sequence dictionary
print(sequence_dict)
