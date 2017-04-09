#! /usr/bin/env python
import fire
import mistontli
import random
import copy

# TODO: Make big refactor for all this mess


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

    @classmethod
    def players_ai_creator(cls):
        """Creates two players asking their name. Randomly assigns a playable symbol."""
        player_name = input('Enter your name: ')

        coin_toss = round(random.uniform(0, 1))
        player_symbol = cls.symbols[coin_toss]
        computer_symbol = cls.symbols[abs(1 - coin_toss)]

        player = cls(player_name, player_symbol)
        computer = cls('Mistontli', computer_symbol)

        return player, computer

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Mistontli:
    """Main logic class. Has the game flow and auxiliary methods for the game."""

    def __init__(self):
        self.first_player = None
        self.second_player = None
        self.current_player = None
        self.active_game = True
        self.winner = None
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def _get_next_move(self):
        """ This gets the next AI move inside the board.

        According to the algorithm by Al Sweigart from the 2017 book "Invent
        your own computer games with python, 4th edition."
        """

        # Tries to win in the next turn
        for i in range(9):
            if self.board[i] == ' ':
                board = copy.deepcopy(self.board)
                board[i] = self.second_player.symbol

                if self._determine_winning(self.second_player.symbol, board):
                    return i

        # Tries to block the player
        for i in range(9):
            if self.board[i] == ' ':
                board = copy.deepcopy(self.board)
                board[i] = self.first_player.symbol

                if self._determine_winning(self.first_player.symbol, board):
                    return i

        # Tries the corners randomly
        corners = [0, 2, 6, 8]
        random.shuffle(corners)
        for corner in corners:
            if self.board[corner] == ' ':
                return corner

        # Tries the center
        if self.board[4] == ' ':
            return 4

        # Tries the sides randomly
        sides = [1, 3, 5, 7]
        random.suffle(sides)
        for side in sides:
            if self.board[side] == ' ':
                return side

    def _determine_winning(self, letter, board=None):
        if not board:
            board = self.board

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

    def _prepare_ai_game(self):
        self.first_player, self.second_player = Player.players_ai_creator()
        self.current_player = self.first_player

    def _game_step(self):
        self._show_board()
        self._get_move(self.current_player)

        if self._determine_winning(self.current_player.symbol):
            self.active_game = False
            self.winner = True
            return

        if ' ' not in self.board:
            self.active_game = False

        self.current_player = self.second_player if self.current_player is self.first_player else self.first_player

    def _ai_game_step(self):
        self._show_board()

        if self.current_player is self.first_player:
            self._get_move(self.current_player)
        else:
            print(self._get_next_move())
            self.board[self._get_next_move()] = self.second_player.symbol

        if self._determine_winning(self.current_player.symbol):
            self.active_game = False
            self.winner = True
            return

        if ' ' not in self.board:
            self.active_game = False

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
        if self.winner:
            print('{} you win!'.format(self.current_player.name))
        else:
            print('Draw!')

        print('Game has finished. Thanks for playing!')

    def start_ai_game(self):
        print('Welcome to Mistontli!')
        self._prepare_ai_game()
        print('{} you play with {}'.format(self.first_player.name, self.first_player.symbol))
        print('I will play with {}'.format(self.second_player.name, self.second_player.symbol))
        print('You go first'.format(self.first_player.name))

        while self.active_game:
            self._ai_game_step()

        self._show_board()
        if self.winner:
            if self.current_player is self.first_player:
                print('You win!')
            else:
                print('You lose!')
        else:
            print('Draw!')

        print('Game has finished. Thanks for playing!')


if __name__ == '__main__':
    fire.Fire(mistontli.Mistontli)
