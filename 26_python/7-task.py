print("=" * 60)
print(("Welcome to the game paper rock scissors!").center(60, "="))
print("=" * 60)
print("To exit the game, type 'exit' at any time.")
print("=" * 60)
import random

choices = ["rock", "paper", "scissors"]

input_choice = ""

while input_choice.lower() != "exit":

    input_choice = input("Please enter your choice (rock, paper, scissors): ")

    if input_choice.lower() not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        
    random_choice = random.choice(choices)

    print(f"Computer chose: {random_choice}")

    if input_choice.lower() == random_choice:
        print("It's a tie!")
    elif (input_choice.lower() == "rock" and random_choice == "scissors") or \
         (input_choice.lower() == "paper" and random_choice == "rock") or \
        (input_choice.lower() == "scissors" and random_choice == "paper"):
        print("You win!")
    elif (input_choice.lower() == "rock" and random_choice == "paper") or \
         (input_choice.lower() == "paper" and random_choice == "scissors") or \
        (input_choice.lower() == "scissors" and random_choice == "rock"):
        print("You lose!")

print("Thank you for playing!")
