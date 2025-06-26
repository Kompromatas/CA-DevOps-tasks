print("=" * 100)
print(("Welcome to the Calculator!").center(100))
print("=" * 100)
print("Please enter two numbers and an operator (+, -, *, /) to perform a calculation")
print("After entering the number or operator, press Enter to submit.")
print("Example: 5 + 3")
print("You can also type 'exit' to quit the calculator.")
print("=" * 100)
number1 = input("")
if number1.lower() == "exit":
    print("Exiting the calculator. Goodbye!")
    exit()
operator = input("")
if operator.lower() == "exit":
    print("Exiting the calculator. Goodbye!")
    exit()
number2 = input("")
if number2.lower() == "exit":
    print("Exiting the calculator. Goodbye!")
    exit()

if operator == "+":
    result = float(number1) + float(number2)
    print(f"The result of {number1} + {number2} is: {result}")
elif operator == "-":
    result = float(number1) - float(number2)
    print(f"The result of {number1} - {number2} is: {result}")
elif operator == "*":
    result = float(number1) * float(number2)
    print(f"The result of {number1} * {number2} is: {result}")
elif operator == "/":
    if float(number2) != 0:
        result = float(number1) / float(number2)
        print(f"The result of {number1} / {number2} is: {result}")
    else:
        result = "Error: Division by zero is not allowed."
        print(result)




