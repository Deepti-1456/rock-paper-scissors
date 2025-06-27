import random  # Importing random module to let the computer make random choices

# List of possible choices
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors Game!")
print("Type 'rock', 'paper' or 'scissors' to play.")
print("Type 'quit' to stop the game.")

while True:
    # Get user's choice
    user_choice = input("Your choice: ").lower()

    # Check if user wants to quit
    if user_choice == "quit":
        print("Thanks for playing! Goodbye.")
        break

    # Check if the input is valid
    if user_choice not in choices:
        print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
        continue

    # Computer randomly chooses
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

    print("-" * 30)  # Separator for better readability
