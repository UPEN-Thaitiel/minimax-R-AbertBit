# Constants for the game setup
BOARD_SIZE = 3       # The Tic-Tac-Toe board is 3x3
REWARD = 10          # Score for winning the game

class TicTacToe:
    def __init__(self, board):
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        print("Welcome to Tic-Tac-Toe!")
        print("You are 'O' and the computer is 'X'")
        print("Positions are numbered 1-9 from top-left to bottom-right")
        print("The computer will make the first move.\n")
        self.print_board()  # Mostrar el tablero inicial
    
        while True:
            self.move_computer()
            self.move_player()

    def print_board(self):
        print("\n")
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]} ")
        print("---+---+---")
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]} ")
        print("---+---+---")
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]} ")
        print("\n")

    def is_cell_free(self, position):
        return self.board[position] == ' '

    def update_player_position(self, player, position):
        if not self.is_cell_free(position):
            print(f"Position {position} is already taken!")
            if player == self.player:
                self.move_player()
            return False
        
        self.board[position] = player
        self.check_game_state()
        return True

    def check_game_state(self):
        self.print_board()
        
        if self.is_winning(self.computer):
            print("Computer wins!")
            exit()
        elif self.is_winning(self.player):
            print("Player wins!")
            exit()
        elif self.is_draw():
            print("It's a draw!")
            exit()

    def is_winning(self, player):
        # Check rows
        for i in range(1, 8, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                return True
        # Check columns
        for i in range(1, 4):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player:
                return True
        # Check diagonals
        if self.board[1] == self.board[5] == self.board[9] == player:
            return True
        if self.board[3] == self.board[5] == self.board[7] == player:
            return True
        return False

    def is_draw(self):
        for pos in self.board.values():
            if pos == ' ':
                return False
        return True

    def move_player(self):
        while True:
            try:
                position = int(input("\nEnter your move (1-9): "))
                if 1 <= position <= 9:
                    if self.is_cell_free(position):
                        self.board[position] = self.player
                        self.check_game_state()
                        break
                    else:
                        print("That position is already taken! Try again.")
                else:
                    print("Please enter a number between 1 and 9!")
            except ValueError:
                print("Please enter a valid number!")

    def move_computer(self):
        best_score = -float('inf')
        best_move = None
        
        for position in self.board:
            if self.is_cell_free(position):
                self.board[position] = self.computer
                score = self.minimax(0, -float('inf'), float('inf'), False)
                self.board[position] = ' '
                
                if score > best_score:
                    best_score = score
                    best_move = position
        
        self.update_player_position(self.computer, best_move)

    def minimax(self, depth, alpha, beta, is_maximizer):
        if self.is_winning(self.computer):
            return REWARD - depth
        if self.is_winning(self.player):
            return -REWARD + depth
        if self.is_draw():
            return 0

        if is_maximizer:
            best_score = -float('inf')
            for position in self.board:
                if self.is_cell_free(position):
                    self.board[position] = self.computer
                    score = self.minimax(depth + 1, alpha, beta, False)
                    self.board[position] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if alpha >= beta:
                        break
            return best_score
        else:
            best_score = float('inf')
            for position in self.board:
                if self.is_cell_free(position):
                    self.board[position] = self.player
                    score = self.minimax(depth + 1, alpha, beta, True)
                    self.board[position] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if alpha >= beta:
                        break
            return best_score


if __name__ == '__main__':
    board = {pos: ' ' for pos in range(1, 10)}
    game = TicTacToe(board)
    game.run()
