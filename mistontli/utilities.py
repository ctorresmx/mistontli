def determine_win(letter, board):
    """Determine if the given symbol (player) will win on the given board."""
    return ((board[0] == letter and board[1] == letter and
             board[2] == letter) or  # Top
            (board[3] == letter and board[4] == letter and
             board[5] == letter) or  # Middle
            (board[6] == letter and board[7] == letter and
             board[8] == letter) or  # Bottom
            (board[0] == letter and board[3] == letter and
             board[6] == letter) or  # Left
            (board[1] == letter and board[4] == letter and
             board[7] == letter) or  # Center
            (board[2] == letter and board[5] == letter and
             board[8] == letter) or  # Right
            (board[0] == letter and board[4] == letter and
             board[8] == letter) or  # Diagonal Left-Right
            (board[2] == letter and board[4] == letter and
             board[6] == letter)  # Diagonal Right-Left
            )
