#!/usr/bin/python3
""" Test function find_peak """
def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    peak = list_of_integers[0]
    for num in list_of_integers:
        if num > peak:
            peak = num

    return peak

# Test cases
print(find_peak([1, 2, 3, 4, 5]))
print(find_peak([5, 4, 3, 2, 1]))
print(find_peak([1, 4, 6, 2, 1]))
print(find_peak([5, 4, 6, 2, 1, 4, 5, 2]))
