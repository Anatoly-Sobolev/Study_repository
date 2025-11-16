import pygame
import random
from Game_consts import *

class Mine:
    def __init__(self, last_tuch):
        self.rect = pygame.Rect(random.randint(0, screen_w-mine_len), random.randint(0, screen_h-mine_len), mine_len, mine_len)
        self.color = last_tuch



    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)