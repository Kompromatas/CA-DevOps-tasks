def print_function(*args):
    """
    This function prints input in seperate line.
    """
    for arg in args:
        print(arg)

input = input("Enter required arguments: ").split()

print_function(*input) 

