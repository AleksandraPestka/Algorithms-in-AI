import random
import math
import copy

class Player:
    '''Represents one player.'''
    def __init__(self, type):
        '''Initializes a player with type X or O.'''
        self.type = type

    def __str__(self):
        return 'Player {}'.format(self.type)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, type):
        super().__init__(type)

    def get_move(self, game):
        valid_position = False
        position = input(f"{self.__str__()} turn, what's your move? ")

        while not valid_position:
            if position in game.board.available_moves():
                valid_position = True 
            else:
                position = input('Position is not valid. Try again: ')
        
        return position

class ComputerRandomPlayer(Player):
    def __init__(self, type):
        super().__init__(type)

    def get_move(self, game):
        return random.choice(game.board.available_moves())

class ComputerAIPlayer(Player):
    def __init__(self, type):
        super().__init__(type)

    def get_move(self, game):
        if len(game.board.available_moves()) == 9:
            # take the first step randomly 
            position = random.choice(game.board.available_moves())
        else:
            position = self.minimax(game, self.type)['position']
        return position

    def minimax(self, game, player_type):
        # define minimizer and maximizer
        max_player = self.type
        min_player = 'O' if player_type == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if game.current_winner == min_player:
            return {
                'position': None, 
                'score': 1 * (len(game.board.available_moves()) + 1) \
                    if min_player == max_player \
                    else -1 * (len(game.board.available_moves()) + 1)
                }
        elif not game.board._is_empty_field():
            return {'position': None, 'score': 0}

        if player_type == max_player:
            # each score should maximize
            best = {'position': None, 'score': -math.inf}
        else: 
            # each score should be minimize
            best = {'position': None, 'score': math.inf}

        for possible_move in game.board.available_moves():
            # make a move
            game.modify_board(possible_move, player_type)
            possible_score = self.minimax(game, min_player)

            # undo moves
            game.board.board[possible_move] = ' '
            game.current_winner = None
            possible_score['position'] = possible_move

            if player_type == max_player:
                if possible_score['score'] > best['score']:
                    best = possible_score
            else:
                if possible_score['score'] < best['score']:
                    best = possible_score

        return best