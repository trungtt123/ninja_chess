import random
import chess
import numpy
import time
import pygame
import tensorflow.keras.models as models
import tensorflow

# # with arg_scope([layers.conv2d], activation_fn=self.activation_fn, data_format="NCHW"), \
# # arg_scope([layers.fully_connected], activation_fn=self.activation_fn):
# #with arg_scope([layers.conv2d], activation_fn=self.activation_fn, data_format="NHWC"), \
# #        arg_scope([layers.fully_connected], activation_fn=self.activation_fn):

model = models.load_model("D:/PythonProject/ninja_chess/Backend/model.h5")
#with tensorflow.device('/cpu:0'):
#     model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['acc'])

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

class Solve():
    # example: h3 -> 17
    def get_ai_move(self, board, level, first_player):
        maximizing_player = False
        if first_player == "BLACK":
            maximizing_player = True
        if level == 2:
            return self.minimax(board, random.randrange(3,5,1), 0, 100000, maximizing_player, level)[0]
        if level == 3:
            return self.minimax(board, 1, 0, 1, maximizing_player, level)[0]
        return self.minimax(board, random.randrange(2,4,1), 0, 100000, maximizing_player, level)[0]

    def square_to_index(self, board):
         letter = chess.square_name(board)
         return 8 - int(letter[1]), squares_index[letter[0]]

    def split_dims(self, board):
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
             i, j = self.square_to_index(move.to_square)
             board3d[12][i][j] = 1
         board.turn = chess.BLACK
         for move in board.legal_moves:
             i, j = self.square_to_index(move.to_square)
             board3d[13][i][j] = 1
         board.turn = aux

         return board3d

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

    def evaluate(self, board, level):
        if level == 3:
            board3d = self.split_dims(board)
            board3d = numpy.expand_dims(board3d, 0)
            return model.predict(board3d)[0][0]
        return self.whiteScore(board) - self.blackScore(board)

    def minimax(self, board, depth, alpha, beta, maximizing_player, level):
        if depth == 0 or board.is_game_over():
            return None, self.evaluate(board, level)
        if maximizing_player == True:
            max_eval = -numpy.inf
            moves = list(board.legal_moves)
            best_move = moves[0]
            for move in moves:
                board.push(move)
                temp_eval = self.minimax(board, depth - 1, alpha, beta, False, level)[1]
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
                temp_eval = self.minimax(board, depth - 1, alpha, beta, True, level)[1]
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
"""
def random_board(max_depth=200):
  board = chess.Board()
  depth = random.randrange(0, max_depth)

  for _ in range(depth):
    all_moves = list(board.legal_moves)
    random_move = random.choice(all_moves)
    board.push(random_move)
    if board.is_game_over():
      break

  return board


board = random_board()
print(board)
s = Solve()
board3d = s.split_dims(board)
print(board3d), print()
board3d = numpy.expand_dims(board3d, 0)
#print(board3d)
print(model.predict(board3d)[0][0])
"""