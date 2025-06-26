# Python Examples

This README provides basic Python examples for string manipulation, loops, and conditions, with explanations.

## String Manipulation

```python
# Concatenation
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, Alice!

# Slicing
text = "Python"
print(text[1:4])  # Output: yth

# Upper and Lower Case
print(text.upper())  # Output: PYTHON
print(text.lower())  # Output: python
```
*Explanation*:  
- Concatenation joins strings together.  
- Slicing extracts a substring.  
- `upper()` and `lower()` change the case.

---

## Loops

```python
# For loop
for i in range(3):
    print("Iteration:", i)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1
```
*Explanation*:  
- `for` loops iterate over a sequence or range.  
- `while` loops repeat as long as a condition is true.

---

## Conditions

```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```
*Explanation*:  
- `if`, `elif`, and `else` control the flow based on conditions.

---

Feel free to expand these examples for more practice!