from typing_extensions import runtime
import pygame
from pygame import draw
from pygame.display import update
import button
import json
import dropdown
# create display window
class OptionScreen():
    def run():
        f = open('option.json', mode="r")
        data = json.load(f)
        
        pygame.init()
        SCREEN_HEIGHT = 600
        SCREEN_WIDTH = 1000

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        

        # load button menu
        start_img = pygame.image.load('../images/button/play.png').convert_alpha()
        option_img = pygame.image.load('../images/button/option.png').convert_alpha()
        exit_img = pygame.image.load('../images/button/exit.png').convert_alpha()
        option_frame_img = pygame.image.load('../images/chess/Chess_board/option_frame.png').convert_alpha()
        option_frame_img = pygame.transform.scale(option_frame_img, (700, 500))
        btnBack_img = pygame.image.load('../images/button/arrow_back.png').convert_alpha()
        btnBack_img = pygame.transform.scale(btnBack_img, (35, 25))

        check_box_none_time = pygame.image.load('../images/button/check_box_none.png').convert_alpha()
        check_box_none_time =  pygame.transform.scale(check_box_none_time, (25, 25))

        check_box_checked_time = pygame.image.load('../images/button/check_box_checked.png').convert_alpha()
        check_box_checked_time =  pygame.transform.scale(check_box_checked_time, (25, 25))

        fontTime = pygame.font.Font('freesansbold.ttf', 17)
        fontTime = fontTime.render('Time', True, 'black')

        # create button munu
        start_button = button.Button(SCREEN_WIDTH // 2 - start_img.get_width() * 0.1 , SCREEN_HEIGHT // 2 - 190, start_img, 0.2)
        option_button = button.Button(SCREEN_WIDTH // 2 - option_img.get_width() * 0.1, SCREEN_HEIGHT // 2 - 120, option_img, 0.2)
        exit_button = button.Button(SCREEN_WIDTH // 2 - exit_img.get_width() * 0.1 , SCREEN_HEIGHT // 2 - 50, exit_img, 0.2)
        btnBack = button.Button(-1, 5, btnBack_img, 1)

        # game loop


        def update_option_frame_img(time, volume):
            option_frame_img = pygame.image.load('../images/chess/Chess_board/option_frame.png').convert_alpha()
            option_frame_img = pygame.transform.scale(option_frame_img, (700, 500))
            
            #option_frame_img.blit(check_box_checked, (150, 250))
            if (time == True):
                pygame.draw.rect(option_frame_img,(230, 241, 159),(150, 150, 25, 25))
                option_frame_img.blit(check_box_checked_time, (150, 150))
            else: 
                pygame.draw.rect(option_frame_img,(230, 241, 159),(150, 150, 25, 25))
                option_frame_img.blit(check_box_none_time, (150, 150))
            option_frame_img.blit(fontTime, (200, 157))
            return option_frame_img
        
                
        COLOR_INACTIVE = (100, 80, 255)
        COLOR_ACTIVE = (100, 200, 255)
        COLOR_LIST_INACTIVE = (255, 100, 100)
        COLOR_LIST_ACTIVE = (255, 150, 150)

        listTime = dropdown.DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        425, 200, 150, 30, 
        pygame.font.SysFont(None, 20), 
        "Cai dat thoi gian", ["Tinh thoi gian", "Khong tinh thoi gian"])

        listLevel = dropdown.DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        425, 250, 150, 30, 
        pygame.font.SysFont(None, 20), 
        "Config Level", ["Easy", "Medium", "Hard"])

        run = True
        while run:
            #clock.tick(30)
            screen.fill((202, 228, 241))
            screen.blit(option_frame_img, (150, 0))
            if (btnBack.draw(screen)):
                run = False
                if (listTime.main == 'Tinh thoi gian'):
                    data['Time'] = True
                else: data['Time'] = False

                if listLevel.main == 'Easy': data['Level'] = 1
                if listLevel.main == 'Medium': data['Level'] = 2
                if listLevel.main == 'Hard': data['Level'] = 3

                f = open('option.json', mode='w+')
                json.dump(data, f)
                f.close()
                return 'MENU_SCREEN'
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    run = False

            selected_option_time = listTime.update(event_list)
            if selected_option_time >= 0:
                listTime.main = listTime.options[selected_option_time]

            selected_option_level = listLevel.update(event_list)
            if selected_option_level >= 0:
                listLevel.main = listLevel.options[selected_option_level]

            #screen.fill((202, 228, 241))
            listLevel.draw(screen)
            listTime.draw(screen)
            
            pygame.display.flip()
        
        


        #pygame.quit()
        #exit()
        #while (running):
         #   screen.fill((202, 228, 241))
            # option_frame_img = update_option_frame_img(time, True)
            # screen.blit(option_frame_img, (150, 0))
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT: 
            #         running = False
            #         pygame.quit()
            #     if event.type == pygame.MOUSEBUTTONDOWN: 
            #         pos_x = pygame.mouse.get_pos()[0]
            #         pos_y = pygame.mouse.get_pos()[1]
                    
            #         if (303 <= pos_x <= 328 and 152 <= pos_y <= 177):  
            #             if (time == True): time = False
            #             else: time = True 
            #             option_frame_img = update_option_frame_img(time, True)
                        
            #     pygame.display.update()
            # screen.blit(option_frame_img, (150, 0))
            
        
        
            
        # if start_button.draw(screen):
        #     return 'PLAY_SCREEN'
        # if option_button.draw(screen):
        #     return 'OPTION_SCREEN'
        # if exit_button.draw(screen):
        #     return 'EXIT'
        # return 'MENU_SCREEN'
  