''' 
Implement Tic-Tac-Toe game using Python Object-Oriented Programming.
User vs computer game. 
'''

from player import HumanPlayer, ComputerRandomPlayer, ComputerAIPlayer

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
        # check if the field is empty and update (make move)
        if self._is_valid_move(position):
            self.board[position] = type
            return self.board
        return None

    def _is_empty_field(self):
        # check if there is any empty field on the board
        return ' ' in self.board.values()

    def available_moves(self):
        # return all available moves
        return [key for key in self.board.keys() if self.board[key]==' ']

    def is_winner(self, player):
        # check if the provided player wins
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

class Game:
    def __init__(self, choice):
        self.player_user = HumanPlayer(choice)
        self.player_comp = ComputerRandomPlayer('X') if choice == 'O' \
                            else ComputerRandomPlayer('O')
        self.current_winner = None
        self.board = Board()

    @staticmethod
    def print_valid_entries():
        '''Prints the valid inputs to play the game.'''
        print('''
            TL - top left    | TM - top middle    | TR - top right
            ML - middle left | MM - center        | MR - middle right
            BL - bottom left | BM - bottom middle | BR - bottom right''')

    def change_turn(self, player):
        if player is self.player_user:
            return self.player_comp
        else:
            return self.player_user

    def modify_board(self, position, type):
        return self.board.update_board(position, type)      

    def won_game(self, player):
        '''Returns True if the player won the game, False otherwise.'''
        if self.board.is_winner(player): self.current_winner = player.type
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

    while(game.board._is_empty_field()):
        game.board.print_board()
        position = player.get_move(game)  
        game.modify_board(position, player.type)
        
        if game.won_game(player):  
            # ends a loop and exits a game
            game.board.print_board()
            print(f'{player} is the Winner!')
            return 
        else:
            player = game.change_turn(player)
    
    print('Game over! It is a tie!')

if __name__ == '__main__':
    sign = player_initial_choice()
    play(sign)