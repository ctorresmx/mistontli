#! /usr/bin/env python
import fire
import mistontli
import random


class Player:
    symbols = ['X', 'O']

    @classmethod
    def players_creator(cls):
        """Creates two players asking their name. Randomly assigns a playable symbol."""
        first_player_name = input('Enter first player name: ')
        second_player_name = input('Enter second player name: ')

        coin_toss = round(random.uniform(0, 1))
        first_player_symbol = cls.symbols[coin_toss]
        second_player_symbol = cls.symbols[abs(1 - coin_toss)]

        first_player = cls(first_player_name, first_player_symbol)
        second_player = cls(second_player_name, second_player_symbol)

        return first_player, second_player

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Mistontli:
    """Main logic class. Has the game flow and auxiliary methods for the game."""
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    number_of_moves = 9
    current_player = None

    def _show_board(self):
        # TODO: Refactor this method, it could probably be less convoluted.
        for line in self.board:
            print('|', end='')
            for square in line:
                print(square, end='|')
            print('\n - - -')

    def _get_move(self, player):
        """Given a player, asks for a possible board move."""

        # TODO: This could be improved with a more robust way to determine if the
        # move is a legal one (not repeated or out of bounds).
        move = input('{} pick your move (Enter the number of the square to play): '.format(player.name))
        move = int(move)

        if move <= 3:
            self.board[0][(move % 3) - 1] = player.symbol
        elif move >= 7:
            self.board[2][(move % 3) - 1] = player.symbol
        else:
            self.board[1][(move % 3) - 1] = player.symbol

        self.number_of_moves -= 1

    def start_game(self):
        # TODO: Refactor all of this into auxiliary methods. Auxiliary methods
        # should be so decoupled that you could change the start_game loop for
        # something else, like a GUI.
        print('Welcome to Mistontli!')

        first_player, second_player = Player.players_creator()

        print('Welcome {} and {}!'.format(first_player.name, second_player.name))
        print('{} you play with {}'.format(first_player.name, first_player.symbol))
        print('{} you play with {}'.format(second_player.name, second_player.symbol))

        current_player = first_player if first_player.symbol == 'X' else second_player

        print('{} you go first'.format(current_player.name))

        while self.number_of_moves > 0:
            self._show_board()
            self._get_move(current_player)

            current_player = second_player if current_player is first_player else first_player

        # TODO: Think of a way to remove the need of calling the _show_board out
        # of the main loop.
        self._show_board()

        print('Game has finished. Thanks for playing!')


if __name__ == '__main__':
    fire.Fire(mistontli.Mistontli)
