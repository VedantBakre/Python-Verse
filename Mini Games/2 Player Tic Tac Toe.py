def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
            
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True
        
    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row col): ")
            row, col = map(int, move.split())
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    print("Welcome to Tic Tac Toe!")
    print("Enter coordinates as: row col (e.g., 0 0 for top left)")
    
    while True:
        print_board(board)
        player = players[turn % 2]
        
        row, col = get_move(player)
        
        if board[row][col] != " ":
            print("That spot is already taken!")
            continue
            
        board[row][col] = player
        
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
            
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
            
        turn += 1

if __name__ == "__main__":
    main()
