#Game Stone Paper Scissor
import random
from enum import IntEnum


class Choice(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def main():
    print("Welcome to Siddhi's Rock, Paper, Scissors!")

    play_again = True

    while play_again:
        print("\nChoose your option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        try:
            user_input = int(input("Your choice (1-3): "))
            if user_input not in range (1, 4):
                print("Invalid input. Try again.")
                continue
        except ValueError:
            print("Invalid input. Try again.")
            continue

        user_choice = Choice(user_input)
        computer_choice = Choice(random.randint(1, 3))

        print(f"\nYou chose: {user_choice.name}")
        print(f"Computer chose: {computer_choice.name}")

        # Determine winner
        if user_choice == computer_choice:
            print("It's a draw!")
        elif ((user_choice == Choice.ROCK and computer_choice == Choice.SCISSORS) or
              (user_choice == Choice.PAPER and computer_choice == Choice.ROCK) or
              (user_choice == Choice.SCISSORS and computer_choice == Choice.PAPER)):
            print("Congrats, You win!")
        else:
            print("OOh Noo, Computer wins!, Better Luck Next Time!")

        again = input("\nPlay again? (y/n): ").lower()
        play_again = (again == 'y' or again == 'yes')

    print("\nThanks for playing!, have a nice day!")


if __name__ == "__main__":
    main()
