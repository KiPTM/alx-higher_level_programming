def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int/float): First integer or float.
        b (int/float): Second integer or float (default is 98).

    Returns:
        int: The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
                   If a is a float, it must be casted to an integer.
                   If b is a float, it must be casted to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
