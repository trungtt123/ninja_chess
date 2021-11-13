import chess
import numpy

def whiteScore(board):
    S = 0
    for i in range(97, 105):
        for j in range(1, 9):
            pos = chr(i) + str(j)
            piece = str(board.piece_at(chess.parse_square(pos)))
            if(piece == "P"): S+=40
            if(piece == "N"): S+=100
            if(piece == "B"): S+=100
            if(piece == "R"): S+=200
            if(piece == "Q"): S+=400
            if(piece == "K"): S+=500
    return S

def blackScore(board):
    S = 0
    for i in range(97, 105):
        for j in range(1, 9):
            pos = chr(i) + str(j)
            piece = str(board.piece_at(chess.parse_square(pos)))
            if(piece == "p"): S+=40
            if(piece == "n"): S+=100
            if(piece == "b"): S+=100
            if(piece == "r"): S+=200
            if(piece == "q"): S+=400
            if(piece == "k"): S+=500
    return S

def evaluate(board):
    return whiteScore(board) - blackScore(board)

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return None, evaluate(board) 

    if maximizing_player == True:
        max_eval = -numpy.inf
        moves = list(board.legal_moves)
        for move in moves:
            board.push(move)
            temp_eval = minimax(board ,depth-1, alpha, beta, False)[1]
            board.pop()
            if temp_eval > max_eval:
                max_eval = temp_eval
                best_move = move
            alpha  = max(temp_eval, alpha)
            if beta <= alpha: 
                break
        return best_move, max_eval
    else:
        min_eval = numpy.inf
        moves = list(board.legal_moves)
        for move in moves:
            board.push(move)
            temp_eval = minimax(board ,depth-1, alpha, beta, True)[1]
            board.pop()
            if temp_eval < min_eval:
                min_eval = temp_eval
                best_move = move
            beta = min(temp_eval, beta)
            if beta <= alpha: 
                break
        return best_move, min_eval
