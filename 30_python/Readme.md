# Python Error Handling, Logging, and Argument Parsing

This document provides an overview of error handling, logging, and argument parsing in Python, with examples and explanations.

---

## 1. Error Handling

Python uses `try`, `except`, `else`, and `finally` blocks to handle exceptions.

### Example

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("No errors occurred.")
finally:
    print("This always runs.")
```

**Explanation:**
- `try`: Code that may raise an exception.
- `except`: Handles specific exceptions.
- `else`: Runs if no exceptions occur.
- `finally`: Always runs, for cleanup.

---

## 2. Logging

The `logging` module provides a flexible framework for emitting log messages from Python programs.

### Example

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    value = 10 / 0
except ZeroDivisionError as e:
    logger.error(f"An error occurred: {e}")
else:
    logger.info("Operation successful.")
finally:
    logger.info("Execution finished.")
```

**Explanation:**
- `logging.basicConfig`: Configures the logging system.
- `getLogger`: Gets a logger instance.
- `logger.error/info`: Logs messages at different severity levels.

---

## 3. Parsing Arguments

Use the `argparse` module to handle command-line arguments.

### Example

```python
import argparse

parser = argparse.ArgumentParser(description="Greet someone.")
parser.add_argument("name", help="Name of the person to greet")
args = parser.parse_args()

print(f"Hello, {args.name}!")
```

**Explanation:**
- `argparse.ArgumentParser`: Creates a parser object.
- `add_argument`: Defines expected arguments.
- `parse_args()`: Parses arguments from the command line.

---

## References

- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Logging](https://docs.python.org/3/library/logging.html)
- [argparse Documentation](https://docs.python.org/3/library/argparse.html)