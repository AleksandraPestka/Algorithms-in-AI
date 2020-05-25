''' Implement Tic-Tac-Toe game using Python Object-Oriented Programming.
User vs computer game. Strategy: Minimax Algorithm.
'''

import random

class Board:
    def __init__(self):
        ''' Define the game board. '''
        self.board = {
            'TL':' ', 'TM':' ', 'TR':' ',
            'ML':' ', 'MM':' ', 'MR':' ',
            'BL':' ', 'BM':' ', 'BR':' ',
        }

    def print_board(self):
        print('\n')
        print(self.board['TL'] + '|' + self.board['TM'] + '|' + self.board['TR'])
        print('--' * 3)
        print(self.board['ML'] + '|' + self.board['MM'] + '|' + self.board['MR'])
        print('--' * 3)
        print(self.board['BL'] + '|' + self.board['BM'] + '|' + self.board['BR'])
        print('\n')

    def _is_valid_move(self, position):
        if self.board[position] == ' ':
            return True
        return False

    def update_board(self, position, type):
        # check if the field is empty and update 
        if self._is_valid_move(position):
            self.board[position] = type
            return self.board
        return None

    def is_winner(self, player):
        player_type = player.type
        combinations = [
            # horizontal 
            ["TL", "TM", "TR"],
            ["ML", "MM", "MR"],
            ["BL", "BM", "BR"],
            # vertical
            ["TL", "ML", "BL"],
            ["TM", "MM", "BM"],
            ["TR", "MR", "BR"],
            # diagonal
            ["TL", "MM", "BR"],
            ["BL", "MM", "TR"]
        ]

        for a, b, c in combinations:
            if self.board[a] == self.board[b] == self.board[c] == player_type:
                return True
        return False

class Player:
    '''Represents one player.'''
    def __init__(self, type):
        '''Initializes a player with type X or O.'''
        self.type = type

    def __str__(self):
        return 'Player {}'.format(self.type)

class Game:
    def __init__(self, choice):
        self.player_user = Player(choice)
        if choice == 'O': self.player_comp = Player('X')
        else: self.player_comp = Player('O')
        self.board = Board()

    def print_valid_entries(self):
        '''Prints the valid inputs to play the game.'''
        print('''
            TL - top left    | TM - top middle    | TR - top right
            ML - middle left | MM - center        | MR - middle right
            BL - bottom left | BM - bottom middle | BR - bottom right''')

    def print_board(self):
        self.board.print_board()

    def change_turn(self, player):
        if player is self.player_user:
            return self.player_comp
        else:
            return self.player_user

    def draw_position_by_computer(self, type):
        while(True):
            position = random.choice(list(self.board.board.keys()))
            if self.board.update_board(position, type) is not None:
                return self.board.update_board(position, type)        

    def modify_board(self, position, type):
        while(True):
            if ((position in self.board.board) and 
                (self.board.update_board(position, type) is not None)):
                break 
            else:
                position = input('Position is not valid. Try again: ')

        return self.board.update_board(position, type)

    def won_game(self, player):
        '''Returns True if the player won the game, False otherwise.'''
        return self.board.is_winner(player)

def player_initial_choice():
    print('Welcome to TIC-TAC-TOE game!')

    # human draw
    while True:
        sign = input('Choose X or O: ')
        if sign == 'X' or sign == 'O':
            break
        else:
            print('Provide correct character!')

    return sign

def play(choice):
    game = Game(choice)
    game.print_valid_entries()
    # choose user as the first player
    player = game.player_user

    # 9 iterations
    for it in range(9):
        game.print_board()
        if player == game.player_user:
            position = input(f"{player} turn, what's your move? ")
            game.modify_board(position, player.type)
        else:
            game.draw_position_by_computer(player.type)
        
        if game.won_game(player):  
            game.print_board()
            print(f'{player} is the Winner!')
            break
        else:
            player = game.change_turn(player)

        if it == 8:
            print('Game over! It is a tie!')

if __name__ == '__main__':
    sign = player_initial_choice()
    play(sign)