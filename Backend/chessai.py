import random
import chess
import numpy
import time
import pygame
# import tensorflow.keras.models as models
# import tensorflow
from keras.models import load_model

squares_index = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7
}

model = load_model('E:\\ninja_chess-master\\Backend\\model.h5')
class Solve ():
    def square_to_index(seft,square):
        letter = chess.square_name(square)
        return 8 - int(letter[1]), squares_index[letter[0]]

    def split_dims(seft, board):
        # this is the 3d matrix
        board3d = numpy.zeros((14, 8, 8), dtype=numpy.int8)

        # here we add the pieces's view on the matrix
        for piece in chess.PIECE_TYPES:
            for square in board.pieces(piece, chess.WHITE):
                idx = numpy.unravel_index(square, (8, 8))
                board3d[piece - 1][7 - idx[0]][idx[1]] = 1
            for square in board.pieces(piece, chess.BLACK):
                idx = numpy.unravel_index(square, (8, 8))
                board3d[piece + 5][7 - idx[0]][idx[1]] = 1

        # add attacks and valid moves too
        # so the network knows what is being attacked
        aux = board.turn
        board.turn = chess.WHITE
        for move in board.legal_moves:
            i, j = seft.square_to_index(move.to_square)
            board3d[12][i][j] = 1
        board.turn = chess.BLACK
        for move in board.legal_moves:
            i, j = seft.square_to_index(move.to_square)
            board3d[13][i][j] = 1
        board.turn = aux

        return board3d

    def minimax_eval(seft,board):

        board3d = seft.split_dims(board)
        board3d = numpy.expand_dims(board3d, 0)
        return model.predict(board3d)[0][0]

    def minimax(seft,board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            return seft.minimax_eval(board)

        if maximizing_player:
            max_eval = -numpy.inf
            for move in board.legal_moves:
                board.push(move)
                eval = seft.minimax(board, depth - 1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = numpy.inf
            for move in board.legal_moves:
                board.push(move)
                eval = seft.minimax(board, depth - 1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_ai_move_ai(seft,board, depth):
        max_move = None
        max_eval = -numpy.inf

        for move in board.legal_moves:
            board.push(move)
            eval = seft.minimax(board, depth - 1, -numpy.inf, numpy.inf, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                max_move = move

        return max_move
    def get_ai_move(seft, board):
      return seft.get_ai_move_ai(board,1)
