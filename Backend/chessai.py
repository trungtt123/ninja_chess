import random
import chess
import numpy

class Solve ():
    def get_ai_move(self, board):
        depth = random.randrange(3,6)
        return self.minimax(board, depth, 0, 5000, True)[0]

    def whiteScore(self, board):
        S = 0
        for i in range(97, 105):
            for j in range(1, 9):
                pos = chr(i) + str(j)
                piece = str(board.piece_at(chess.parse_square(pos)))
                if (piece == "P"): S += 10
                if (piece == "N"): S += 30
                if (piece == "B"): S += 30
                if (piece == "R"): S += 50
                if (piece == "Q"): S += 90
                if (piece == "K"): S += 100
        return S

    def blackScore(self, board):
        S = 0
        for i in range(97, 105):
            for j in range(1, 9):
                pos = chr(i) + str(j)
                piece = str(board.piece_at(chess.parse_square(pos)))
                if (piece == "p"): S += 10
                if (piece == "n"): S += 30
                if (piece == "b"): S += 30
                if (piece == "r"): S += 50
                if (piece == "q"): S += 90
                if (piece == "k"): S += 100
        return S

    def evaluate(self, board):
        return self.blackScore(board) - self.whiteScore(board)

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            return None, self.evaluate(board)

        if maximizing_player == True:
            max_eval = -numpy.inf
            moves = list(board.legal_moves)
            best_move = moves[0]
            for move in moves:
                board.push(move)
                temp_eval = self.minimax(board, depth - 1, alpha, beta, False)[1]
                board.pop()
                if temp_eval >= max_eval:
                    if temp_eval == max_eval:
                        choice = random.randrange(0,2,1)
                        if(choice == 0): best_move = move
                    else:
                        best_move = move
                    max_eval = temp_eval

                alpha = max(temp_eval, alpha)
                if beta <= alpha:
                    break
            return best_move, max_eval
        else:
            min_eval = numpy.inf
            moves = list(board.legal_moves)
            best_move = moves[0]
            for move in moves:
                board.push(move)
                temp_eval = self.minimax(board, depth - 1, alpha, beta, True)[1]
                board.pop()
                if temp_eval <= min_eval:
                    if temp_eval == min_eval:
                        choice = random.randrange(0, 2, 1)
                        if (choice == 0): best_move = move
                    else:
                        best_move = move
                    min_eval = temp_eval

                beta = min(temp_eval, beta)
                if beta <= alpha:
                    break
            return best_move, min_eval



