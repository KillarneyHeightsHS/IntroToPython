# Initialize the board as a 3x3 array filled with spaces
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to display the board
def display_board():
    print("  0   1   2")
    for i, row in enumerate(board):
        print(i, " | ".join(row))
        if i < 2:
            print("  ---------")

# Function to check if a position is occupied
def is_occupied(row, col):
    return board[row][col] != " "

# Function to place X or O at given coordinates
def place_mark(row, col, mark):
    if not is_occupied(row, col):
        board[row][col] = mark
        return True
    else:
        print("That position is already taken!")
        return False

# Function to check for a winner
def check_winner(mark):
    # Check rows
    for i in range(3):
        count = 0
        for j in range(3):
            if board[i][j] == mark:
                count += 1
        if count == 3:
            return True

    # Check columns
    # -- your code goes here --

    # Check main diagonal
    # -- your code goes here --

    # Check anti-diagonal
    count = 0
    for i in range(3):
        if board[i][2 - i] == mark:
            count += 1
    if count == 3:
        return True
    return False

# Function to check for a draw
def is_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False
    return True

# Game loop
def play_game():
    current_player = "X"
    while True:
        display_board()
        print(f"Player {current_player}'s turn.")

        # Get user input
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid coordinates. Try again.")
                continue
        except ValueError:
            print("Please enter numbers only.")
            continue

        # Place mark if valid
        if place_mark(row, col, current_player):
            if check_winner(current_player):
                display_board()
                print(f"Player {current_player} wins!")
                break
            elif is_draw():
                display_board()
                print("It's a draw!")
                break
            # Switch players
            current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()