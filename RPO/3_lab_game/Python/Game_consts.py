import pygame

screen_w = 1280
screen_h = 720
caption = "PONG GAME!"
paddle_h = 150
paddle_w = 15
blue_paddle_date = (0, screen_h/2 - paddle_h/2, paddle_w, paddle_h)
red_paddle_date = (screen_w - paddle_w, screen_h/2 - paddle_h/2, paddle_w, paddle_h)
ball_size = (30, 30)
mine_len = 65
speed_x = 10
speed_y = 8
ball_color = 'black'
backgroung = 240, 255, 240
color_player_1 = 'blue'
color_player_2 = 'red'
red_bomb = pygame.image.load('imeges/red_bomb (1).png')
blue_bomb = pygame.image.load('imeges/blue_bomb (1).png')
text_color = 'black'
score_max_number = 3