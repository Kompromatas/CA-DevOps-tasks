def decorator(arg):
    """Decorator to measure execution time of a function."""
    def inner(func):
        def wrapper(*args, **kwargs):
            print(f"Before function '{func.__name__}' start, today is {arg}")
            #func()
            result = func(*args, **kwargs)
            print(f"After function '{func.__name__}' execution, today is {arg}")
            return result
        return wrapper
    return inner

today = str(input("What day of the week is it today? "))
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
@decorator(today)
def sum(x, y):
    print(f"Function: Adding {x} and {y}")
    return x + y    

sum = sum(x, y)
print(f"Result: {sum}")

@decorator(today)
def multiply(x, y):
    print(f"Function: Multiplying {x} and {y}")
    return x * y

multiply = multiply(x, y)
print(f"Result: {multiply}")