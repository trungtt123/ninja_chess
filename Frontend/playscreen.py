from os import stat
import pygame
from pygame import draw
from pygame.display import update
import button
import random
import chess
import sys
from threading import Thread
import threading
import time
import json
import datetime
import concurrent.futures

sys.path.append('../Backend')
import chessai #import backend

# create display window

class PlayScreen():

    def run():   
        f = open('option.json', mode="r")
        
        data = json.load(f)
        f.close()
        #pygame.init()
        board_fen = data['CurrentBoard']
        if (board_fen == None): board_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        board = chess.Board(board_fen)
        #print(board.fen())
        SCREEN_HEIGHT = 600
        SCREEN_WIDTH = 1000
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


        #audio 
        pygame.mixer.init()
        moveSound = pygame.mixer.Sound('../audio/move.mp3')
        winSound = pygame.mixer.Sound('../audio/win.wav')
        loseSound = pygame.mixer.Sound('../audio/lose.wav')
        goodSound = pygame.mixer.Sound('../audio/good.mp3')
        badSound = pygame.mixer.Sound('../audio/bad.mp3')
        winSound.set_volume(0.6)
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
            'a2': (5, 365), 'b2': (65, 365), 'c2': (125, 365), 'd2': (185, 365), 'e2': (245, 365), 'f2': (305, 365), 'g2': (365, 365), 'h2': (425, 365),
            'a1': (5, 425), 'b1': (65, 425), 'c1': (125, 425), 'd1': (185, 425), 'e1': (245, 425), 'f1': (305, 425), 'g1': (365, 425), 'h1': (425, 425),
        }
        positionPiece_2 = {
            'h1': (5, 5), 'g1': (65, 5), 'f1': (125, 5), 'e1': (185, 5), 'd1': (245, 5), 'c1': (305, 5), 'b1': (365, 5), 'a1': (425, 5),
            'h2': (5, 65), 'g2': (65, 65), 'f2': (125, 65), 'e2': (185, 65), 'd2': (245, 65), 'c2': (305, 65), 'b2': (365, 65), 'a2': (425, 65),
            'h3': (5, 125), 'g3': (65, 125), 'f3': (125, 125), 'e3': (185, 125), 'd3': (245, 125), 'c3': (305, 125), 'b3': (365, 125), 'a3': (425, 125),
            'h4': (5, 185), 'g4': (65, 185), 'f4': (125, 185), 'e4': (185, 185), 'd4': (245, 185), 'c4': (305, 185), 'b4': (365, 185), 'a4': (425, 185),
            'h5': (5, 245), 'g5': (65, 245), 'f5': (125, 245), 'e5': (185, 245), 'd5': (245, 245), 'c5': (305, 245), 'b5': (365, 245), 'a5': (425, 245),
            'h6': (5, 305), 'g6': (65, 305), 'f6': (125, 305), 'e6': (185, 305), 'd6': (245, 305), 'c6': (305, 305), 'b6': (365, 305), 'a6': (425, 305),
            'h7': (5, 365), 'g7': (65, 365), 'f7': (125, 365), 'e7': (185, 365), 'd7': (245, 365), 'c7': (305, 365), 'b7': (365, 365), 'a7': (425, 365),
            'h8': (5, 425), 'g8': (65, 425), 'f8': (125, 425), 'e8': (185, 425), 'd8': (245, 425), 'c8': (305, 425), 'b8': (365, 425), 'a8': (425, 425),
        }

        
        
        #load piece
        #----------black piece-------------
        blackKing = pygame.image.load('../images/chess/Chess_Pieces_Green/King/King_shadow.png').convert_alpha()
        blackKing = pygame.transform.scale(blackKing, (70, 70))
        #blackKingSmall = pygame.transform.scale(blackKing, (35, 35))

        blackQueen = pygame.image.load('../images/chess/Chess_Pieces_Green/Queen/Queen_shadow.png').convert_alpha()
        blackQueen = pygame.transform.scale(blackQueen, (70, 70))
        blackQueenSmall = pygame.transform.scale(blackQueen, (35, 35))

        blackBishop = pygame.image.load('../images/chess/Chess_Pieces_Green/Bishop/Bishop_shadow.png').convert_alpha()
        blackBishop = pygame.transform.scale(blackBishop, (70, 70))
        blackBishopSmall = pygame.transform.scale(blackBishop, (35, 35))

        blackKnight = pygame.image.load('../images/chess/Chess_Pieces_Green/Knight/Knight_shadow.png').convert_alpha()
        blackKnight = pygame.transform.scale(blackKnight, (70, 70))
        blackKnightSmall = pygame.transform.scale(blackKnight, (35, 35))
        
        blackRook = pygame.image.load('../images/chess/Chess_Pieces_Green/Rook/Rook_shadow.png').convert_alpha()
        blackRook = pygame.transform.scale(blackRook, (70, 70))
        blackRookSmall = pygame.transform.scale(blackRook, (35, 35))
        
        blackPawn = pygame.image.load('../images/chess/Chess_Pieces_Green/Pawn/Pawn_shadow.png').convert_alpha()
        blackPawn = pygame.transform.scale(blackPawn, (70, 70))
        blackPawnSmall = pygame.transform.scale(blackPawn, (35, 35))

        #-----------white piece----------------


        whiteKing = pygame.image.load('../images/chess/Chess_Pieces_Golden/King/King_shadow.png').convert_alpha()
        whiteKing = pygame.transform.scale(whiteKing, (70, 70))
        whiteKingSmall =  pygame.transform.scale(whiteKing, (35, 35))

        whiteQueen = pygame.image.load('../images/chess/Chess_Pieces_Golden/Queen/Queen_shadow.png').convert_alpha()
        whiteQueen = pygame.transform.scale(whiteQueen, (70, 70))
        whiteQueenSmall =  pygame.transform.scale(whiteQueen, (35, 35))
        btnQueen = pygame.image.load('../images/chess/Chess_Pieces_Golden/Queen/Queen_shadow.png').convert_alpha()

        whiteBishop = pygame.image.load('../images/chess/Chess_Pieces_Golden/Bishop/Bishop_shadow.png').convert_alpha()
        whiteBishop = pygame.transform.scale(whiteBishop, (70, 70))
        whiteBishopSmall = pygame.transform.scale(whiteBishop, (35, 35))
        btnBishop = pygame.image.load('../images/chess/Chess_Pieces_Golden/Bishop/Bishop_shadow.png').convert_alpha()
        
        whiteKnight = pygame.image.load('../images/chess/Chess_Pieces_Golden/Knight/Knight_shadow.png').convert_alpha()
        whiteKnight = pygame.transform.scale(whiteKnight, (70, 70))
        whiteKnightSmall = pygame.transform.scale(whiteKnight, (35, 35))
        btnKnight = pygame.image.load('../images/chess/Chess_Pieces_Golden/Knight/Knight_shadow.png').convert_alpha()

        whiteRook = pygame.image.load('../images/chess/Chess_Pieces_Golden/Rook/Rook_shadow.png').convert_alpha()
        whiteRook = pygame.transform.scale(whiteRook, (70, 70))
        whiteRookSmall = pygame.transform.scale(whiteRook, (35, 35))
        
        btnRook = pygame.image.load('../images/chess/Chess_Pieces_Golden/Rook/Rook_shadow.png').convert_alpha()

        whitePawn = pygame.image.load('../images/chess/Chess_Pieces_Golden/Pawn/Pawn_shadow.png').convert_alpha()
        whitePawn = pygame.transform.scale(whitePawn, (70, 70))
        whitePawnSmall = pygame.transform.scale(whitePawn, (35, 35))

        #box opacity
        boxOpacityYellowC = pygame.image.load('../images/chess/Chess_board/box_opacity_yellow_c.png').convert_alpha()
        boxOpacityYellowC = pygame.transform.scale(boxOpacityYellowC, (70, 70)) 
        boxOpacityYellow = pygame.image.load('../images/chess/Chess_board/box_opacity_yellow.png').convert_alpha()
        boxOpacityYellow = pygame.transform.scale(boxOpacityYellow, (70, 70)) 
        boxOpacityRed = pygame.image.load('../images/chess/Chess_board/box_opacity_red_c.png').convert_alpha()
        boxOpacityRed = pygame.transform.scale(boxOpacityRed, (70, 70)) 

        boxLevelWhite = pygame.image.load('../images/chess/Chess_board/board-phong-tuong-white.png').convert_alpha()
        boxLevelWhite = pygame.transform.scale(boxLevelWhite, (250, 250)) 

        boxLevelBlack = pygame.image.load('../images/chess/Chess_board/board-phong-tuong-black.png').convert_alpha()
        boxLevelBlack = pygame.transform.scale(boxLevelBlack, (250, 250)) 
        
        btnUndo = pygame.image.load('../images/button/undo_move.png').convert_alpha()
        btnUndo = pygame.transform.scale(btnUndo, (80, 80)) 

        btnBack_img = pygame.image.load('../images/button/arrow_back.png').convert_alpha()
        btnBack_img = pygame.transform.scale(btnBack_img, (35, 25))

        btnWhite = pygame.image.load('../images/button/9_yellow.png').convert_alpha()
        btnWhite =  pygame.transform.scale(btnWhite, (100, 100)) 
        btnBlack = pygame.image.load('../images/button/9_green.png').convert_alpha()
        btnBlack =  pygame.transform.scale(btnBlack, (100, 100)) 
        btnBack = button.Button(-1, 5, btnBack_img, 1)

        btnUndoDisable = pygame.image.load('../images/button/undo_move_disable.png').convert_alpha()
        btnUndoDisable = pygame.transform.scale(btnUndoDisable, (50, 50)) 
        
        boxContain = pygame.image.load('../images/chess/Chess_board/contain.png').convert_alpha()
        boxContain = pygame.transform.scale(boxContain, (400, 400)) 

        boxConfirm = pygame.image.load('../images/chess/Chess_board/confirm.png').convert_alpha()
        boxConfirm = pygame.transform.scale(boxConfirm, (300, 200)) 
        myClock = pygame.image.load('../images/chess/clock.png').convert_alpha()
        myClock = pygame.transform.scale(myClock, (120, 35)) 


        win =  pygame.image.load('../images/chess/win.png').convert_alpha()
        win = pygame.transform.scale(win, (498, 243)) 
        lose =  pygame.image.load('../images/chess/lose.png').convert_alpha()
        lose = pygame.transform.scale(lose, (498, 243)) 
        draw =  pygame.image.load('../images/chess/draw.png').convert_alpha()
        draw = pygame.transform.scale(draw, (450, 180)) 

        #update board
        def update_box_contain(loot_piece, firstTurn):
            boxContain = pygame.image.load('../images/chess/Chess_board/contain.png').convert_alpha()
            boxContain = pygame.transform.scale(boxContain, (400, 400)) 
            #boxContain.blit(whiteKing, (20, 20))
            spaceX = 8
            spaceY1 = 160
            spaceY2 = 230
            if firstTurn == 'BLACK': 
                spaceY1 = 230
                spaceY2 = 160
            for piece in loot_piece[0]:
                spaceX += 22
                if (piece == 'Q'): boxContain.blit(whiteQueenSmall, (spaceX, spaceY1))  
                if (piece == 'R'): boxContain.blit(whiteRookSmall, (spaceX, spaceY1))
                if (piece == 'P'): boxContain.blit(whitePawnSmall, (spaceX, spaceY1))
                if (piece == 'N'): boxContain.blit(whiteKnightSmall, (spaceX, spaceY1))
                if (piece == 'B'): boxContain.blit(whiteBishopSmall, (spaceX, spaceY1))
            spaceX = 8
            for piece in loot_piece[1]:
                spaceX += 22
                if (piece == 'q'): boxContain.blit(blackQueenSmall, (spaceX, spaceY2))  
                if (piece == 'r'): boxContain.blit(blackRookSmall, (spaceX, spaceY2))
                if (piece == 'p'): boxContain.blit(blackPawnSmall, (spaceX, spaceY2))
                if (piece == 'n'): boxContain.blit(blackKnightSmall, (spaceX, spaceY2))
                if (piece == 'b'): boxContain.blit(blackBishopSmall, (spaceX, spaceY2))
            return boxContain
        def update_board_white(board, moves):
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

        
        def update_board_black(board, moves):
            #print(board)
            color = []
            chess_board_img = pygame.image.load('../images/chess/Chess_board/Chessboard.png').convert_alpha()

            chess_board_img = pygame.transform.scale(chess_board_img, (500, 500))
            
            if (moves != []):
                piece = str(board.piece_at(chess.parse_square(str(moves[0])[0:2])))
                chess_board_img.blit(boxOpacityYellow, (positionPiece_2[str(moves[0])[0:2]][0], positionPiece_2[str(moves[0])[0:2]][1]))
            
        
            # draw board
            for i in range(97, 105):
                for j in range(1, 9):
                    pos = chr(i) + str(j)
                    piece = str(board.piece_at(chess.parse_square(pos)))
                    #pos = chr(201 - i) + str(9 - j)
                    if (piece == 'K'):
                        chess_board_img.blit(whiteKing, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
                    if (piece == 'k'):
                        chess_board_img.blit(blackKing, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
                    if (piece == 'Q'):
                        chess_board_img.blit(whiteQueen, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
                    if (piece == 'q'):
                        chess_board_img.blit(blackQueen, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
                    if (piece == 'N'):
                        chess_board_img.blit(whiteKnight, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
                    if (piece == 'n'):
                        chess_board_img.blit(blackKnight, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
                    if (piece == 'B'):
                        chess_board_img.blit(whiteBishop, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
                    if (piece == 'b'):
                        chess_board_img.blit(blackBishop, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
                    if (piece == 'P'):
                        chess_board_img.blit(whitePawn, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
                    if (piece == 'p'):
                        chess_board_img.blit(blackPawn, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
                    if (piece == 'R'):
                        chess_board_img.blit(whiteRook, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
                    if (piece == 'r'):
                        chess_board_img.blit(blackRook, (positionPiece_2[pos][0], positionPiece_2[pos][1]))
            for move in moves:
                if str(move)[2:4] not in color: 
                    color.append(str(move)[2:4])
                else: 
                    continue
                piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                if (piece == 'None'):
                    chess_board_img.blit(boxOpacityYellowC, (positionPiece_2[str(move)[2:4]][0], positionPiece_2[str(move)[2:4]][1]))
                else: 
                    chess_board_img.blit(boxOpacityRed, (positionPiece_2[str(move)[2:4]][0], positionPiece_2[str(move)[2:4]][1]))
              
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

        def get_win_or_lose(board, firstTurn):
    
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
            w_win = board.is_attacked_by(chess.WHITE, chess.parse_square(blackKing))
            b_win = board.is_attacked_by(chess.BLACK, chess.parse_square(whiteKing))
            if (w_win == True and firstTurn == 'WHITE'): return 1 
            if (w_win == True and firstTurn == 'BLACK'): return 2
            if (b_win == True and firstTurn == 'WHITE'): return 2 # black win
            if (b_win == True and firstTurn == 'BLACK'): return 1
            return 0 # draw

        # game loop
        btnWhite = button.Button(410, 190, btnWhite, 0.8)

        btnBlack = button.Button(530, 190, btnBlack, 0.8)
        firstTurn = data['FirstTurn']
        turn = data['Turn']
        loot_piece = data['LootPiece']
        level = data['Level']
        if turn == None: turn = 'WHITE'
        
        def update_data(currentBoard, firstTurn, turn, lootPiece, clock_1, clock_2):
            f = open('option.json', mode="w+")
            try:
                data['CurrentBoard'] = currentBoard.fen()
                data['FirstTurn'] = firstTurn
                data['Turn'] = turn
                data['LootPiece'] = lootPiece
                data['Clock_1'] = clock_1
                data['Clock_2'] = clock_2
            except:
                data['CurrentBoard'] = None
                data['FirstTurn'] = None
                data['Turn'] = None
                data['LootPiece'] = [[], []]
                data['Clock_1'] = None
                data['Clock_2'] = None
            json.dump(data, f)

            f.close()

        while (firstTurn == None):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    update_data(board, firstTurn, turn, loot_piece, None, None)
                    return 'EXIT'
                    pygame.quit()
                screen.fill((202, 228, 241))
                
                screen.blit(boxConfirm, (360, 100))
                # if (btnBack.draw(screen)):
                #     return 'MENU_SCREEN'
                if (btnWhite.draw(screen)):
                    firstTurn = 'WHITE'
                if (btnBlack.draw(screen)):
                    firstTurn = 'BLACK'

            pygame.display.update()

        
        
        screen.fill((202, 228, 241))
        
        #screen.blit(boxContain, (580, 150))
        
        #button in screen
        btnQueen = button.Button(20 , 140, btnQueen, 0.12)
        

        btnBishop = button.Button(70 , 140, btnBishop, 0.12)
        

        btnRook = button.Button(120 , 140, btnRook, 0.12)
        

        btnKnight = button.Button(170 , 140, btnKnight, 0.12)
        
        btnUndo = button.Button(900, 490, btnUndo, 0.8)

        
        
        btnUndo.draw(screen)

        
       
        running = True

        font = pygame.font.Font('freesansbold.ttf', 15)
        
        
        def get_time_after_1s(seconds):
            seconds -= 1
            hours = int (seconds / 3600)
            minutes = int ((seconds - hours * 3600) / 60)
            secs = seconds - hours * 3600 - minutes * 60 
            
            if (0 <= secs <= 9): secs = '0' + str(secs) 
            if (0 <= minutes <= 9): minutes = '0' + str(minutes)
            if (0 <= hours <= 9): hours = '0' + str(hours)
            return str(hours) + ":" + str(minutes) + ":" + str(secs)
        
        def solve_clock(m1, m2):   

            while (running == True):
                clock1 = font.render(get_time_after_1s(m1), True, 'black')
                clock2 = font.render(get_time_after_1s(m2), True, 'black')
                #print(turn)
                if (turn == firstTurn): m1 -= 1
                else: m2 -= 1 
                 
                
                pygame.draw.rect(screen,(202, 228, 241),(610, 0, 610, 170))
             
                screen.blit(myClock, (620, 110))

                screen.blit(clock1, (670, 124))

                screen.blit(myClock, (820, 110))

                screen.blit(clock2, (870, 124))
                
                pygame.display.update()
                
                #print(m1, m2)
                if (m1 * m2 == 0):
                    return (m1, m2) 
                time.sleep(1)               
            return (m1, m2)
        def get_move_ai(board, level, firstTurn):
            if (running == True):
                return chessai.Solve().get_ai_move(board, level, firstTurn)
        t1 = None
        if (data['Time']): 
            if (data['Clock_1'] == None or data['Clock_2'] == None):
                t1 = concurrent.futures.ThreadPoolExecutor().submit(solve_clock, data['LimitTime'] + 1, data['LimitTime'] + 1)
            else: t1 = concurrent.futures.ThreadPoolExecutor().submit(solve_clock, data['Clock_1'], data['Clock_2']) 
       
        state = 0 # - 1 phong tướng, 0 khác th phong tướng
        legal_moves = []
        
        
        #print(ai_running.result())
        
        if (firstTurn == 'BLACK'): 
            ai_running = None 
            #print(turn)
            if (turn == 'WHITE'):  
                ai_running = concurrent.futures.ThreadPoolExecutor().submit(get_move_ai, board, level, firstTurn)
            chess_board_img = update_board_black(board, [])
            screen.blit(chess_board_img, (30, 50))
            boxContain = update_box_contain(loot_piece, firstTurn)
            screen.blit(boxContain, (580, 150))
            pygame.display.update()
            while (running):
                pygame.draw.rect(screen,(202, 228, 241),(0, 0, 50, 50))
                if (btnBack.draw(screen)):
                    running = False
                    if (t1 != None):
                        update_data(board, firstTurn, turn, loot_piece, t1.result()[0], t1.result()[1])
                    else:
                        update_data(board, firstTurn, turn, loot_piece, None, None)

                    return 'MENU_SCREEN'
                pygame.display.update()
                if (ai_running != None):
                    if (ai_running.running() == True): 
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                                return 'EXIT'
                                pygame.quit()
                        continue
                if (data['Time'] and t1.running() == False):
                    if (t1.result()[1] == 0):
                        screen.blit(win, (40, 150))
                        winSound.play()
                        
                    if (t1.result()[0] == 0):
                        screen.blit(lose, (40, 150))
                        loseSound.play()
                    running = False
                    pygame.display.update()
                    update_data(None, None, None, [[], []], None, None)
                    pygame.time.delay(5000)
                    return 'PLAY_SCREEN'
                    
                
                if (turn == 'WHITE' and board.is_game_over() == False):
                    #time.sleep(1)
                    #print('run here')
                    
                    
                    if (ai_running != None and ai_running.running() == False):
                        move = ai_running.result()
                    else: continue  
                    
                    
                
                    piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                    if (piece != 'None'): 
                        if (piece.isupper()): loot_piece[0].append(piece)
                        else: loot_piece[1].append(piece)
                    board.push(move)
                    moveSound.play()
                    #if (board.is_checkmate()): badSound.play()
                    turn = 'BLACK'

                    #screen.fill((202, 228, 241))
                    pygame.draw.rect(screen,(202, 228, 241),(25,25,590,800))
                    pygame.draw.rect(screen,(202, 228, 241),(610, 150, 1000, 800))
                    chess_board_img = update_board_black(board, [])
                    
                    
                    if (btnUndo.draw(screen)): 
                        try:
                            move = board.pop()
                            piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                            if (piece != 'None' and piece.isupper()): loot_piece[0].pop()
                            
                            move = board.pop()
                            piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                            if (piece != 'None' and piece.isupper() == False): loot_piece[1].pop()
                            
                            chess_board_img = update_board_black(board, [])
                        except: print('do not have front move 123')
                        print(loot_piece)
                    boxContain = update_box_contain(loot_piece, firstTurn)
                    screen.blit(boxContain, (580, 150))
                    screen.blit(chess_board_img, (30, 50))
                    continue
                
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        running = False
                        update_data(board, firstTurn, turn, loot_piece, t1.result()[0], t1.result()[1])
                        pygame.quit()
                        return 'EXIT'
                    
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
                                    
                                    piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                                    if (piece != 'None'): 
                                        if (piece.isupper()): loot_piece[0].append(piece)
                                        else: loot_piece[1].append(piece)
                                    board.push(move)
                                    moveSound.play()
                                    #if (board.is_checkmate()): goodSound.play()
                                    turn = 'WHITE'
                                    legal_moves = []
                                    state = 0
                                    ai_running = concurrent.futures.ThreadPoolExecutor().submit(get_move_ai, board, level, firstTurn)
                                    break

                        x = 8 - int ((pos_x - 40) / 60) 
                        y = int ((pos_y - 60) / 60) + 1
                        
                        if (1 <= x <= 8 and 1 <= y <= 8): 
                            pos = chr(x+96) +  str(y)
                            

                            selectedChess = board.piece_at(int(chess.parse_square(pos)))
                            if (turn == 'BLACK'):
                                print(legal_moves)
                                for move in legal_moves:
                                    if (len(str(move)) == 4):
                                        if (str(move)[2:4] == pos): 
                                            turn = 'WHITE'
                                            piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                                            print(piece)
                                            if (piece != 'None'): 
                                                if (piece.isupper()): loot_piece[0].append(piece)
                                                else: loot_piece[1].append(piece)
                                            board.push(move)
                                            moveSound.play()
                                            #if (board.is_checkmate()): goodSound.play()
                                            chess_board_img = update_board_black(board, [])
                                            legal_moves = []
                                            ai_running = concurrent.futures.ThreadPoolExecutor().submit(get_move_ai, board, level, firstTurn)
                                            break
                                    if (len(str(move)) == 5):
                                        if (str(move)[2:4] == pos):
                                            screen.blit(boxLevelBlack, (150, 150)) 
                                            state = 1
                                            break
                            if (str(selectedChess).isupper() == False and turn == 'BLACK' and state == 0): 
                                legal_moves = get_legal_move(board, pos)
                                
                                chess_board_img = update_board_black(board, legal_moves)
                            else: chess_board_img = update_board_black(board, [])
                        #screen.blit(boxContain, (580, 150))
                        
                        if (state == 0): 
                            
                            #screen.fill((202, 228, 241))
                            pygame.draw.rect(screen,(202, 228, 241),(25,25,590,700))
                            pygame.draw.rect(screen,(202, 228, 241),(610, 150, 1000, 800))
                            if (btnUndo.draw(screen)): 
                                try:
                                    move = board.pop()
                                
                                    piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                                    if (piece != 'None' and piece.isupper()): loot_piece[0].pop()
                                    try:
                                        move = board.pop()
                                        piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                                        if (piece != 'None' and piece.isupper() == False): loot_piece[1].pop()
                                    except: board.push(move)
                                    chess_board_img = update_board_black(board, [])
                                except: print('do not have front move')
                                print(loot_piece)
                            boxContain = update_box_contain(loot_piece, firstTurn)
                            screen.blit(boxContain, (580, 150))
                            screen.blit(chess_board_img, (30, 50))

                        
                        
                        if (board.is_game_over()): 
                            moves = list(board.legal_moves)

                            if (moves == [] and get_win_or_lose(board, firstTurn) == 0):
                                screen.blit(draw, (60, 180))
                                winSound.play()
                                running = False
                                break

                            if (get_win_or_lose(board, firstTurn) == 1): 
                                screen.blit(win, (40, 150))
                                winSound.play()
                                
                            if (get_win_or_lose(board, firstTurn) == 2): 
                                screen.blit(lose, (40, 150))
                                loseSound.play()
                            running = False
                            break   
                
                      
                pygame.display.update()
                if (running == False): 
                    update_data(None, None, None, [[], []], None, None)
                    pygame.time.delay(5000)
                    return 'PLAY_SCREEN'
        else: 
            #ai_running = concurrent.futures.ThreadPoolExecutor().submit(get_move_ai, board, level)
            ai_running = None
            print(turn)
            if (turn == 'BLACK'): 
                ai_running = concurrent.futures.ThreadPoolExecutor().submit(get_move_ai, board, level, firstTurn)
            chess_board_img = update_board_white(board, [])
            screen.blit(chess_board_img, (30, 50))
            boxContain = update_box_contain(loot_piece, firstTurn)
            screen.blit(boxContain, (580, 150))
            pygame.display.update()
            while (running):
                pygame.draw.rect(screen,(202, 228, 241),(0, 0, 50, 50))
                if (btnBack.draw(screen)):
                    running = False
                    if (t1 != None):
                        update_data(board, firstTurn, turn, loot_piece, t1.result()[0], t1.result()[1])
                    else:
                        update_data(board, firstTurn, turn, loot_piece, None, None)
                    return 'MENU_SCREEN'
                pygame.display.update()
                if (ai_running != None):
                    if (ai_running.running() == True): 
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                print('hello')
                                running = False
                                pygame.quit()
                                return 'EXIT'
                        continue
                if (data['Time'] and t1.running() == False):
                    if (t1.result()[1] == 0):
                        screen.blit(win, (40, 150))
                        winSound.play()
                        
                    if (t1.result()[0] == 0):
                        screen.blit(lose, (40, 150))
                        loseSound.play()
                    running = False
                    pygame.display.update()
                    update_data(None, None, None, [[], []], None, None)
                    pygame.time.delay(5000)
                    return 'PLAY_SCREEN'
                pygame.draw.rect(screen,(202, 228, 241),(0, 0, 50, 50))
                
                if (btnBack.draw(screen)):
                    print('running')
                    running = False
                    if (t1 != None):
                        update_data(board, firstTurn, turn, loot_piece, t1.result()[0], t1.result()[1])
                    else:
                        update_data(board, firstTurn, turn, loot_piece, None, None)
                    return 'MENU_SCREEN'
                pygame.display.update()
                if (turn == 'BLACK' and board.is_game_over() == False):
                    
                    # ----------CALL AI-----------
                    if (ai_running != None and ai_running.running() == False):
                        move = ai_running.result()
                    else: continue

                    piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                    if (piece != 'None'): 
                        if (piece.isupper()): loot_piece[0].append(piece)
                        else: loot_piece[1].append(piece)
                    board.push(move)
                    moveSound.play()
                    #if (board.is_checkmate()): badSound.play()
                    turn = 'WHITE'

                    #screen.fill((202, 228, 241))
                    pygame.draw.rect(screen,(202, 228, 241),(25,25,590,800))
                    #print(pos_x, pos_y)
                    pygame.draw.rect(screen,(202, 228, 241),(610, 150, 1000, 800))

                    
                    chess_board_img = update_board_white(board, [])
                    
                    
                    if (btnUndo.draw(screen)): 
                        try:
                            move = board.pop()
                            piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                            if (piece != 'None' and piece.isupper()): loot_piece[0].pop()
                            
                            move = board.pop()
                            piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                            if (piece != 'None' and piece.isupper() == False): loot_piece[1].pop()
                            
                            chess_board_img = update_board_white(board, [])
                        except: print('do not have front move')
                        print(loot_piece)
                    boxContain = update_box_contain(loot_piece, firstTurn)
                    screen.blit(boxContain, (580, 150))
                    screen.blit(chess_board_img, (30, 50))
                    continue
                
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        running = False
                        update_data(board, firstTurn, turn, loot_piece, t1.result()[0], t1.result()[1])
                        pygame.quit()
                        return 'EXIT'
                    
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
                                    
                                    piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                                    if (piece != 'None'): 
                                        if (piece.isupper()): loot_piece[0].append(piece)
                                        else: loot_piece[1].append(piece)
                                    board.push(move)
                                    moveSound.play()
                                    #if (board.is_checkmate()): goodSound.play()
                                    turn = 'BLACK'
                                    ai_running = concurrent.futures.ThreadPoolExecutor().submit(get_move_ai, board, level, firstTurn)
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
                                            
                                            piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                                            print(piece)
                                            if (piece != 'None'): 
                                                if (piece.isupper()): loot_piece[0].append(piece)
                                                else: loot_piece[1].append(piece)
                                            board.push(move)
                                            ai_running = concurrent.futures.ThreadPoolExecutor().submit(get_move_ai, board, level, firstTurn)
                                            moveSound.play()
                                            #if (board.is_checkmate()): goodSound.play()
                                            chess_board_img = update_board_white(board, [])
                                            legal_moves = []
                                            break
                                    if (len(str(move)) == 5):
                                        if (str(move)[2:4] == pos):
                                            screen.blit(boxLevelWhite, (150, 150)) 
                                            state = 1
                                            break
                            if (str(selectedChess).isupper() and turn == 'WHITE' and state == 0): 
                                legal_moves = get_legal_move(board, pos)
                                
                                chess_board_img = update_board_white(board, legal_moves)
                            else: chess_board_img = update_board_white(board, [])
                        #screen.blit(boxContain, (580, 150))
                        
                        if (state == 0): 
                            
                            #screen.fill((202, 228, 241))
                            print('run')
                            pygame.draw.rect(screen,(202, 228, 241),(25, 25,590,800))
                            pygame.draw.rect(screen,(202, 228, 241),(610, 150, 1000, 800))
                            if (btnUndo.draw(screen)): 
                                try:
                                    move = board.pop()
                                    piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                                    if (piece != 'None' and piece.isupper()): loot_piece[0].pop()
                                    
                                    move = board.pop()
                                    piece = str(board.piece_at(chess.parse_square(str(move)[2:4])))
                                    if (piece != 'None' and piece.isupper() == False): loot_piece[1].pop()
                                    
                                    chess_board_img = update_board_white(board, [])
                                except: print('do not have front move')
                                print(loot_piece)
                            boxContain = update_box_contain(loot_piece, firstTurn)
                            screen.blit(boxContain, (580, 150))
                            screen.blit(chess_board_img, (30, 50))
                        
                        
                        if (board.is_game_over()): 
                            moves = list(board.legal_moves)

                            if (moves == [] and get_win_or_lose(board, firstTurn) == 0):
                                screen.blit(draw, (60, 180))
                                winSound.play()
                                running = False
                                break

                            if (get_win_or_lose(board, firstTurn) == 1): 
                                screen.blit(win, (40, 150))
                                winSound.play()
                                
                            if (get_win_or_lose(board, firstTurn) == 2): 
                                screen.blit(lose, (40, 150))
                                loseSound.play()
                            running = False
                            break   

                        
                        
                pygame.display.update()
                if (running == False): 
                    update_data(None, None, None, [[], []], None, None)
                    pygame.time.delay(5000)
                    return 'PLAY_SCREEN'
       

    pygame.quit()