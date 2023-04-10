def check_win(state):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if all(state[i] == "X" for i in win):
            return "X"
        if all(state[i] == "O" for i in win):
            return "O"
    return None

def print_board(state):
    print("\n".join([" | ".join(state[i:i+3]) for i in range(0, 9, 3)]))

if __name__ == "__main__":
    state = [""]*9
    turn = "X"
    print("Welcome to Tic Tac Toe")
    while True:
        print_board(state)
        print(f"{turn}'s turn")
        try:
            value = int(input("Please enter a value (0-8): "))
            if not 0 <= value <= 8:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")
            continue
        if state[value]:
            print("That spot is already taken. Please choose another.")
            continue
        state[value] = turn
        winner = check_win(state)
        if winner:
            print_board(state)
            print(f"{winner} won the game!")
            break
        if all(state):
            print_board(state)
            print("It's a tie!")
            break
        turn = "O" if turn == "X" else "X"
