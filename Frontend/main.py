# run this file

import menuscreen
import playscreen
import optionscreen
import pygame
from pygame import draw
pygame.display.set_caption('Ninja Chess')

currentScreen = 'MENU_SCREEN'

pygame.mixer.init()
soundObj = pygame.mixer.Sound('../audio/music_1.mp3');
soundObj.play(loops=-1)
soundObj.set_volume(0.1)

while (currentScreen != 'EXIT'):
    if (currentScreen == 'MENU_SCREEN'): 
        currentScreen = menuscreen.MenuScreen.run()
    if (currentScreen == 'PLAY_SCREEN'): 
        currentScreen = playscreen.PlayScreen.run()
    if (currentScreen == 'OPTION_SCREEN'): 
        currentScreen = optionscreen.OptionScreen.run()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            currentScreen = 'EXIT'
            soundObj.stop()
    pygame.display.update()
pygame.quit()