#! /usr/bin/env python
import fire
import mistontli
import random
import copy
import time

# TODO: Document everything


class Player:
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


class ClassicAIPlayer(Player):
    name = 'Mistontli Classical'

    def __init__(self, name, symbol):
        self.symbol = symbol

    def get_move(self, board):
        """ This gets the next AI move inside the board.

        According to the algorithm by Al Sweigart from the 2017 book "Invent
        your own computer games with python, 4th edition."
        """

        print('Thinking...')
        time.sleep(1)

        # Tries to win in the next turn
        for i in range(9):
            if board[i] == ' ':
                board_copy = copy.deepcopy(board)
                board_copy[i] = self.symbol

                if Mistontli._determine_winning(self.symbol, board_copy):
                    return i

        # Tries to block the player
        for i in range(9):
            if board[i] == ' ':
                board_copy = copy.deepcopy(board)
                board_copy[i] = self.opponents_symbol()

                if Mistontli._determine_winning(self.opponents_symbol(), board_copy):
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


class HumanPlayer(Player):

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


class Mistontli:
    """Main logic class. Has the game flow and auxiliary methods for the game."""

    def __init__(self):
        self._first_player = None
        self._second_player = None
        self._current_player = None
        self._active_game = True
        self._winner = None
        self._board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        # TODO: Investigate if this can be a class variable and point to
        # these functions.
        self._game_modes = {'vs': self._prepare_2_player_game,
                            'classicAI': self._prepare_classical_ai_game,
                            }

    @staticmethod
    def _determine_winning(letter, board):
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

    def _show_board(self):
        print(' - - -')
        for i, cell in enumerate(self._board):
            print('|{}'.format(cell), end='')
            if i % 3 == 2:
                print('|\n - - -')
        print('')

    def _prepare_2_player_game(self):
        """Creates two players asking their name. Randomly assigns a playable symbol."""
        first_player_name = input('Enter first player name: ')
        second_player_name = input('Enter second player name: ')

        coin_toss = round(random.uniform(0, 1))
        first_player_symbol = Player.symbols[coin_toss]
        second_player_symbol = Player.symbols[abs(1 - coin_toss)]

        self._first_player = HumanPlayer(first_player_name, first_player_symbol)
        self._second_player = HumanPlayer(second_player_name, second_player_symbol)

        self._current_player = self._first_player if self._first_player.symbol == 'X' else self._second_player

        print('{} you play with {}'.format(self._first_player.name, self._first_player.symbol))
        print('{} you play with {}'.format(self._second_player.name, self._second_player.symbol))
        print('{} you go first'.format(self._current_player.name))

    def _prepare_classical_ai_game(self):
        """Creates a human player and a classicAI player. Randomly assigns a playable symbol."""
        player_name = input('Enter your name: ')

        coin_toss = round(random.uniform(0, 1))
        player_symbol = Player.symbols[coin_toss]
        computer_symbol = Player.symbols[abs(1 - coin_toss)]

        self._first_player = HumanPlayer(player_name, player_symbol)
        self._second_player = ClassicAIPlayer('Mistontli', computer_symbol)

        self._current_player = self._first_player

        print('{} you play with {}'.format(self._first_player.name, self._first_player.symbol))
        print('I will play with {}'.format(self._second_player.name, self._second_player.symbol))
        print('You go first'.format(self._first_player.name))

    def _game_step(self):
        self._show_board()
        move = self._current_player.get_move(self._board)

        self._board[move] = self._current_player.symbol

        if Mistontli._determine_winning(self._current_player.symbol, self._board):
            self._active_game = False
            self._winner = True
            return

        if ' ' not in self._board:
            self._active_game = False

        self._current_player = self._second_player if self._current_player is self._first_player else self._first_player

    def start_game(self, mode='vs'):
        print('Welcome to Mistontli!')
        print('You are going to play in {} mode'.format(mode))
        self._game_modes[mode]()

        while self._active_game:
            self._game_step()

        self._show_board()
        if self._winner:
            print('{} you win!'.format(self._current_player.name))
        else:
            print('Draw!')

        print('Game has finished. Thanks for playing!')


if __name__ == '__main__':
    fire.Fire(mistontli.Mistontli)
