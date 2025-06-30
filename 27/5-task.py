def string_order(strings):
    """
    This function returns the strings in order.
    """
    words = strings.split()
    order = sorted(words, key=len)

    return ' ' .join(order)

input = input("Enter words separated by spaces: ")
if input:
    print("Words in order:", string_order(input))   