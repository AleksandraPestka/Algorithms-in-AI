import random

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
        
        while not valid_position:
            position = input(f"{self.__str__()} turn, what's your move? ")
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