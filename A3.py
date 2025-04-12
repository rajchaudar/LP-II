import itertools

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]  
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != ' ':
            return board[condition[0]]
    return None

def heuristic(board, player):
    opponent = 'O' if player == 'X' else 'X'
    score = 0
    
    for condition in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        values = [board[i] for i in condition]
        if values.count(player) == 2 and values.count(' ') == 1:
            score += 10
        elif values.count(opponent) == 2 and values.count(' ') == 1:
            score -= 10
    
    return score

def get_available_moves(board):
    return [i for i, cell in enumerate(board) if cell == ' ']

def a_star_search(board, player):
    open_set = [(board, 0)]
    best_move = None
    max_score = float('-inf')
    
    for move in get_available_moves(board):
        new_board = board[:]
        new_board[move] = player
        score = heuristic(new_board, player)
        if score > max_score:
            max_score = score
            best_move = move
    
    return best_move

def tic_tac_toe():
    board = [' '] * 9
    players = itertools.cycle(['X', 'O'])
    
    while True:
        player = next(players)
        if player == 'X': 
            move = a_star_search(board, player)
            if move is not None:
                board[move] = player
        else: 
            move = int(input("Enter your move (0-8): "))
            if board[move] == ' ':
                board[move] = player
            else:
                print("Invalid move, try again.")
                continue
        
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        elif ' ' not in board:
            print("It's a draw!")
            break

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")
    print("\n")

if __name__ == "__main__":
    tic_tac_toe()
