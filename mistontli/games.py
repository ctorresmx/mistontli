import random

from players import HumanPlayer
from players import ClassicAIPlayer


class BaseGame:
    def prepare_game(self):
        raise NotImplementedError


class TwoPlayerGame(BaseGame):
    def prepare_game(self):
        """Creates two players asking their name. Randomly assigns a playable symbol."""
        first_player_name = input('Enter first player name: ')
        second_player_name = input('Enter second player name: ')

        coin_toss = round(random.uniform(0, 1))
        first_player_symbol = HumanPlayer.symbols[coin_toss]
        second_player_symbol = HumanPlayer.symbols[abs(1 - coin_toss)]

        first_player = HumanPlayer(first_player_name, first_player_symbol)
        second_player = HumanPlayer(second_player_name, second_player_symbol)

        current_player = first_player if first_player.symbol == 'X' else second_player

        return first_player, second_player, current_player


class ClassicAIGame(BaseGame):
    def prepare_game(self):
        """Creates a human player and a classicAI player. Randomly assigns a playable symbol."""
        player_name = input('Enter your name: ')

        coin_toss = round(random.uniform(0, 1))
        player_symbol = HumanPlayer.symbols[coin_toss]
        computer_symbol = ClassicAIPlayer.symbols[abs(1 - coin_toss)]

        first_player = HumanPlayer(player_name, player_symbol)
        classic_ai_player = ClassicAIPlayer('Mistontli', computer_symbol)

        return first_player, classic_ai_player, first_player
