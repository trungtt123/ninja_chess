import pygame
from pygame import draw
import button

# create display window
class MenuScreen():
    def run():
        SCREEN_HEIGHT = 600
        SCREEN_WIDTH = 1000

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        

        # load button menu
        start_img = pygame.image.load('images/button/play.png').convert_alpha()
        option_img = pygame.image.load('images/button/option.png').convert_alpha()
        exit_img = pygame.image.load('images/button/exit.png').convert_alpha()


        # create button munu
        start_button = button.Button(SCREEN_WIDTH // 2 - start_img.get_width() * 0.1 , SCREEN_HEIGHT // 2 - 190, start_img, 0.2)
        option_button = button.Button(SCREEN_WIDTH // 2 - option_img.get_width() * 0.1, SCREEN_HEIGHT // 2 - 120, option_img, 0.2)
        exit_button = button.Button(SCREEN_WIDTH // 2 - exit_img.get_width() * 0.1 , SCREEN_HEIGHT // 2 - 50, exit_img, 0.2)


        # game loop

        screen.fill((202, 228, 241))

        if start_button.draw(screen):
            return 'PLAY_SCREEN'
        if option_button.draw(screen):
            return 'OPTION_SCREEN'
        if exit_button.draw(screen):
            return 'EXIT'
        return 'MENU_SCREEN'
  