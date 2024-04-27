def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    
    low, high = 0, len(list_of_integers) - 1
    
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1
    
    return list_of_integers[low]

# Test cases
print(find_peak([1, 2, 3, 4, 5]))  # Output: 5
print(find_peak([5, 4, 3, 2, 1]))  # Output: 5
print(find_peak([1, 4, 6, 2, 1]))  # Output: 6
print(find_peak([5, 4, 6, 2, 1, 4, 5, 2]))  # Output: 6
