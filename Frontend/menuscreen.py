import pygame
from pygame import draw
import button
import json
# create display window
class MenuScreen():
    def run():
        SCREEN_HEIGHT = 600
        SCREEN_WIDTH = 1000

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        

        # load button menu
        start_img = pygame.image.load('../images/button/play.png').convert_alpha()
        option_img = pygame.image.load('../images/button/option.png').convert_alpha()
        exit_img = pygame.image.load('../images/button/exit.png').convert_alpha()
        menu_button = pygame.image.load('../images/button/menu_button.png').convert_alpha()

        # create button munu
        start_button = button.Button(SCREEN_WIDTH // 2 - start_img.get_width() * 0.1 , SCREEN_HEIGHT // 2 - 190, start_img, 0.2)
        option_button = button.Button(SCREEN_WIDTH // 2 - option_img.get_width() * 0.1, SCREEN_HEIGHT // 2 - 120, option_img, 0.2)
        exit_button = button.Button(SCREEN_WIDTH // 2 - exit_img.get_width() * 0.1 , SCREEN_HEIGHT // 2 - 50, exit_img, 0.2)

        menu_button = button.Button(SCREEN_WIDTH // 2 - menu_button.get_width() * 0.1 , SCREEN_HEIGHT // 2 - 190, menu_button, 0.2)

        # game loop

        screen.fill((202, 228, 241))

        if menu_button.draw(screen):
            point = pygame.mouse.get_pos()
            #print(point)
            if (427 <= point[0] <= 573 and 114 <= point[1] <= 169): 
                
                f = open('option.json', mode="r")
                data = json.load(f)
                f.close()
                f = open('option.json', mode="w+")
                data['CurrentBoard'] = None
                data['FirstTurn'] = None
                data['Turn'] = None
                data['LootPiece'] = [[], []]
                data['Clock_1'] = None
                data['Clock_2'] = None
                json.dump(data, f)

                f.close()
                return 'PLAY_SCREEN'
            if (427 <= point[0] <= 573 and 181 <= point[1] <= 235): return 'PLAY_SCREEN'
            if (427 <= point[0] <= 573 and 250 <= point[1] <= 300): return 'OPTION_SCREEN'
            if (427 <= point[0] <= 573 and 313 <= point[1] <= 370): return 'EXIT'
        return 'MENU_SCREEN'
  