import random
import time
import copy

from utilities import determine_win


class BasePlayer:
    """Base player class, you can subclass this and override the 'get_move'
    method to implement your own type of player."""
    symbols = ['X', 'O']

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def opponents_symbol(self):
        if self.symbol == 'X':
            return 'O'
        return 'X'

    def get_move(self, board):
        raise NotImplementedError


class ClassicAIPlayer(BasePlayer):
    """This is a classical AI player, i.e., using a type of min-max algorithm."""
    name = 'Mistontli Classical'  # The default name of this AI.

    def __init__(self, name, symbol):
        self.symbol = symbol

    def get_move(self, board):
        """ This gets the next AI move inside the board.

        According to the algorithm by Al Sweigart from the 2017 book "Invent
        your own computer games with python, 4th edition."
        """

        print('Thinking...')
        time.sleep(1)

        # Tries to win this turn
        for i in range(9):
            if board[i] == ' ':
                board_copy = copy.deepcopy(board)
                board_copy[i] = self.symbol

                if determine_win(self.symbol, board_copy):
                    return i

        # Tries to block the player
        for i in range(9):
            if board[i] == ' ':
                board_copy = copy.deepcopy(board)
                board_copy[i] = self.opponents_symbol()

                if determine_win(self.opponents_symbol(), board_copy):
                    return i

        # Tries the corners randomly
        corners = [0, 2, 6, 8]
        random.shuffle(corners)
        for corner in corners:
            if board[corner] == ' ':
                return corner

        # Tries the center
        if board[4] == ' ':
            return 4

        # Tries the sides randomly
        sides = [1, 3, 5, 7]
        random.shuffle(sides)
        for side in sides:
            if board[side] == ' ':
                return side


class HumanPlayer(BasePlayer):
    """This is a human-based player. It will ask the next move through the terminal."""

    def get_move(self, board):
        move = input('{} pick your move (1 - 9): '.format(self.name))

        try:
            move = int(move)

            if board[move - 1] == ' ':
                return move - 1
            else:
                print('That cell is already filled!')
                return self.get_move(board)

        except ValueError:
            print('You should enter a number between 1 and 9')
            return self.get_move(board)
        except IndexError:
            print('You should enter a number between 1 and 9')
            return self.get_move(board)
