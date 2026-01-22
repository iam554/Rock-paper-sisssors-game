# rock_paper_scissors.py

import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter rock, paper, or scissors: ").lower()

if user_choice not in choices:
    print("Invalid choice")
else:
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Result: Draw")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You Win!")
    else:
        print("Result: You Lose!")