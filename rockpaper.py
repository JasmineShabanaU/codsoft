import random

def get_computer_choice():
    """Generate computer's choice randomly."""
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user, computer):
    """Determine the result of the round."""
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "win"
    else:
        return "lose"


def display_result(user, computer, result):
    """Display round result."""
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")

    if result == "win":
        print("🎉 Congratulations! You win this round!")
    elif result == "lose":
        print("😢 You lose this round!")
    else:
        print("🤝 It's a tie!")


def get_user_choice():
    """Get valid input from user."""
    while True:
        choice = input("\nEnter Rock, Paper, or Scissors: ").strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("❌ Invalid choice! Please enter rock, paper, or scissors.")


def play_game():
    """Main game function."""
    print("=" * 50)
    print("✊ ✋ ✌️   ROCK PAPER SCISSORS GAME")
    print("=" * 50)
    print("Instructions:")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock")
    print("=" * 50)

    user_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n🎮 Round {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1
        print("\n📊 Score Board")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()

        if play_again not in ["yes", "y"]:
            print("\n🏁 Final Score")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")

            if user_score > computer_score:
                print("🏆 You are the overall winner!")
            elif computer_score > user_score:
                print("💻 Computer wins overall!")
            else:
                print("🤝 The game ends in a tie!")

            print("\nThanks for playing! 👋")
            break

        round_number += 1
if __name__ == "__main__":
    play_game()
