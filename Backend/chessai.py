import random
import chess

class Solve ():
    def get_ai_move(self, board):
        moves = list(board.legal_moves)
        return random.choice(moves)
