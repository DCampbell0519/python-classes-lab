class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    
    def play_game(self):
        print('I love me some tic-tac-toe!')

    def print_board(self):
        board = self.board
        print(f"""
                A   B   C
            1)  {board['a1'] or ' '} | {board['b1'] or ' '} | {board['c1'] or ' '}
                ----------
            2)  {board['a2'] or ' '} | {board['b2'] or ' '} | {board['c2'] or ' '}
                ----------
            3)  {board['a3'] or ' '} | {board['b3'] or ' '} | {board['c3'] or ' '}
        """)
    
    def print_message(self):
        if self.tie:
            print('Tie Game!')
        elif self.winner:
            print(f'{self.winner} wins the game!')
        else: 
            print(f'It\'s player {self.turn}\'s turn!')

    def render(self):
        Game.play_game(self)
        Game.print_board(self)
        Game.print_message(self)
    
    def place_piece(self):
        move = input(f'Enter a valid move (example: A1): ').lower()
        while True:
            print(move)
            if ('a' or 'b' or 'c') and ('1' or '2' or '3') in move:
                print('Cowabunga!')
                break
            else: 
                print('Fuck you, try again.')
                print(move)
                break



tic_tac_toe = Game()
# tic_tac_toe.play_game()
# tic_tac_toe.print_board()
# tic_tac_toe.winner = 'X'
# tic_tac_toe.tie = True
# print(tic_tac_toe.winner)
# print(tic_tac_toe.tie)
# tic_tac_toe.print_message()
tic_tac_toe.render()
tic_tac_toe.place_piece()
