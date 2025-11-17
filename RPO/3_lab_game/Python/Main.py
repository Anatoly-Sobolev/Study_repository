import sys
import pygame

from Screen import Screen
from Ball import Ball
from Player import Player
from Game_consts import *
from Mine import Mine
from Game_over_condition import game_over

pygame.init()
game_display = Screen(screen_w, screen_h, caption)
ball = Ball(*ball_size, ball_color, screen_w, screen_h)
blue_player = Player(*blue_paddle_date, screen_h, color_player_1, pygame.K_w, pygame.K_s)
red_player = Player(*red_paddle_date, screen_h, color_player_2, pygame.K_UP, pygame.K_DOWN)
clock = pygame.time.Clock()

while True:

    game_display.screen.fill(backgroung)
    for enent in pygame.event.get():
        if enent.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        blue_player.check_push(enent)
        red_player.check_push(enent)

    game_display.update(ball, blue_player, red_player)
    pygame.display.update()
    clock.tick(60)

    game_over(red_player, blue_player, game_display)