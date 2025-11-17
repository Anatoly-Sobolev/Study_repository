import pygame
import sys
from Game_consts import *

def game_over(red_player, blue_player, display):
    if red_player.score == score_max_number or blue_player.score == score_max_number:
        text_game_over = f'{['RED', 'BLUE'][red_player.score == score_max_number]} PLAYER WON'
        font = pygame.font.Font(None, 150)
        text_surface = font.render(text_game_over, True, ['RED', 'BLUE'][red_player.score == score_max_number])
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_w // 2, screen_h // 2)
        display.screen.blit(text_surface, text_rect)

        pygame.display.update()
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()

