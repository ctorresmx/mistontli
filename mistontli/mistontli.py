#! /usr/bin/env python
import fire
import mistontli

from games import TwoPlayerGame
from games import ClassicAIGame

from utilities import determine_win


class Mistontli:
    """Main logic class. Has the game flow and auxiliary methods for the game."""

    def __init__(self):
        self._first_player = None
        self._second_player = None
        self._current_player = None
        self._active_game = True
        self._winner = None
        self._game = None
        self._mode = None
        self._board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        self._game_modes = {'vs': TwoPlayerGame,
                            'classicAI': ClassicAIGame,
                            }

    def _show_board(self):
        """Shows the board as a 2D representation out of a 1D array."""
        print(' - - -')
        for i, cell in enumerate(self._board):
            print('|{}'.format(cell), end='')
            if i % 3 == 2:
                print('|\n - - -')
        print('')

    def _prepare_game(self, mode):
        self._mode = mode
        print('You are going to play in {} mode'.format(self._mode))
        self._game = self._game_modes[self._mode]()
        self._first_player, self._second_player, self._current_player = self._game.prepare_game()

        print('{} you play with {}'.format(self._first_player.name,
                                           self._first_player.symbol))

        print('{} you play with {}'.format(self._second_player.name,
                                           self._second_player.symbol))

        print('{} you go first'.format(self._current_player.name))

    def _game_step(self):
        """This is the main game loop. It should be called as long as the game
        is active."""
        self._show_board()
        move = self._current_player.get_move(self._board)

        self._board[move] = self._current_player.symbol

        if determine_win(self._current_player.symbol, self._board):
            self._active_game = False
            self._winner = True
            return

        if ' ' not in self._board:
            self._active_game = False

        if self._current_player is self._first_player:
            self._current_player = self._second_player
        else:
            self._current_player = self._first_player

    def start_game(self, mode='vs'):
        """Entry point for Fire.

        There are two kinds of game at this point:
            - 2 players a.k.a. 'vs'
            - Classic AI a.k.a. 'classicAI'
        """
        print('Welcome to Mistontli!')
        self._prepare_game(mode)

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
