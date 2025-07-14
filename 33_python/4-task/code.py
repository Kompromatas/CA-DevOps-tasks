import time

def decorator(func):
    def wrapper(*args, **kwargs):
        """Decorator to measure execution time of a function."""
        print(f"Starting function '{func.__name__}'")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds")
        return result
    return wrapper

@decorator
def sum():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"Function: Adding {x} and {y}")
    return x + y

result = sum()
print(f"Result: {result}")
