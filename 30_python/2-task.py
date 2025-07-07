import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

def devide(num1, num2):
    """
    Divides two numbers and handles division by zero.
    
    Args:
        num1 (int): The numerator.
        num2 (int): The denominator.
    
    Returns:
        The result of the division or None if division by zero occurs.
    """
    try:
        result = num1 / num2
        logging.info(f"Division successful: {num1} / {num2} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero.")
        return None

try:
    x= int(input("Enter the first number: "))
    y= int(input("Enter the second number: "))
except ValueError:
    logging.error("Invalid input: Please enter valid integers.")

a = devide(x, y)
print(f"The result is: {a}")


