# Python Functions and Modules

This document explains how to create and use functions and modules in Python, with examples.

## Functions

A **function** is a reusable block of code that performs a specific task.

### Defining a Function

```python
def greet(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")
```

### Calling a Function

```python
greet("Alice")
# Output: Hello, Alice!
```

### Function with Return Value

```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

## Modules

A **module** is a file containing Python code (functions, classes, variables) that can be imported into other Python files.

### Creating a Module

1. Create a file named `mymodule.py`:

```python
# mymodule.py
def multiply(a, b):
    return a * b
```

2. Import and use the module in another file:

```python
# main.py
import mymodule

result = mymodule.multiply(4, 6)
print(result)  # Output: 24
```

### Importing Specific Functions

```python
from mymodule import multiply

print(multiply(2, 3))  # Output: 6
```

## Summary

- Use `def` to define functions.
- Use modules to organize and reuse code.
- Import modules using `import` or `from ... import ...`.

For more details, see the [official Python documentation](https://docs.python.org/3/tutorial/modules.html).