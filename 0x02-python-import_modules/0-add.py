a = 1
b = 2

# Define a function that imports add_0.py and performs the addition
def import_and_add():
    from add_0 import add
    result = add(a, b)
    return result

# Call the function and print the result using string formatting
result = import_and_add()
print("{} + {} = {}".format(a, b, result))
