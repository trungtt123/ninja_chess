from os import stat
import pygame
from pygame import draw
import button
import random
import chess
import sys

sys.path.append('../Backend')

import chessai
# create display window


class PlayScreen():
    def run():
        SCREEN_HEIGHT = 600
        SCREEN_WIDTH = 1000
        board = chess.Board()
        #cursor = pygame.cursors.compile(pygame.cursors.sizer_x_strings)
        #cursor, mask = pygame.cursors.compile(pygame.cursors.broken_x_strings)
        #pygame.mouse.set_cursor((24, 16), (7, 11), *cursor)
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
        
        #load piece
        #----------black piece-------------
        blackKing = pygame.image.load('../images/chess/Chess_Pieces_Green/King/King_shadow.png').convert_alpha()
        blackKing = pygame.transform.scale(blackKing, (70, 70))

        blackQueen = pygame.image.load('../images/chess/Chess_Pieces_Green/Queen/Queen_shadow.png').convert_alpha()
        blackQueen = pygame.transform.scale(blackQueen, (70, 70))

        blackBishop = pygame.image.load('../images/chess/Chess_Pieces_Green/Bishop/Bishop_shadow.png').convert_alpha()
        blackBishop = pygame.transform.scale(blackBishop, (70, 70))

        blackKnight = pygame.image.load('../images/chess/Chess_Pieces_Green/Knight/Knight_shadow.png').convert_alpha()
        blackKnight = pygame.transform.scale(blackKnight, (70, 70))
        
        blackRook = pygame.image.load('../images/chess/Chess_Pieces_Green/Rook/Rook_shadow.png').convert_alpha()
        blackRook = pygame.transform.scale(blackRook, (70, 70))
        
        blackPawn = pygame.image.load('../images/chess/Chess_Pieces_Green/Pawn/Pawn_shadow.png').convert_alpha()
        blackPawn = pygame.transform.scale(blackPawn, (70, 70))

        #-----------white piece----------------


        whiteKing = pygame.image.load('../images/chess/Chess_Pieces_Golden/King/King_shadow.png').convert_alpha()
        whiteKing = pygame.transform.scale(whiteKing, (70, 70))

        whiteQueen = pygame.image.load('../images/chess/Chess_Pieces_Golden/Queen/Queen_shadow.png').convert_alpha()
        whiteQueen = pygame.transform.scale(whiteQueen, (70, 70))
        btnQueen = pygame.image.load('../images/chess/Chess_Pieces_Golden/Queen/Queen_shadow.png').convert_alpha()

        whiteBishop = pygame.image.load('../images/chess/Chess_Pieces_Golden/Bishop/Bishop_shadow.png').convert_alpha()
        whiteBishop = pygame.transform.scale(whiteBishop, (70, 70))
        btnBishop = pygame.image.load('../images/chess/Chess_Pieces_Golden/Bishop/Bishop_shadow.png').convert_alpha()
        
        whiteKnight = pygame.image.load('../images/chess/Chess_Pieces_Golden/Knight/Knight_shadow.png').convert_alpha()
        whiteKnight = pygame.transform.scale(whiteKnight, (70, 70))
        btnKnight = pygame.image.load('../images/chess/Chess_Pieces_Golden/Knight/Knight_shadow.png').convert_alpha()

        whiteRook = pygame.image.load('../images/chess/Chess_Pieces_Golden/Rook/Rook_shadow.png').convert_alpha()
        whiteRook = pygame.transform.scale(whiteRook, (70, 70))
        btnRook = pygame.image.load('../images/chess/Chess_Pieces_Golden/Rook/Rook_shadow.png').convert_alpha()

        whitePawn = pygame.image.load('../images/chess/Chess_Pieces_Golden/Pawn/Pawn_shadow.png').convert_alpha()
        whitePawn = pygame.transform.scale(whitePawn, (70, 70))

        #box opacity
        boxOpacityYellowC = pygame.image.load('../images/chess/Chess_board/box_opacity_yellow_c.png').convert_alpha()
        boxOpacityYellowC = pygame.transform.scale(boxOpacityYellowC, (70, 70)) 
        boxOpacityYellow = pygame.image.load('../images/chess/Chess_board/box_opacity_yellow.png').convert_alpha()
        boxOpacityYellow = pygame.transform.scale(boxOpacityYellow, (70, 70)) 
        boxOpacityRed = pygame.image.load('../images/chess/Chess_board/box_opacity_red_c.png').convert_alpha()
        boxOpacityRed = pygame.transform.scale(boxOpacityRed, (70, 70)) 

        boxLevel = pygame.image.load('../images/chess/Chess_board/board-phong-tuong-fix.png').convert_alpha()
        boxLevel = pygame.transform.scale(boxLevel, (250, 250)) 
        
        win =  pygame.image.load('../images/chess/win.png').convert_alpha()
        win = pygame.transform.scale(win, (498, 243)) 
        lose =  pygame.image.load('../images/chess/lose.png').convert_alpha()
        lose = pygame.transform.scale(lose, (498, 243)) 
        #update board
        def update_board(board, moves):
            color = []
            chess_board_img = pygame.image.load('../images/chess/Chess_board/Chessboard.png').convert_alpha()
            chess_board_img = pygame.transform.scale(chess_board_img, (500, 500))
            
            if (moves != []):
                piece = str(board.piece_at(chess.parse_square(str(moves[0])[0:2])))
                chess_board_img.blit(boxOpacityYellow, (positionPiece[str(moves[0])[0:2]][0], positionPiece[str(moves[0])[0:2]][1]))
            
            
            # draw board
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
            for move in moves:
                if str(move)[2:4] not in color: 
                    color.append(str(move)[2:4])
                else: 
                    continue
                piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                if (piece == 'None'):
                    chess_board_img.blit(boxOpacityYellowC, (positionPiece[str(move)[2:4]][0], positionPiece[str(move)[2:4]][1]))
                else: 
                    chess_board_img.blit(boxOpacityRed, (positionPiece[str(move)[2:4]][0], positionPiece[str(move)[2:4]][1]))  
            return chess_board_img

        def get_legal_move(board, pos):
            cur = []
            moves = board.legal_moves
            
            for move in moves:
                #print(move, pos)
                if (str(move)[0:2] == pos): 
                    cur.append(move)
            #print(cur)
            return cur
        def get_win_or_lose(board):
    
            whiteKing = ''
            blackKing = ''
    
            for i in range(97, 105):
                for j in range(1, 9):
                    pos = chr(i) + str(j)
                    piece = str(board.piece_at(chess.parse_square(pos)))

                    if (piece == 'K'):
                        whiteKing = pos
                    if (piece == 'k'):
                        blackKing = pos
            
            print(blackKing, whiteKing)
            print(board.is_attacked_by(chess.WHITE, chess.parse_square(blackKing)))

            if (board.is_attacked_by(chess.WHITE, chess.parse_square(blackKing)) and board.is_game_over()):
                return True
            if (board.is_attacked_by(chess.BLACK, chess.parse_square(whiteKing)) and board.is_game_over()):
                return False
            return False


        # game loop
        

        chess_board_img = update_board(board, [])
        screen.fill((202, 228, 241))
        screen.blit(chess_board_img, (30, 50))
        
        btnQueen = button.Button(20 , 140, btnQueen, 0.12)
        

        btnBishop = button.Button(70 , 140, btnBishop, 0.12)
        

        btnRook = button.Button(120 , 140, btnRook, 0.12)
        

        btnKnight = button.Button(170 , 140, btnKnight, 0.12)
        
        running = True
        turn = 'WHITE'
        state = 0 # - 1 phong tướng, 0 khác th phong tướng
        legal_moves = []
        
        while (running):
            
            if (turn == 'BLACK' and board.is_game_over() == False):
                move = chessai.Solve().get_ai_move(board)
                board.push(move)
                turn = 'WHITE'
                chess_board_img = update_board(board, [])
                screen.blit(chess_board_img, (30, 50))
                continue
            
            for event in pygame.event.get():
                

                if event.type == pygame.QUIT:
                    #running = False
                    pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    pos_x = pygame.mouse.get_pos()[0]
                    pos_y = pygame.mouse.get_pos()[1]


                    if (state == 1):
                        chrTxt = ''
                        if (190 <= pos_x <= 215 and 308 <= pos_y <= 343): chrTxt = 'q'
                        if (234 <= pos_x <= 263 and 308 <= pos_y <= 343): chrTxt = 'r'
                        if (282 <= pos_x <= 312 and 308 <= pos_y <= 343): chrTxt = 'n'
                        if (330 <= pos_x <= 363 and 308 <= pos_y <= 343): chrTxt = 'b'
                        print(chrTxt)
                        print(legal_moves)
                        for move in legal_moves:
                            if (len(str(move)) == 5 and str(move)[4] == chrTxt): 
                                board.push(move)
                                turn = 'BLACK'
                                legal_moves = []
                                state = 0
                                break

                    x = int ((pos_x - 40) / 60) + 1
                    y = 8 - int ((pos_y - 60) / 60) 
                    if (1 <= x <= 8 and 1 <= y <= 8): 
                        pos = chr(x+96) +  str(y)
                        selectedChess = board.piece_at(int(chess.parse_square(pos)))
                        if (turn == 'WHITE'):
                            for move in legal_moves:
                                if (len(str(move)) == 4):
                                    if (str(move)[2:4] == pos): 
                                        turn = 'BLACK'
                                        board.push(move)
                                        chess_board_img = update_board(board, [])
                                        legal_moves = []
                                        break
                                if (len(str(move)) == 5):
                                    if (str(move)[2:4] == pos):
                                        screen.blit(boxLevel, (150, 150)) 
                                        state = 1
                                        break
                        if (str(selectedChess).isupper() and turn == 'WHITE'): 
                            legal_moves = get_legal_move(board, pos)
                            
                            chess_board_img = update_board(board, legal_moves)
                        else: chess_board_img = update_board(board, [])
                    if (state == 0): screen.blit(chess_board_img, (30, 50))
                    if (board.is_game_over()): 
                        #print(get_win_or_lose(board))
                        if (get_win_or_lose(board)): 
                            screen.blit(win, (40, 150))
                            running = False
                        else: 
                            screen.blit(lose, (40, 150))
                            running = False
                        break    
            pygame.display.update()
            if (running == False): 
                pygame.time.delay(2000)
                return 'PLAY_SCREEN'
    pygame.quit()