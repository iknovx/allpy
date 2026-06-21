print("Welcome to the Rock, Paper, Scissors game!")
print("You can choose rock, paper, or scissors.")
user_choice = input("Enter your choice (rock, paper, scissors): ").lower() # Get user input and convert it to lowercase
import random
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices) # Randomly select a choice for the computer
print("Computer chose:", computer_choice)
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
elif (user_choice == "rock" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "scissors") or \
        (user_choice == "scissors" and computer_choice == "rock"):
    print("Computer wins!")
else:
    print("Invalid choice. Please enter rock, paper, or scissors.")
    