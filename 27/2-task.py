def string_function(s):
    """
    This function returns string in reverse order.
    """
    if s:
        s = s[::-1]
        return s.lower()
    else:
        return "You entered an empty string."

word = input("Enter a word or random letters: ")

print("Reversed word or so:", string_function(word))
