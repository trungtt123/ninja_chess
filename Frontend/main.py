# run this file

import menuscreen
import playscreen
import pygame
from pygame import draw
pygame.display.set_caption('Ninja Chess')

currentScreen = 'MENU_SCREEN'


while (currentScreen != 'EXIT'):
    
    if (currentScreen == 'MENU_SCREEN'): 
        currentScreen = menuscreen.MenuScreen.run()
    if (currentScreen == 'PLAY_SCREEN'): 
        currentScreen = playscreen.PlayScreen.run()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            currentScreen = 'EXIT'
    pygame.display.update()
pygame.quit()