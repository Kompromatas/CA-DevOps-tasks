
sentence = input("Enter sentence: ")

letter_counts = {}

for char in sentence:
    if char.isalpha(): 
        char = char.lower()  
        letter_counts[char] = letter_counts.get(char, 0) + 1


for letter, count in sorted(letter_counts.items()):
    print(f"Letter '{letter}' count in the sentence = {count}.")