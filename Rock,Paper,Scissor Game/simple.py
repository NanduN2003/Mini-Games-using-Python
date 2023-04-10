import random

from colorama import init, Fore, Style

# initialize colorama for colored output
init()

while True:
    # get user input
    user_action = input(Fore.GREEN + "Enter a choice (rock, paper, scissors): " + Style.RESET_ALL).lower()

    # validate user input
    if user_action not in ["rock", "paper", "scissors"]:
        print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
        continue

    # generate computer action
    computer_action = random.choice(["rock", "paper", "scissors"])

    # print choices
    print(Fore.GREEN + f"\nYou chose {user_action}, computer chose {computer_action}." + Style.RESET_ALL)

    # determine winner
    if user_action == computer_action:
        print(Fore.YELLOW + f"Both players selected {user_action}. It's a tie!" + Style.RESET_ALL)
    elif user_action == "rock":
        if computer_action == "scissors":
            print(Fore.GREEN + "Rock smashes scissors! You win!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Paper covers rock! You lose." + Style.RESET_ALL)
    elif user_action == "paper":
        if computer_action == "rock":
            print(Fore.GREEN + "Paper covers rock! You win!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Scissors cuts paper! You lose." + Style.RESET_ALL)
    elif user_action == "scissors":
        if computer_action == "paper":
            print(Fore.GREEN + "Scissors cuts paper! You win!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Rock smashes scissors! You lose." + Style.RESET_ALL)

    # ask to play again
    play_again = input(Fore.CYAN + "Play again? (y/n): " + Style.RESET_ALL).lower()
    if play_again != "y":
        break

print(Fore.CYAN + "Thanks for playing!" + Style.RESET_ALL)
