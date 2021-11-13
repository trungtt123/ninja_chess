import pygame
from pygame import draw
import button
import random
import chess
import chessai
import time

# create display window

# board = chess.Board()
class PlayScreen():
    def run():
        board = chess.Board()
        SCREEN_HEIGHT = 600
        SCREEN_WIDTH = 1000
        positionPiece = {
            'a8': (5, 5), 'b8': (65, 5), 'c8': (125, 5), 'd8': (185, 5), 'e8': (245, 5), 'f8': (305, 5), 'g8': (365, 5), 'h8': (425, 5),
            'a7': (5, 65), 'b7': (65, 65), 'c7': (125, 65), 'd7': (185, 65), 'e7': (245, 65), 'f7': (305, 65), 'g7': (365, 65), 'h7': (425, 65),
            'a6': (5, 125), 'b6': (65, 125), 'c6': (125, 125), 'd6': (185, 125), 'e6': (245, 125), 'f6': (305, 125), 'g6': (365, 125), 'h6': (425, 125),
            'a5': (5, 185), 'b5': (65, 185), 'c5': (125, 185), 'd5': (185, 185), 'e5': (245, 185), 'f5': (305, 185), 'g5': (365, 185), 'h5': (425, 185),
            'a4': (5, 245), 'b4': (65, 245), 'c4': (125, 245), 'd4': (185, 245), 'e4': (245, 245), 'f4': (305, 245), 'g4': (365, 245), 'h4': (425, 245),
            'a3': (5, 305), 'b3': (65, 305), 'c3': (125, 305), 'd3': (185, 305), 'e3': (245, 305), 'f3': (305, 305), 'g3': (365, 305), 'h3': (425, 305),
            'a3': (5, 305), 'b3': (65, 305), 'c3': (125, 305), 'd3': (185, 305), 'e3': (245, 305), 'f3': (305, 305), 'g3': (365, 305), 'h3': (425, 305),
            'a2': (5, 365), 'b2': (65, 365), 'c2': (125, 365), 'd2': (185, 365), 'e2': (245, 365), 'f2': (305, 365), 'g2': (365, 365), 'h2': (425, 365),
            'a1': (5, 425), 'b1': (65, 425), 'c1': (125, 425), 'd1': (185, 425), 'e1': (245, 425), 'f1': (305, 425), 'g1': (365, 425), 'h1': (425, 425),
        }


        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Chess AI')

        #load piece
        #----------black piece-------------
        blackKing = pygame.image.load('images/chess/Chess_Pieces_Green/King/King_shadow.png').convert_alpha()
        blackKing = pygame.transform.scale(blackKing, (70, 70))

        blackQueen = pygame.image.load('images/chess/Chess_Pieces_Green/Queen/Queen_shadow.png').convert_alpha()
        blackQueen = pygame.transform.scale(blackQueen, (70, 70))

        blackBishop = pygame.image.load('images/chess/Chess_Pieces_Green/Bishop/Bishop_shadow.png').convert_alpha()
        blackBishop = pygame.transform.scale(blackBishop, (70, 70))

        blackKnight = pygame.image.load('images/chess/Chess_Pieces_Green/Knight/Knight_shadow.png').convert_alpha()
        blackKnight = pygame.transform.scale(blackKnight, (70, 70))
        
        blackRook = pygame.image.load('images/chess/Chess_Pieces_Green/Rook/Rook_shadow.png').convert_alpha()
        blackRook = pygame.transform.scale(blackRook, (70, 70))
        
        blackPawn = pygame.image.load('images/chess/Chess_Pieces_Green/Pawn/Pawn_shadow.png').convert_alpha()
        blackPawn = pygame.transform.scale(blackPawn, (70, 70))

        #-----------white piece----------------


        whiteKing = pygame.image.load('images/chess/Chess_Pieces_Golden/King/King_shadow.png').convert_alpha()
        whiteKing = pygame.transform.scale(whiteKing, (70, 70))

        whiteQueen = pygame.image.load('images/chess/Chess_Pieces_Golden/Queen/Queen_shadow.png').convert_alpha()
        whiteQueen = pygame.transform.scale(whiteQueen, (70, 70))

        whiteBishop = pygame.image.load('images/chess/Chess_Pieces_Golden/Bishop/Bishop_shadow.png').convert_alpha()
        whiteBishop = pygame.transform.scale(whiteBishop, (70, 70))

        whiteKnight = pygame.image.load('images/chess/Chess_Pieces_Golden/Knight/Knight_shadow.png').convert_alpha()
        whiteKnight = pygame.transform.scale(whiteKnight, (70, 70))
        
        whiteRook = pygame.image.load('images/chess/Chess_Pieces_Golden/Rook/Rook_shadow.png').convert_alpha()
        whiteRook = pygame.transform.scale(whiteRook, (70, 70))
        
        whitePawn = pygame.image.load('images/chess/Chess_Pieces_Golden/Pawn/Pawn_shadow.png').convert_alpha()
        whitePawn = pygame.transform.scale(whitePawn, (70, 70))

        #update board

        def update_board(board):
            chess_board_img = pygame.image.load('images/chess/Chess_board/Chessboard.png').convert_alpha()
            chess_board_img = pygame.transform.scale(chess_board_img, (500, 500))
            for i in range(97, 105):
                for j in range(1, 9):
                    pos = chr(i) + str(j)
                    piece = str(board.piece_at(chess.parse_square(pos)))
                    if (piece == 'K'):
                        chess_board_img.blit(whiteKing, (positionPiece[pos][0], positionPiece[pos][1]))
                    if (piece == 'k'):
                        chess_board_img.blit(blackKing, (positionPiece[pos][0], positionPiece[pos][1]))
                    if (piece == 'Q'):
                        chess_board_img.blit(whiteQueen, (positionPiece[pos][0], positionPiece[pos][1]))
                    if (piece == 'q'):
                        chess_board_img.blit(blackQueen, (positionPiece[pos][0], positionPiece[pos][1]))
                    if (piece == 'N'):
                        chess_board_img.blit(whiteKnight, (positionPiece[pos][0], positionPiece[pos][1]))
                    if (piece == 'n'):
                        chess_board_img.blit(blackKnight, (positionPiece[pos][0], positionPiece[pos][1]))
                    if (piece == 'B'):
                        chess_board_img.blit(whiteBishop, (positionPiece[pos][0], positionPiece[pos][1]))
                    if (piece == 'b'):
                        chess_board_img.blit(blackBishop, (positionPiece[pos][0], positionPiece[pos][1]))
                    if (piece == 'P'):
                        chess_board_img.blit(whitePawn, (positionPiece[pos][0], positionPiece[pos][1]))
                    if (piece == 'p'):
                        chess_board_img.blit(blackPawn, (positionPiece[pos][0], positionPiece[pos][1]))
                    if (piece == 'R'):
                        chess_board_img.blit(whiteRook, (positionPiece[pos][0], positionPiece[pos][1]))
                    if (piece == 'r'):
                        chess_board_img.blit(blackRook, (positionPiece[pos][0], positionPiece[pos][1]))
       
            return chess_board_img

        def get_legal_move(board, pos):
            cur = []
            moves = board.legal_moves
            
            for move in moves:
                print(move, pos)
                if (str(move)[0:2] == pos): cur.append(move)
            return cur
        
        # game loop
        
        chess_board_img = update_board(board)
        screen.fill((202, 228, 241))
        screen.blit(chess_board_img, (30, 50))
        running = True
        yourturn = True
        cnt = 0
        state = 0 # trạng thái bàn cờ
        # 0 - người chơi không làm gì
        # 1 - người chơi đang chọn nước
        while (running):
            if(cnt > 79 and board.is_game_over() == 0):
                print('DRAW GAME!')
                running = False
            
            if(yourturn == False):
                depth = random.randrange(3,5)
                move = chessai.minimax(board=board, depth=depth, alpha=0, beta=500, maximizing_player=True)[0]
                board.push(move)
                cnt +=1
                chess_board_img = update_board(board)
                screen.blit(chess_board_img, (30, 50)) 
                yourturn = True
                pygame.display.update()

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:

                    
                    #if (board.is_game_over()): continue
                        moves = list(board.legal_moves)
                        move = random.choice(moves)
                        board.push(move)
                        cnt += 1
                    
                    #----
                        
                        pos_x = pygame.mouse.get_pos()[0]
                        pos_y = pygame.mouse.get_pos()[1]
                        x = int ((pos_x - 40) / 60) + 1
                        y = 8 - int ((pos_y - 60) / 60) 
                        if (1 <= x <= 8 and 1 <= y <= 8): 
                            pos = chr(x+96) +  str(y)
                            selectedChess = board.piece_at(int(chess.parse_square(pos)))
                            if (str(selectedChess).isupper()): 
                                moves = get_legal_move(board, pos)
                                if (moves != []): print(moves)
                        

                        chess_board_img = update_board(board)
                        screen.blit(chess_board_img, (30, 50))  
                        yourturn = False
                        pygame.display.update()
            pygame.display.update()
    pygame.quit()

    