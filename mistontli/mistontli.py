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
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __init__(self):
        self.first_player = None
        self.second_player = None
        self.current_player = None
        self.active_game = True

    def _determine_winning(self, letter):
        return ((self.board[0] == letter and self.board[1] == letter and
                 self.board[2] == letter) or  # Top
                (self.board[3] == letter and self.board[4] == letter and
                 self.board[5] == letter) or  # Middle
                (self.board[6] == letter and self.board[7] == letter and
                 self.board[8] == letter) or  # Bottom
                (self.board[0] == letter and self.board[3] == letter and
                 self.board[6] == letter) or  # Left
                (self.board[1] == letter and self.board[4] == letter and
                 self.board[7] == letter) or  # Center
                (self.board[2] == letter and self.board[5] == letter and
                 self.board[8] == letter) or  # Right
                (self.board[0] == letter and self.board[4] == letter and
                 self.board[8] == letter) or  # Diagonal Left-Right
                (self.board[2] == letter and self.board[4] == letter and
                 self.board[6] == letter)  # Diagonal Right-Left
                )

    def _show_board(self):
        print(' - - -')
        for i, cell in enumerate(self.board):
            print('|{}'.format(cell), end='')
            if i % 3 == 2:
                print('|\n - - -')
        print('')

    def _get_move(self, player):
        """Given a player, asks for a possible board move."""

        move = input('{} pick your move (1 - 9): '.format(player.name))

        try:
            move = int(move)
        except ValueError:
            print('You should enter a number between 1 and 9')
            return self._get_move(player)

        if self.board[move - 1] == ' ':
            self.board[move - 1] = player.symbol
        else:
            print('That cell is already filled!')
            return self._get_move(player)

    def _prepare_game(self):
        self.first_player, self.second_player = Player.players_creator()
        self.current_player = self.first_player if self.first_player.symbol == 'X' else self.second_player

    def _game_step(self):
        self._show_board()
        self._get_move(self.current_player)

        if self._determine_winning(self.current_player.symbol):
            self.active_game = False
            return

        self.current_player = self.second_player if self.current_player is self.first_player else self.first_player

    def start_game(self):
        print('Welcome to Mistontli!')
        self._prepare_game()
        print('{} you play with {}'.format(self.first_player.name, self.first_player.symbol))
        print('{} you play with {}'.format(self.second_player.name, self.second_player.symbol))
        print('{} you go first'.format(self.current_player.name))

        while self.active_game:
            self._game_step()

        self._show_board()
        print('{} you win!'.format(self.current_player.name))
        print('Game has finished. Thanks for playing!')


if __name__ == '__main__':
    fire.Fire(mistontli.Mistontli)
